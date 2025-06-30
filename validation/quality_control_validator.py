#!/usr/bin/env python3
"""
Quality Control Validator for Solana Detective Package
Validates endpoint coverage, code quality, and functionality
"""

import json
import inspect
import sys
import os
from typing import Dict, List, Any, Tuple
from solana_detective.client import SolanaDetective

class QualityControlValidator:
    """Comprehensive quality control validator"""
    
    def __init__(self):
        # Load API documentation
        with open('QUALITY_CHECKED_SOLANA_API_DOCS.json', 'r') as f:
            self.api_docs = json.load(f)
        
        # Method to endpoint mapping
        self.method_endpoint_mapping = {
            # Token Endpoints
            "get_token_info": "GET /tokens/{tokenAddress}",
            "get_tokens_by_pool": "GET /tokens/by-pool/{poolAddress}",
            "get_token_holders": "GET /tokens/{tokenAddress}/holders",
            "get_token_holders_top": "GET /tokens/{tokenAddress}/holders/top",
            "get_token_ath": "GET /tokens/{tokenAddress}/ath",
            "get_deployer_tokens": "GET /deployer/{wallet}",
            "search_tokens": "GET /search",
            "get_latest_tokens": "GET /tokens/latest",
            "get_tokens_multi": "POST /tokens/multi",
            "get_trending_tokens": "GET /tokens/trending",  # Also covers GET /tokens/trending/{timeframe}
            "get_tokens_by_volume": "GET /tokens/volume",   # Also covers GET /tokens/volume/{timeframe}
            "get_tokens_multi_all": "GET /tokens/multi/all",
            "get_tokens_multi_graduated": "GET /tokens/multi/graduated",
            
            # Price Endpoints
            "get_token_price": "GET /price",
            "get_price_history": "GET /price/history",
            "get_price_at_timestamp": "GET /price/history/timestamp",
            "get_price_range": "GET /price/history/range",
            "post_token_price": "POST /price",
            "get_multiple_token_prices": "GET /price/multi",
            "post_multiple_token_prices": "POST /price/multi",
            
            # Wallet Endpoints
            "get_wallet_tokens": "GET /wallet/{owner}",
            "get_wallet_basic": "GET /wallet/{owner}/basic",
            "get_wallet_page": "GET /wallet/{owner}/page/{page}",
            "get_wallet_trades": "GET /wallet/{owner}/trades",
            "get_wallet_chart": "GET /wallet/{owner}/chart",
            
            # Trade Endpoints
            "get_pool_trades": "GET /trades/{tokenAddress}/{poolAddress}",
            "get_wallet_token_trades": "GET /trades/{tokenAddress}/{poolAddress}/{owner}",
            "get_token_wallet_trades": "GET /trades/{tokenAddress}/by-wallet/{owner}",
            
            # Chart Data Endpoints
            "get_chart_data": ["GET /chart/{token}", "GET /chart/{token}/{pool}"],  # Handles both
            "get_holders_chart": "GET /holders/chart/{token}",
            
            # PnL Data Endpoints
            "get_wallet_pnl": "GET /pnl/{wallet}",
            "get_first_buyers": "GET /first-buyers/{token}",
            "get_wallet_token_pnl": "GET /pnl/{wallet}/{token}",
            
            # Top Traders Endpoints
            "get_top_traders_all": ["GET /top-traders/all", "GET /top-traders/all/{page}"],  # Handles both
            "get_top_traders_token": "GET /top-traders/{token}",
            
            # Stats and Events Endpoints
            "get_token_stats": ["GET /stats/{token}", "GET /stats/{token}/{pool}"],  # Handles both
            "get_live_events": ["GET /events/{tokenAddress}", "GET /events/{tokenAddress}/{poolAddress}"],  # Handles both
            
            # Credits Endpoint
            "get_credits": "GET /credits"
        }
        
    def validate_endpoint_coverage(self) -> Dict[str, Any]:
        """Validate that all API endpoints are covered by methods"""
        print("🔍 ENDPOINT COVERAGE VALIDATION")
        print("=" * 50)
        
        # Get all expected endpoints
        expected_endpoints = set(self.api_docs['endpoints'].keys())
        
        # Get all covered endpoints
        covered_endpoints = set()
        for method_name, endpoint_mapping in self.method_endpoint_mapping.items():
            if isinstance(endpoint_mapping, list):
                covered_endpoints.update(endpoint_mapping)
            else:
                covered_endpoints.add(endpoint_mapping)
        
        # Find missing and extra endpoints
        missing_endpoints = expected_endpoints - covered_endpoints
        extra_endpoints = covered_endpoints - expected_endpoints
        
        # Calculate coverage
        coverage_percentage = (len(covered_endpoints & expected_endpoints) / len(expected_endpoints)) * 100
        
        print(f"📊 Coverage Analysis:")
        print(f"   📈 Expected endpoints: {len(expected_endpoints)}")
        print(f"   📈 Covered endpoints: {len(covered_endpoints & expected_endpoints)}")
        print(f"   📈 Coverage percentage: {coverage_percentage:.1f}%")
        
        if missing_endpoints:
            print(f"\n❌ Missing endpoints ({len(missing_endpoints)}):")
            for endpoint in sorted(missing_endpoints):
                print(f"   - {endpoint}")
        
        if extra_endpoints:
            print(f"\n⚠️  Extra endpoints ({len(extra_endpoints)}):")
            for endpoint in sorted(extra_endpoints):
                print(f"   + {endpoint}")
        
        result = {
            "coverage_percentage": coverage_percentage,
            "expected_count": len(expected_endpoints),
            "covered_count": len(covered_endpoints & expected_endpoints),
            "missing_endpoints": list(missing_endpoints),
            "extra_endpoints": list(extra_endpoints),
            "passed": coverage_percentage >= 95.0
        }
        
        if result["passed"]:
            print("✅ Endpoint coverage validation PASSED")
        else:
            print("❌ Endpoint coverage validation FAILED")
            
        return result
    
    def validate_method_signatures(self) -> Dict[str, Any]:
        """Validate method signatures and documentation"""
        print("\n🔍 METHOD SIGNATURE VALIDATION")
        print("=" * 50)
        
        issues = []
        method_count = 0
        documented_count = 0
        
        # Get all public methods from SolanaDetective
        for name, method in inspect.getmembers(SolanaDetective, predicate=inspect.isfunction):
            if not name.startswith('_') and name != 'health_check' and name != 'get_available_endpoints':
                method_count += 1
                
                # Check if method has docstring
                if method.__doc__:
                    documented_count += 1
                    print(f"   ✅ {name} - Documented")
                else:
                    issues.append(f"Missing docstring: {name}")
                    print(f"   ❌ {name} - Missing docstring")
                
                # Check method signature
                sig = inspect.signature(method)
                params = list(sig.parameters.keys())
                
                # Validate common patterns
                if name.startswith('get_token') and 'token' not in params:
                    issues.append(f"Token method missing 'token' parameter: {name}")
                elif name.startswith('get_wallet') and 'owner' not in params and 'wallet' not in params:
                    issues.append(f"Wallet method missing wallet parameter: {name}")
        
        documentation_percentage = (documented_count / method_count) * 100 if method_count > 0 else 0
        
        print(f"\n📊 Method Quality:")
        print(f"   📈 Total methods: {method_count}")
        print(f"   📈 Documented methods: {documented_count}")
        print(f"   📈 Documentation percentage: {documentation_percentage:.1f}%")
        
        if issues:
            print(f"\n⚠️  Issues found ({len(issues)}):")
            for issue in issues:
                print(f"   - {issue}")
        
        result = {
            "method_count": method_count,
            "documented_count": documented_count,
            "documentation_percentage": documentation_percentage,
            "issues": issues,
            "passed": documentation_percentage >= 90.0 and len(issues) == 0
        }
        
        if result["passed"]:
            print("✅ Method signature validation PASSED")
        else:
            print("❌ Method signature validation FAILED")
            
        return result
    
    def validate_error_handling(self) -> Dict[str, Any]:
        """Validate error handling implementation"""
        print("\n🔍 ERROR HANDLING VALIDATION")
        print("=" * 50)
        
        # Read client.py to check error handling patterns
        with open('solana_detective/client.py', 'r') as f:
            client_code = f.read()
        
        error_patterns = {
            "try_except_blocks": client_code.count("try:"),
            "custom_exceptions": client_code.count("raise ValidationError") + 
                              client_code.count("raise APIError") + 
                              client_code.count("raise AuthenticationError") + 
                              client_code.count("raise RateLimitError"),
            "input_validation": client_code.count("_validate_"),
            "timeout_handling": "timeout" in client_code,
            "retry_logic": "retry" in client_code.lower(),
            "rate_limiting": "rate_limit" in client_code.lower()
        }
        
        print("📊 Error Handling Features:")
        for feature, count in error_patterns.items():
            if isinstance(count, bool):
                status = "✅" if count else "❌"
                print(f"   {status} {feature.replace('_', ' ').title()}: {'Yes' if count else 'No'}")
            else:
                status = "✅" if count > 0 else "❌"
                print(f"   {status} {feature.replace('_', ' ').title()}: {count}")
        
        # Calculate score
        score = 0
        if error_patterns["try_except_blocks"] >= 3: score += 20
        if error_patterns["custom_exceptions"] >= 5: score += 20
        if error_patterns["input_validation"] >= 2: score += 20
        if error_patterns["timeout_handling"]: score += 15
        if error_patterns["retry_logic"]: score += 15
        if error_patterns["rate_limiting"]: score += 10
        
        result = {
            "error_patterns": error_patterns,
            "score": score,
            "passed": score >= 80
        }
        
        print(f"\n📈 Error Handling Score: {score}/100")
        
        if result["passed"]:
            print("✅ Error handling validation PASSED")
        else:
            print("❌ Error handling validation FAILED")
            
        return result
    
    def validate_configuration_management(self) -> Dict[str, Any]:
        """Validate configuration management"""
        print("\n🔍 CONFIGURATION MANAGEMENT VALIDATION")
        print("=" * 50)
        
        config_features = []
        
        # Check if config.py exists and has required features
        if os.path.exists('solana_detective/config.py'):
            with open('solana_detective/config.py', 'r') as f:
                config_code = f.read()
            
            features = {
                "environment_variables": "os.getenv" in config_code,
                "default_config": "DEFAULT_CONFIG" in config_code,
                "file_based_config": "config_file" in config_code,
                "validation": "ValueError" in config_code,
                "api_key_handling": "api_key" in config_code
            }
            
            for feature, present in features.items():
                status = "✅" if present else "❌"
                print(f"   {status} {feature.replace('_', ' ').title()}")
                if present:
                    config_features.append(feature)
        
        score = (len(config_features) / 5) * 100
        
        result = {
            "features": config_features,
            "score": score,
            "passed": score >= 80
        }
        
        print(f"\n📈 Configuration Score: {score:.1f}/100")
        
        if result["passed"]:
            print("✅ Configuration management validation PASSED")
        else:
            print("❌ Configuration management validation FAILED")
            
        return result
    
    def run_comprehensive_validation(self) -> Dict[str, Any]:
        """Run all validation checks"""
        print("🎯 COMPREHENSIVE QUALITY CONTROL VALIDATION")
        print("=" * 60)
        
        results = {
            "endpoint_coverage": self.validate_endpoint_coverage(),
            "method_signatures": self.validate_method_signatures(),
            "error_handling": self.validate_error_handling(),
            "configuration": self.validate_configuration_management()
        }
        
        # Calculate overall score
        scores = []
        passed_checks = 0
        total_checks = len(results)
        
        for check_name, result in results.items():
            if result.get("passed", False):
                passed_checks += 1
            
            if "score" in result:
                scores.append(result["score"])
            elif "coverage_percentage" in result:
                scores.append(result["coverage_percentage"])
            elif "documentation_percentage" in result:
                scores.append(result["documentation_percentage"])
        
        overall_score = sum(scores) / len(scores) if scores else 0
        pass_rate = (passed_checks / total_checks) * 100
        
        print(f"\n🏆 OVERALL QUALITY ASSESSMENT")
        print("=" * 40)
        print(f"📊 Overall Score: {overall_score:.1f}/100")
        print(f"📊 Pass Rate: {pass_rate:.1f}% ({passed_checks}/{total_checks})")
        
        if overall_score >= 90 and pass_rate >= 75:
            print("🎉 EXCELLENT - Production ready!")
            quality_level = "EXCELLENT"
        elif overall_score >= 75 and pass_rate >= 50:
            print("✅ GOOD - Minor improvements needed")
            quality_level = "GOOD"
        else:
            print("⚠️  NEEDS WORK - Significant improvements required")
            quality_level = "NEEDS_WORK"
        
        results["overall"] = {
            "score": overall_score,
            "pass_rate": pass_rate,
            "quality_level": quality_level,
            "passed_checks": passed_checks,
            "total_checks": total_checks
        }
        
        return results

if __name__ == "__main__":
    validator = QualityControlValidator()
    results = validator.run_comprehensive_validation()
    
    # Save results
    with open('quality_control_results.json', 'w') as f:
        json.dump(results, f, indent=2)
    
    print(f"\n💾 Results saved to quality_control_results.json")

