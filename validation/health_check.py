#!/usr/bin/env python3
"""
Solana Detective Health Check
Quick operational test to verify package functionality
"""

import sys
import os
import json
from datetime import datetime

# Add package to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def print_status(message, status="INFO"):
    """Print formatted status message"""
    timestamp = datetime.now().strftime("%H:%M:%S")
    symbols = {"INFO": "ℹ️", "SUCCESS": "✅", "ERROR": "❌", "WARNING": "⚠️"}
    symbol = symbols.get(status, "ℹ️")
    print(f"[{timestamp}] {symbol} {message}")

def test_package_import():
    """Test if the package can be imported"""
    try:
        from solana_detective import SolanaDetective
        print_status("Package imported successfully", "SUCCESS")
        return True
    except ImportError as e:
        print_status(f"Package import failed: {e}", "ERROR")
        return False

def test_configuration():
    """Test configuration setup"""
    try:
        from solana_detective.config import Config
        
        # Try to load config
        config = Config()
        
        if config.api_key:
            print_status("API key configured", "SUCCESS")
        else:
            print_status("API key not configured", "WARNING")
            return False
            
        print_status(f"Base URL: {config.base_url}", "INFO")
        return True
        
    except Exception as e:
        print_status(f"Configuration test failed: {e}", "ERROR")
        return False

def test_api_connectivity():
    """Test basic API connectivity"""
    try:
        from solana_detective import SolanaDetective
        
        # Initialize client
        detective = SolanaDetective()
        print_status("Client initialized", "SUCCESS")
        
        # Test with credits endpoint (minimal API call)
        credits = detective.get_credits()
        print_status(f"API connectivity successful. Credits: {credits}", "SUCCESS")
        return True
        
    except Exception as e:
        print_status(f"API connectivity failed: {e}", "ERROR")
        return False

def test_basic_functionality():
    """Test basic functionality with a simple API call"""
    try:
        from solana_detective import SolanaDetective
        
        detective = SolanaDetective()
        
        # Test with a well-known token (SOL)
        sol_token = "So11111111111111111111111111111111111111112"
        token_info = detective.get_token_info(sol_token)
        
        if token_info and 'token' in token_info:
            token_name = token_info['token'].get('name', 'Unknown')
            print_status(f"Basic functionality test passed. Token: {token_name}", "SUCCESS")
            return True
        else:
            print_status("Basic functionality test failed: Invalid response", "ERROR")
            return False
            
    except Exception as e:
        print_status(f"Basic functionality test failed: {e}", "ERROR")
        return False

def test_error_handling():
    """Test error handling with invalid input"""
    try:
        from solana_detective import SolanaDetective
        
        detective = SolanaDetective()
        
        # Test with invalid token address
        try:
            detective.get_token_info("invalid_address")
            print_status("Error handling test failed: Should have raised exception", "ERROR")
            return False
        except Exception:
            print_status("Error handling test passed", "SUCCESS")
            return True
            
    except Exception as e:
        print_status(f"Error handling test failed: {e}", "ERROR")
        return False

def main():
    """Run all health checks"""
    print_status("Starting Solana Detective Health Check", "INFO")
    print("=" * 60)
    
    tests = [
        ("Package Import", test_package_import),
        ("Configuration", test_configuration),
        ("API Connectivity", test_api_connectivity),
        ("Basic Functionality", test_basic_functionality),
        ("Error Handling", test_error_handling)
    ]
    
    results = {}
    
    for test_name, test_func in tests:
        print_status(f"Running {test_name} test...", "INFO")
        try:
            results[test_name] = test_func()
        except Exception as e:
            print_status(f"{test_name} test crashed: {e}", "ERROR")
            results[test_name] = False
        print()
    
    # Summary
    print("=" * 60)
    print_status("Health Check Summary", "INFO")
    
    passed = sum(results.values())
    total = len(results)
    
    for test_name, result in results.items():
        status = "SUCCESS" if result else "ERROR"
        print_status(f"{test_name}: {'PASS' if result else 'FAIL'}", status)
    
    print()
    if passed == total:
        print_status(f"All tests passed ({passed}/{total})", "SUCCESS")
        print_status("Solana Detective is ready for use!", "SUCCESS")
        return 0
    else:
        print_status(f"Some tests failed ({passed}/{total})", "ERROR")
        print_status("Please check the errors above and refer to TROUBLESHOOTING.md", "WARNING")
        return 1

if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code)

