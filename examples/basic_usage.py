#!/usr/bin/env python3
"""
Solana Detective - Basic Usage Examples
Simple examples demonstrating core functionality
"""

import sys
import os
from datetime import datetime

# Add package to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from solana_detective import SolanaDetective

def example_1_token_info():
    """Example 1: Get basic token information"""
    print("🪙 Example 1: Token Information")
    print("-" * 40)
    
    detective = SolanaDetective()
    
    # Get info for SOL token
    sol_token = "So11111111111111111111111111111111111111112"
    token_info = detective.get_token_info(sol_token)
    
    if token_info and 'token' in token_info:
        token = token_info['token']
        print(f"Name: {token.get('name', 'N/A')}")
        print(f"Symbol: {token.get('symbol', 'N/A')}")
        print(f"Decimals: {token.get('decimals', 'N/A')}")
        
        if 'pools' in token_info and token_info['pools']:
            pool = token_info['pools'][0]
            price = pool.get('price', {}).get('usd', 'N/A')
            print(f"Price: ${price}")
    
    print()

def example_2_token_price():
    """Example 2: Get current token price"""
    print("💰 Example 2: Token Price")
    print("-" * 40)
    
    detective = SolanaDetective()
    
    # Get price for SOL
    sol_token = "So11111111111111111111111111111111111111112"
    price_info = detective.get_token_price(sol_token)
    
    if price_info:
        price = price_info.get('price', 'N/A')
        print(f"SOL Price: ${price} USD")
    
    print()

def example_3_wallet_tokens():
    """Example 3: Get wallet token holdings"""
    print("👛 Example 3: Wallet Holdings")
    print("-" * 40)
    
    detective = SolanaDetective()
    
    # Example wallet (replace with actual wallet)
    wallet_address = "AB9RndvzedBPXqUrbYPZ8dMdLvfD9yozDdvg9Tkxg68X"
    
    try:
        wallet_info = detective.get_wallet_tokens(wallet_address)
        
        if wallet_info and 'tokens' in wallet_info:
            tokens = wallet_info['tokens']
            total_value = wallet_info.get('total', 0)
            
            print(f"Total Portfolio Value: ${total_value:.2f}")
            print(f"Number of Tokens: {len(tokens)}")
            
            # Show top 3 holdings
            print("\nTop Holdings:")
            for i, token in enumerate(tokens[:3]):
                symbol = token.get('token', {}).get('symbol', 'Unknown')
                balance = token.get('balance', 0)
                value = token.get('value', 0)
                print(f"  {i+1}. {symbol}: {balance:.2f} (${value:.2f})")
        
    except Exception as e:
        print(f"Error: {e}")
    
    print()

def example_4_token_ath():
    """Example 4: Get token all-time high"""
    print("📈 Example 4: Token All-Time High")
    print("-" * 40)
    
    detective = SolanaDetective()
    
    # Example token
    token_address = "So11111111111111111111111111111111111111112"
    
    try:
        ath_info = detective.get_token_ath(token_address)
        
        if ath_info:
            ath_price = ath_info.get('highest_price', 'N/A')
            ath_mcap = ath_info.get('highest_market_cap', 'N/A')
            timestamp = ath_info.get('timestamp', 0)
            
            if timestamp:
                ath_date = datetime.fromtimestamp(timestamp / 1000)
                ath_date_str = ath_date.strftime('%Y-%m-%d %H:%M:%S')
            else:
                ath_date_str = 'N/A'
            
            print(f"ATH Price: ${ath_price}")
            print(f"ATH Market Cap: ${ath_mcap:,.2f}" if isinstance(ath_mcap, (int, float)) else f"ATH Market Cap: {ath_mcap}")
            print(f"ATH Date: {ath_date_str}")
    
    except Exception as e:
        print(f"Error: {e}")
    
    print()

def example_5_trending_tokens():
    """Example 5: Get trending tokens"""
    print("🔥 Example 5: Trending Tokens")
    print("-" * 40)
    
    detective = SolanaDetective()
    
    try:
        trending = detective.get_trending_tokens()
        
        if trending and isinstance(trending, list):
            print("Top Trending Tokens:")
            for i, token in enumerate(trending[:5]):
                name = token.get('name', 'Unknown')
                symbol = token.get('symbol', 'Unknown')
                price = token.get('price', {}).get('usd', 'N/A')
                print(f"  {i+1}. {name} ({symbol}): ${price}")
    
    except Exception as e:
        print(f"Error: {e}")
    
    print()

def example_6_wallet_trades():
    """Example 6: Get wallet trading history"""
    print("📊 Example 6: Wallet Trades")
    print("-" * 40)
    
    detective = SolanaDetective()
    
    # Example wallet
    wallet_address = "AB9RndvzedBPXqUrbYPZ8dMdLvfD9yozDdvg9Tkxg68X"
    
    try:
        trades = detective.get_wallet_trades(wallet_address)
        
        if trades and 'trades' in trades:
            trade_list = trades['trades']
            print(f"Total Trades Found: {len(trade_list)}")
            
            if trade_list:
                print("\nRecent Trades:")
                for i, trade in enumerate(trade_list[:3]):
                    from_token = trade.get('from', {}).get('token', {}).get('symbol', 'Unknown')
                    to_token = trade.get('to', {}).get('token', {}).get('symbol', 'Unknown')
                    volume = trade.get('volume', {}).get('usd', 0)
                    timestamp = trade.get('time', 0)
                    
                    if timestamp:
                        trade_date = datetime.fromtimestamp(timestamp / 1000)
                        date_str = trade_date.strftime('%Y-%m-%d %H:%M')
                    else:
                        date_str = 'Unknown'
                    
                    print(f"  {i+1}. {from_token} → {to_token}: ${volume:.2f} ({date_str})")
    
    except Exception as e:
        print(f"Error: {e}")
    
    print()

def example_7_api_credits():
    """Example 7: Check API credits"""
    print("⚡ Example 7: API Credits")
    print("-" * 40)
    
    detective = SolanaDetective()
    
    try:
        credits = detective.get_credits()
        print(f"Remaining API Credits: {credits}")
    
    except Exception as e:
        print(f"Error: {e}")
    
    print()

def example_8_error_handling():
    """Example 8: Error handling demonstration"""
    print("🚨 Example 8: Error Handling")
    print("-" * 40)
    
    detective = SolanaDetective()
    
    # Try with invalid token address
    try:
        result = detective.get_token_info("invalid_address")
        print("This shouldn't print - invalid address should fail")
    except Exception as e:
        print(f"✅ Correctly caught error: {type(e).__name__}")
        print(f"   Error message: {str(e)[:100]}...")
    
    print()

def main():
    """Run all basic examples"""
    print("🔍 Solana Detective - Basic Usage Examples")
    print("=" * 60)
    print()
    
    # Check if API key is configured
    try:
        detective = SolanaDetective()
        print("✅ API key configured, running examples...\n")
    except Exception as e:
        print(f"❌ API key not configured: {e}")
        print("Please set SOLANA_TRACKER_API_KEY environment variable or update config.json")
        return
    
    examples = [
        example_1_token_info,
        example_2_token_price,
        example_3_wallet_tokens,
        example_4_token_ath,
        example_5_trending_tokens,
        example_6_wallet_trades,
        example_7_api_credits,
        example_8_error_handling
    ]
    
    for example_func in examples:
        try:
            example_func()
        except Exception as e:
            print(f"❌ Example failed: {e}\n")
    
    print("=" * 60)
    print("✅ Basic examples completed!")
    print("See advanced_analysis.py for more complex usage patterns.")

if __name__ == "__main__":
    main()

