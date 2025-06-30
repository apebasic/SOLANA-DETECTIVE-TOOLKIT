#!/usr/bin/env python3
"""
Solana Detective - Advanced Analysis Examples
Complex multi-endpoint analysis patterns and workflows
"""

import sys
import os
from datetime import datetime, timezone
import pytz

# Add package to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from solana_detective import SolanaDetective

def advanced_1_wallet_pnl_analysis():
    """Advanced 1: Complete wallet PnL analysis"""
    print("💹 Advanced 1: Wallet PnL Analysis")
    print("-" * 50)
    
    detective = SolanaDetective()
    wallet_address = "AB9RndvzedBPXqUrbYPZ8dMdLvfD9yozDdvg9Tkxg68X"
    
    try:
        # Get wallet trades
        trades_data = detective.get_wallet_trades(wallet_address)
        
        if not trades_data or 'trades' not in trades_data:
            print("No trades found for this wallet")
            return
        
        trades = trades_data['trades']
        print(f"Analyzing {len(trades)} trades...")
        
        # Group trades by token
        token_trades = {}
        for trade in trades:
            to_token_addr = trade.get('to', {}).get('address')
            if to_token_addr:
                if to_token_addr not in token_trades:
                    token_trades[to_token_addr] = {'buys': [], 'sells': []}
                
                # Determine if this is a buy or sell based on the trade direction
                from_token = trade.get('from', {}).get('token', {}).get('symbol', '')
                to_token = trade.get('to', {}).get('token', {}).get('symbol', '')
                
                if from_token in ['USDC', 'SOL', 'WSOL']:  # Buying with stablecoin/SOL
                    token_trades[to_token_addr]['buys'].append(trade)
                else:  # Selling for stablecoin/SOL
                    token_trades[to_token_addr]['sells'].append(trade)
        
        # Analyze each token's performance
        print("\nToken Performance Analysis:")
        for token_addr, token_data in list(token_trades.items())[:3]:  # Top 3 tokens
            buys = token_data['buys']
            sells = token_data['sells']
            
            if not buys:
                continue
                
            # Get token info
            try:
                token_info = detective.get_token_info(token_addr)
                token_name = token_info.get('token', {}).get('symbol', 'Unknown')
            except:
                token_name = 'Unknown'
            
            print(f"\n📊 {token_name} ({token_addr[:8]}...)")
            print(f"   Buys: {len(buys)}, Sells: {len(sells)}")
            
            # Calculate total invested
            total_invested = sum(trade.get('volume', {}).get('usd', 0) for trade in buys)
            total_received = sum(trade.get('volume', {}).get('usd', 0) for trade in sells)
            
            print(f"   Total Invested: ${total_invested:.2f}")
            print(f"   Total Received: ${total_received:.2f}")
            
            if sells:
                realized_pnl = total_received - total_invested
                print(f"   Realized PnL: ${realized_pnl:.2f}")
    
    except Exception as e:
        print(f"Error in PnL analysis: {e}")
    
    print()

def advanced_2_token_momentum_analysis():
    """Advanced 2: Token momentum and trend analysis"""
    print("📈 Advanced 2: Token Momentum Analysis")
    print("-" * 50)
    
    detective = SolanaDetective()
    
    try:
        # Get trending tokens
        trending = detective.get_trending_tokens()
        
        if not trending:
            print("No trending data available")
            return
        
        print("Analyzing top trending tokens...")
        
        for i, token in enumerate(trending[:3]):
            token_addr = token.get('mint', token.get('address'))
            if not token_addr:
                continue
                
            symbol = token.get('symbol', 'Unknown')
            print(f"\n🔥 #{i+1}: {symbol}")
            
            # Get detailed token info
            try:
                token_info = detective.get_token_info(token_addr)
                
                if token_info and 'events' in token_info:
                    events = token_info['events']
                    
                    # Analyze price changes
                    timeframes = ['1h', '24h']
                    for tf in timeframes:
                        if tf in events:
                            change = events[tf].get('priceChangePercentage', 0)
                            print(f"   {tf} change: {change:.2f}%")
                
                # Get ATH data
                ath_data = detective.get_token_ath(token_addr)
                if ath_data:
                    ath_price = ath_data.get('highest_price', 0)
                    current_price = token.get('price', {}).get('usd', 0)
                    
                    if ath_price and current_price:
                        distance_from_ath = ((ath_price - current_price) / ath_price) * 100
                        print(f"   Distance from ATH: {distance_from_ath:.1f}%")
            
            except Exception as e:
                print(f"   Error analyzing {symbol}: {e}")
    
    except Exception as e:
        print(f"Error in momentum analysis: {e}")
    
    print()

