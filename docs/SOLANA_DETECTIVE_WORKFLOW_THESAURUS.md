# Solana Detective Workflow Thesaurus 📚

**A canonical library of verified, working analytical workflows**

## 🎯 Purpose

This document serves as a **living knowledge base** of proven analytical patterns and workflows. Each entry represents a **validated, reusable methodology** that any AI can execute using the `SolanaDetective` master script.

## 📋 Workflow Template

Each workflow entry follows this standardized format:

```
## [WORKFLOW_NAME]

**User Goal**: [What problem does this solve?]
**Status**: ✅ Validated | 🧪 Testing | 📝 Draft
**Last Updated**: [Date]

### Required Inputs:
- Input 1: [Description]
- Input 2: [Description]

### Output Data Points:
- Data Point 1: [Description]
- Data Point 2: [Description]

### Core Logic/Steps:
1. Step 1: [API call or calculation]
2. Step 2: [API call or calculation]
3. Step 3: [Processing logic]

### Endpoints Used:
- `detective.method_name(parameters)` - [Purpose]
- `detective.method_name(parameters)` - [Purpose]

### Key Calculations:
- Formula 1: [Mathematical expression]
- Formula 2: [Mathematical expression]

### Time Data Standards:
- [Specific time handling requirements]

### Example Use Case:
[Brief example of successful application]

### Notes:
[Any special considerations or edge cases]
```

---

## 🔄 WORKFLOW LIBRARY

### 1. WALLET_TRADE_JOURNAL_ANALYSIS

**User Goal**: Generate comprehensive trading journal with PNL analysis and strategy optimization insights  
**Status**: ✅ Validated  
**Last Updated**: June 30, 2025

#### Required Inputs:
- Wallet Address: [Solana wallet address to analyze]

#### Output Data Points:
- Token Traded: Ticker symbol
- Token Traded: Contract address  
- Buy: Amount in SOL
- Buy: Price of token (USD)
- Buy: Time of buy (Unix + EST)
- Sell: Amount in SOL
- Sell: Price of token (USD)  
- Sell: Time of sell (Unix + EST)
- ATH: Price at ATH (USD)
- ATH: Time at ATH (Unix + EST, smallest timeframe)
- PNL: Actual PNL of trade
- PNL: MAX PNL if didn't sell (held to ATH)

#### Core Logic/Steps:
1. **Retrieve Trade History**: Get all wallet transactions
2. **Identify Token Pairs**: Match buy/sell transactions for same tokens
3. **Extract Trade Data**: Parse amounts, prices, timestamps for each trade
4. **Get Token Information**: Fetch ticker and contract details
5. **Retrieve ATH Data**: Get all-time high price and timestamp
6. **Calculate Actual PNL**: (Sell Price × Amount Sold) - (Buy Price × Amount Bought)
7. **Calculate Max PNL**: (ATH Price - Buy Price) × Amount Bought
8. **Format Time Data**: Convert Unix timestamps to EST

#### Endpoints Used:
- `detective.get_wallet_trades(wallet_address)` - Retrieve all buy/sell transactions
- `detective.get_token_info(token_address)` - Get token ticker and contract details
- `detective.get_token_ath(token_address)` - Get ATH price and timestamp

#### Key Calculations:
- **Actual PNL**: `(sell_price * amount_sold) - (buy_price * amount_bought)`
- **Max Potential PNL**: `(ath_price - buy_price) * amount_bought`
- **PNL Efficiency**: `actual_pnl / max_potential_pnl * 100`

#### Time Data Standards:
- Store both Unix timestamp and EST conversion
- Use smallest available timeframe for ATH timing accuracy
- Format: `{"unix": 1234567890, "est": "2025-06-30 15:30:45 EST"}`

#### Example Use Case:
Analyzing a wallet's meme token trading strategy to optimize take-profit levels and timing decisions based on historical performance vs maximum potential gains.

#### Notes:
- Handle partial sells by tracking remaining position sizes
- Account for multiple buy/sell cycles for same token
- Consider gas fees in PNL calculations if required for precision

---

## 📝 Adding New Workflows

When a new analytical workflow is successfully validated:

1. **Document immediately** using the template above
2. **Test thoroughly** with real data
3. **Mark as validated** only after user confirmation
4. **Include edge cases** and special considerations
5. **Update this thesaurus** for future AI inheritance

## 🎯 Usage Guidelines

- **Always check this thesaurus first** before building new analysis logic
- **Follow validated workflows exactly** to ensure consistency
- **Extend existing workflows** rather than creating duplicates
- **Document any modifications** as new workflow variants
- **Validate with user** before marking workflows as ✅ Validated

---

*This thesaurus grows with each successful analytical pattern we develop and validate.*

