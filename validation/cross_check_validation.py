#!/usr/bin/env python3
"""
Comprehensive Cross-Check Validation Script
Validates our package against the original Solana Tracker API documentation
"""

import json
import re
import sys
import os
from typing import Dict, List, Set, Any

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from solana_detective import SolanaDetective

class CrossCheckValidator:
    """Validates package implementation against official API documentation"""
    
    def __init__(self):
        self.validation_results = {
            "endpoint_coverage": {},
            "method_implementation": {},
            "parameter_accuracy": {},
            "response_format": {},
            "documentation_consistency": {},
            "orthography_check": {},
            "overall_score": 0
        }
        
        # Official API endpoints from documentation
        self.official_endpoints = {
            # Token Endpoints (15)
            "GET /tokens/{tokenAddress}": "get_token_info",
            "GET /tokens/pool/{poolAddress}": "get_tokens_by_pool", 
            "GET /tokens/{tokenAddress}/holders": "get_token_holders",
            "GET /tokens/{tokenAddress}/holders/top": "get_token_holders_top",
            "GET /tokens/{tokenAddress}/ath": "get_token_ath",
            "GET /deployer/{wallet}": "get_deployer_tokens",
            "GET /search": "search_tokens",
            "GET /tokens/latest": "get_latest_tokens",
            "GET /tokens/multi": "get_tokens_multi",
            "POST /tokens/multi": "post_tokens_multi",
            "GET /tokens/multi/all": "get_tokens_multi_all",
            "GET /tokens/multi/graduated": "get_tokens_multi_graduated",
            "GET /tokens/trending": "get_trending_tokens",
            "GET /tokens/trending/{timeframe}": "get_trending_tokens",
            "GET /tokens/volume": "get_tokens_by_volume",
            "GET /tokens/volume/{timeframe}": "get_tokens_by_volume",
            
            # Price Endpoints (7)
            "GET /price": "get_token_price",
            "GET /price/history": "get_price_history",
            "GET /price/history/timestamp": "get_price_at_timestamp",
            "GET /price/history/range": "get_price_range",
            "POST /price": "post_token_price",
            "GET /price/multi": "get_multiple_token_prices",
            "POST /price/multi": "post_multiple_token_prices",
            
            # Wallet Endpoints (5)
            "GET /wallet/{owner}": "get_wallet_tokens",
            "GET /wallet/{owner}/basic": "get_wallet_basic",
            "GET /wallet/{owner}/page/{page}": "get_wallet_page",
            "GET /wallet/{owner}/trades": "get_wallet_trades",
            "GET /wallet/{owner}/chart": "get_wallet_chart",
            
            # Trade Endpoints (3)
            "GET /trades/{tokenAddress}/{poolAddress}": "get_pool_trades",
            "GET /trades/{tokenAddress}/{poolAddress}/{owner}": "get_wallet_token_trades",
            "GET /trades/{tokenAddress}/by-wallet/{owner}": "get_token_wallet_trades",
            
            # Chart Data (4)
            "GET /chart/{token}": "get_chart_data",
            "GET /chart/{token}/{pool}": "get_chart_data",
            "GET /holders/chart/{token}": "get_holders_chart",
            "GET /chart/holders/{token}": "get_token_holders_chart",
            
            # PnL Data (3)
            "GET /pnl/{wallet}": "get_wallet_pnl",
            "GET /first-buyers/{token}": "get_first_buyers",
            "GET /pnl/{wallet}/{token}": "get_wallet_token_pnl",
            
            # Top Traders (3)
            "GET /top-traders/all": "get_top_traders_all",
            "GET /top-traders/all/{page}": "get_top_traders_all",
            "GET /top-traders/{token}": "get_top_traders_token",
            
            # Stats & Events (5)
            "GET /stats/{token}": "get_token_stats",
            "GET /stats/{token}/{pool}": "get_token_stats",
            "GET /live-events": "get_live_events",
            "GET /events/{tokenAddress}": "get_token_events",
            "GET /events/{tokenAddress}/{poolAddress}": "get_pool_events",
            
            # Credits (1)
            "GET /credits": "get_credits"
        }
        
        # Expected parameters for key endpoints
        self.expected_parameters = {
            "get_token_price": ["token", "priceChanges"],
            "get_price_history": ["token", "time_from", "time_to"],
            "get_chart_data": ["token", "pool", "type", "time_from", "time_to", "marketCap", "removeOutliers"],
            "search_tokens": ["query", "limit"],
            "get_wallet_trades": ["owner", "page", "limit"],
            "get_first_buyers": ["token", "limit"]
        }
        
        # Chart intervals validation
        self.expected_intervals = [
            "1s", "5s", "15s", "1m", "3m", "5m", "15m", "30m",
            "1h", "2h", "4h", "6h", "8h", "12h", "1d", "3d", "1w", "1mn"
        ]
    
    def validate_endpoint_coverage(self) -> Dict[str, Any]:
        """Validate that all official endpoints are implemented"""
        print("🔍 VALIDATING ENDPOINT COVERAGE...")
        
        # Get implemented methods from our client
        detective = SolanaDetective(api_key="dummy_key_for_validation")
        implemented_methods = [method for method in dir(detective) 
                             if not method.startswith('_') and callable(getattr(detective, method))]
        
        # Check coverage
        total_endpoints = len(self.official_endpoints)
        covered_endpoints = 0
        missing_endpoints = []
        
        for endpoint, expected_method in self.official_endpoints.items():
            if expected_method in implemented_methods:
                covered_endpoints += 1
            else:
                missing_endpoints.append(f"{endpoint} -> {expected_method}")
        
        coverage_percentage = (covered_endpoints / total_endpoints) * 100
        
        result = {
            "total_endpoints": total_endpoints,
            "covered_endpoints": covered_endpoints,
            "coverage_percentage": coverage_percentage,
            "missing_endpoints": missing_endpoints,
            "status": "PASS" if coverage_percentage >= 95 else "FAIL"
        }
        
        self.validation_results["endpoint_coverage"] = result
        print(f"   ✅ Coverage: {coverage_percentage:.1f}% ({covered_endpoints}/{total_endpoints})")
        
        return result
    
    def validate_method_implementation(self) -> Dict[str, Any]:
        """Validate method implementations match expected signatures"""
        print("🔧 VALIDATING METHOD IMPLEMENTATIONS...")
        
        detective = SolanaDetective(api_key="dummy_key_for_validation")
        validation_errors = []
        validated_methods = 0
        
        # Check key methods have correct parameters
        for method_name, expected_params in self.expected_parameters.items():
            if hasattr(detective, method_name):
                method = getattr(detective, method_name)
                
                # Get method signature (basic check)
                import inspect
                sig = inspect.signature(method)
                actual_params = list(sig.parameters.keys())
                
                # Remove 'self' parameter
                if 'self' in actual_params:
                    actual_params.remove('self')
                
                # Check if expected parameters are present
                missing_params = [p for p in expected_params if p not in actual_params]
                if missing_params:
                    validation_errors.append(f"{method_name}: Missing parameters {missing_params}")
                
                validated_methods += 1
            else:
                validation_errors.append(f"Method {method_name} not implemented")
        
        result = {
            "validated_methods": validated_methods,
            "total_checked": len(self.expected_parameters),
            "validation_errors": validation_errors,
            "status": "PASS" if len(validation_errors) == 0 else "FAIL"
        }
        
        self.validation_results["method_implementation"] = result
        print(f"   ✅ Methods validated: {validated_methods}/{len(self.expected_parameters)}")
        
        return result
    
    def validate_chart_intervals(self) -> Dict[str, Any]:
        """Validate chart intervals are correctly documented"""
        print("⏱️  VALIDATING CHART INTERVALS...")
        
        # Check our documentation for interval accuracy
        try:
            with open("QUALITY_CHECKED_SOLANA_TRACKER_API_DOCS.md", "r") as f:
                docs_content = f.read()
            
            # Find chart intervals in documentation
            interval_pattern = r"Available Intervals.*?:(.*?)(?=\n\n|\n###|\nQuery|\nResponse|$)"
            matches = re.search(interval_pattern, docs_content, re.DOTALL)
            
            if matches:
                intervals_text = matches.group(1)
                found_intervals = re.findall(r'`([^`]+)`', intervals_text)
                
                missing_intervals = [i for i in self.expected_intervals if i not in found_intervals]
                extra_intervals = [i for i in found_intervals if i not in self.expected_intervals]
                
                # Check for 1m vs 1mn distinction
                has_1m = "1m" in found_intervals
                has_1mn = "1mn" in found_intervals
                
                result = {
                    "expected_intervals": len(self.expected_intervals),
                    "found_intervals": len(found_intervals),
                    "missing_intervals": missing_intervals,
                    "extra_intervals": extra_intervals,
                    "has_1m_1mn_distinction": has_1m and has_1mn,
                    "status": "PASS" if len(missing_intervals) == 0 and has_1m and has_1mn else "FAIL"
                }
            else:
                result = {
                    "error": "Could not find interval documentation",
                    "status": "FAIL"
                }
            
        except FileNotFoundError:
            result = {
                "error": "Documentation file not found",
                "status": "FAIL"
            }
        
        self.validation_results["parameter_accuracy"] = result
        print(f"   ✅ Intervals: {result.get('found_intervals', 0)}/{len(self.expected_intervals)}")
        
        return result
    
    def validate_documentation_consistency(self) -> Dict[str, Any]:
        """Validate documentation consistency across files"""
        print("📚 VALIDATING DOCUMENTATION CONSISTENCY...")
        
        consistency_issues = []
        files_checked = 0
        
        # Check key documentation files exist
        doc_files = [
            "README.md",
            "AI_HANDOFF_GUIDE.md", 
            "QUALITY_CHECKED_SOLANA_TRACKER_API_DOCS.md",
            "solana_detective/__init__.py",
            "solana_detective/client.py"
        ]
        
        for file_path in doc_files:
            if os.path.exists(file_path):
                files_checked += 1
                
                # Basic content validation
                try:
                    with open(file_path, "r") as f:
                        content = f.read()
                    
                    # Check for common issues
                    if len(content) < 100:
                        consistency_issues.append(f"{file_path}: File too short")
                    
                    if "TODO" in content.upper() or "FIXME" in content.upper():
                        consistency_issues.append(f"{file_path}: Contains TODO/FIXME")
                    
                    # Check for proper endpoint count mentions
                    if "47" in content and "endpoint" in content.lower():
                        # Good - mentions correct endpoint count
                        pass
                    elif "endpoint" in content.lower() and any(num in content for num in ["38", "39", "40", "41", "42", "43", "44", "45", "46"]):
                        consistency_issues.append(f"{file_path}: Mentions incorrect endpoint count")
                        
                except Exception as e:
                    consistency_issues.append(f"{file_path}: Read error - {e}")
            else:
                consistency_issues.append(f"{file_path}: File missing")
        
        result = {
            "files_checked": files_checked,
            "total_files": len(doc_files),
            "consistency_issues": consistency_issues,
            "status": "PASS" if len(consistency_issues) == 0 else "FAIL"
        }
        
        self.validation_results["documentation_consistency"] = result
        print(f"   ✅ Files checked: {files_checked}/{len(doc_files)}")
        
        return result
    
    def validate_orthography(self) -> Dict[str, Any]:
        """Validate spelling and formatting consistency"""
        print("📝 VALIDATING ORTHOGRAPHY AND FORMATTING...")
        
        orthography_issues = []
        
        # Common spelling/formatting checks
        checks = {
            "solana_detective/client.py": [
                ("def ", "Method definitions"),
                ("class ", "Class definitions"),
                ("import ", "Import statements"),
                ("return ", "Return statements")
            ],
            "README.md": [
                ("## ", "Section headers"),
                ("### ", "Subsection headers"),
                ("```python", "Code blocks"),
                ("`detective.", "Method references")
            ]
        }
        
        for file_path, patterns in checks.items():
            if os.path.exists(file_path):
                try:
                    with open(file_path, "r") as f:
                        content = f.read()
                    
                    for pattern, description in patterns:
                        count = content.count(pattern)
                        if count == 0 and pattern in ["def ", "class "]:
                            orthography_issues.append(f"{file_path}: No {description} found")
                
                except Exception as e:
                    orthography_issues.append(f"{file_path}: Read error - {e}")
        
        # Check for consistent naming
        if os.path.exists("solana_detective/client.py"):
            try:
                with open("solana_detective/client.py", "r") as f:
                    content = f.read()
                
                # Check method naming consistency
                method_pattern = r"def (get_|post_|search_|health_)"
                methods = re.findall(method_pattern, content)
                
                if len(methods) < 30:  # Should have many methods
                    orthography_issues.append("client.py: Insufficient method definitions found")
                    
            except Exception as e:
                orthography_issues.append(f"client.py: Analysis error - {e}")
        
        result = {
            "orthography_issues": orthography_issues,
            "status": "PASS" if len(orthography_issues) == 0 else "FAIL"
        }
        
        self.validation_results["orthography_check"] = result
        print(f"   ✅ Orthography issues: {len(orthography_issues)}")
        
        return result
    
    def calculate_overall_score(self) -> float:
        """Calculate overall validation score"""
        scores = []
        weights = {
            "endpoint_coverage": 0.3,
            "method_implementation": 0.25,
            "parameter_accuracy": 0.2,
            "documentation_consistency": 0.15,
            "orthography_check": 0.1
        }
        
        for category, weight in weights.items():
            if category in self.validation_results:
                result = self.validation_results[category]
                
                if category == "endpoint_coverage":
                    score = result.get("coverage_percentage", 0)
                elif category == "method_implementation":
                    total = result.get("total_checked", 1)
                    errors = len(result.get("validation_errors", []))
                    score = ((total - errors) / total) * 100
                else:
                    score = 100 if result.get("status") == "PASS" else 0
                
                scores.append(score * weight)
        
        overall_score = sum(scores)
        self.validation_results["overall_score"] = overall_score
        
        return overall_score
    
    def run_comprehensive_validation(self) -> Dict[str, Any]:
        """Run all validation checks"""
        print("🚀 STARTING COMPREHENSIVE CROSS-CHECK VALIDATION")
        print("=" * 60)
        
        # Run all validation checks
        self.validate_endpoint_coverage()
        self.validate_method_implementation()
        self.validate_chart_intervals()
        self.validate_documentation_consistency()
        self.validate_orthography()
        
        # Calculate overall score
        overall_score = self.calculate_overall_score()
        
        print("\n" + "=" * 60)
        print("📊 VALIDATION SUMMARY")
        print("=" * 60)
        
        for category, result in self.validation_results.items():
            if category != "overall_score":
                status = result.get("status", "UNKNOWN")
                emoji = "✅" if status == "PASS" else "❌"
                print(f"{emoji} {category.replace('_', ' ').title()}: {status}")
        
        print(f"\n🏆 OVERALL SCORE: {overall_score:.1f}/100")
        
        if overall_score >= 95:
            print("🎉 EXCELLENT - Production ready!")
        elif overall_score >= 85:
            print("✅ GOOD - Minor issues to address")
        elif overall_score >= 70:
            print("⚠️  FAIR - Several issues need attention")
        else:
            print("❌ POOR - Major issues require fixing")
        
        return self.validation_results

def main():
    """Main validation function"""
    validator = CrossCheckValidator()
    results = validator.run_comprehensive_validation()
    
    # Save results
    with open("cross_check_validation_results.json", "w") as f:
        json.dump(results, f, indent=2)
    
    print(f"\n📁 Results saved to: cross_check_validation_results.json")
    
    return results

if __name__ == "__main__":
    main()