def advanced_3_cross_wallet_analysis():
    """Advanced 3: Cross-wallet pattern analysis"""
    print("🔍 Advanced 3: Cross-Wallet Analysis")
    print("-" * 50)
    
    detective = SolanaDetective()
    
    # Example: Analyze multiple wallets for common patterns
    wallets = [
        "AB9RndvzedBPXqUrbYPZ8dMdLvfD9yozDdvg9Tkxg68X",
        # Add more wallet addresses as needed
    ]
    
    try:
        wallet_data = {}
        
        for wallet in wallets:
            print(f"Analyzing wallet: {wallet[:8]}...")
            
            try:
                # Get wallet holdings
                holdings = detective.get_wallet_tokens(wallet)
                
                if holdings and 'tokens' in holdings:
                    tokens = holdings['tokens']
                    wallet_data[wallet] = {
                        'total_value': holdings.get('total', 0),
                        'token_count': len(tokens),
                        'top_holdings': [t.get('address') for t in tokens[:5]]
                    }
            
            except Exception as e:
                print(f"   Error: {e}")
        
        # Find common holdings
        if len(wallet_data) > 1:
            print("\n🔗 Common Holdings Analysis:")
            all_holdings = []
            for data in wallet_data.values():
                all_holdings.extend(data['top_holdings'])
            
            # Count occurrences
            from collections import Counter
            common_tokens = Counter(all_holdings)
            
            print("Most common tokens across wallets:")
            for token_addr, count in common_tokens.most_common(3):
                if count > 1:
                    try:
                        token_info = detective.get_token_info(token_addr)
                        symbol = token_info.get('token', {}).get('symbol', 'Unknown')
                        print(f"   {symbol}: {count} wallets")
                    except:
                        print(f"   {token_addr[:8]}...: {count} wallets")
    
    except Exception as e:
        print(f"Error in cross-wallet analysis: {e}")
    
    print()

def advanced_4_trading_strategy_backtest():
    """Advanced 4: Trading strategy backtesting"""
    print("🎯 Advanced 4: Trading Strategy Backtest")
    print("-" * 50)
    
    detective = SolanaDetective()
    wallet_address = "AB9RndvzedBPXqUrbYPZ8dMdLvfD9yozDdvg9Tkxg68X"
    
    try:
        # Get wallet trades
        trades_data = detective.get_wallet_trades(wallet_address)
        
        if not trades_data or 'trades' not in trades_data:
            print("No trades found")
            return
        
        trades = trades_data['trades']
        print(f"Backtesting strategy on {len(trades)} trades...")
        
        # Simulate "take profit at 50%" strategy
        strategy_results = []
        
        for trade in trades[:10]:  # Analyze first 10 trades
            to_token_addr = trade.get('to', {}).get('address')
            if not to_token_addr:
                continue
            
            buy_price = trade.get('price', {}).get('usd', 0)
            buy_time = trade.get('time', 0)
            
            if not buy_price or not buy_time:
                continue
            
            try:
                # Get ATH data to see maximum potential
                ath_data = detective.get_token_ath(to_token_addr)
                
                if ath_data:
                    ath_price = ath_data.get('highest_price', 0)
                    ath_time = ath_data.get('timestamp', 0)
                    
                    if ath_price > buy_price and ath_time > buy_time:
                        # Calculate different exit strategies
                        target_50_percent = buy_price * 1.5
                        
                        if ath_price >= target_50_percent:
                            # Strategy would have worked
                            strategy_pnl = 50  # 50% profit
                            max_possible = ((ath_price - buy_price) / buy_price) * 100
                            
                            strategy_results.append({
                                'token': to_token_addr[:8],
                                'strategy_pnl': strategy_pnl,
                                'max_possible': max_possible,
                                'efficiency': strategy_pnl / max_possible if max_possible > 0 else 0
                            })
            
            except Exception as e:
                continue
        
        # Analyze strategy performance
        if strategy_results:
            print(f"\nStrategy Results ({len(strategy_results)} applicable trades):")
            avg_efficiency = sum(r['efficiency'] for r in strategy_results) / len(strategy_results)
            print(f"Average efficiency: {avg_efficiency:.1%}")
            
            print("\nTop performing trades:")
            for result in sorted(strategy_results, key=lambda x: x['max_possible'], reverse=True)[:3]:
                print(f"   {result['token']}...: {result['strategy_pnl']:.1f}% vs {result['max_possible']:.1f}% max")
    
    except Exception as e:
        print(f"Error in strategy backtest: {e}")
    
    print()

def advanced_5_market_timing_analysis():
    """Advanced 5: Market timing and entry analysis"""
    print("⏰ Advanced 5: Market Timing Analysis")
    print("-" * 50)
    
    detective = SolanaDetective()
    
    try:
        # Get trending tokens for timing analysis
        trending = detective.get_trending_tokens()
        
        if not trending:
            print("No trending data available")
            return
        
        print("Analyzing market timing patterns...")
        
        for token in trending[:2]:
            token_addr = token.get('mint', token.get('address'))
            if not token_addr:
                continue
            
            symbol = token.get('symbol', 'Unknown')
            print(f"\n⏱️  {symbol} Timing Analysis:")
            
            try:
                # Get token info with price events
                token_info = detective.get_token_info(token_addr)
                
                if token_info and 'events' in token_info:
                    events = token_info['events']
                    
                    # Analyze different timeframes
                    timeframes = ['1m', '5m', '15m', '30m', '1h', '24h']
                    
                    print("   Price momentum across timeframes:")
                    for tf in timeframes:
                        if tf in events:
                            change = events[tf].get('priceChangePercentage', 0)
                            direction = "📈" if change > 0 else "📉" if change < 0 else "➡️"
                            print(f"     {tf:>3}: {direction} {change:>6.2f}%")
                
                # Get ATH timing
                ath_data = detective.get_token_ath(token_addr)
                if ath_data and ath_data.get('timestamp'):
                    ath_timestamp = ath_data['timestamp'] / 1000
                    ath_date = datetime.fromtimestamp(ath_timestamp)
                    now = datetime.now()
                    time_since_ath = now - ath_date
                    
                    print(f"   Time since ATH: {time_since_ath.days} days ago")
            
            except Exception as e:
                print(f"   Error: {e}")
    
    except Exception as e:
        print(f"Error in timing analysis: {e}")
    
    print()

def main():
    """Run all advanced analysis examples"""
    print("🔍 Solana Detective - Advanced Analysis Examples")
    print("=" * 70)
    print()
    
    # Check if API key is configured
    try:
        detective = SolanaDetective()
        print("✅ API key configured, running advanced examples...\n")
    except Exception as e:
        print(f"❌ API key not configured: {e}")
        print("Please set SOLANA_TRACKER_API_KEY environment variable or update config.json")
        return
    
    examples = [
        advanced_1_wallet_pnl_analysis,
        advanced_2_token_momentum_analysis,
        advanced_3_cross_wallet_analysis,
        advanced_4_trading_strategy_backtest,
        advanced_5_market_timing_analysis
    ]
    
    for example_func in examples:
        try:
            example_func()
        except Exception as e:
            print(f"❌ Advanced example failed: {e}\n")
    
    print("=" * 70)
    print("✅ Advanced analysis examples completed!")
    print("These patterns demonstrate the power of combining multiple API endpoints")
    print("for sophisticated blockchain analysis using the script-free approach.")

if __name__ == "__main__":
    main()

