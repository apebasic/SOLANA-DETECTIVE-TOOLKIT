# Quick Start for AI Users 🤖

**Fast setup guide for AI systems using the Solana Detective toolkit**

## 🚀 One-Minute Setup

### Step 1: Get the Code
```bash
# Clone the repository
git clone https://github.com/apebasic/SOLANA-DETECTIVE-TOOLKIT.git
cd SOLANA-DETECTIVE-TOOLKIT/
```

### Step 2: Set API Key
```bash
# Set environment variable (replace with actual key)
export SOLANA_TRACKER_API_KEY="your_api_key_here"
```

### Step 3: Verify Setup
```bash
# Run health check
python3 validation/health_check.py
```

### Step 4: Start Using
```python
from solana_detective import SolanaDetective

# Initialize and use
detective = SolanaDetective()
result = detective.get_token_info("So11111111111111111111111111111111111111112")
print(f"SOL Token: {result['token']['name']}")
```

## 📚 Essential Documentation

- **[AI Handoff Guide](docs/AI_HANDOFF_GUIDE.md)** - Complete AI inheritance guide
- **[Workflow Thesaurus](docs/SOLANA_DETECTIVE_WORKFLOW_THESAURUS.md)** - Validated analysis patterns
- **[API Documentation](docs/QUALITY_CHECKED_SOLANA_TRACKER_API_DOCS.md)** - All 47 endpoints
- **[Troubleshooting](docs/TROUBLESHOOTING.md)** - Common issues and solutions

## 🎯 Script-Free Philosophy

This toolkit follows a **script-free approach**:
- ✅ Use the `SolanaDetective` package for all API calls
- ✅ Process data and calculations in your reasoning
- ❌ Don't write additional scripts for analysis
- ✅ Follow validated workflows from the thesaurus

## 🔍 Common Use Cases

### Wallet Analysis
```python
# Get wallet trading history
trades = detective.get_wallet_trades("wallet_address")
# Process trades data to calculate PnL, patterns, etc.
```

### Token Research
```python
# Get token information and ATH
token_info = detective.get_token_info("token_address")
ath_data = detective.get_token_ath("token_address")
# Analyze price performance, holder distribution, etc.
```

### Market Analysis
```python
# Get trending tokens
trending = detective.get_trending_tokens()
# Analyze momentum, volume patterns, etc.
```

## ⚡ Quick Commands

```bash
# Health check
python3 validation/health_check.py

# API coverage validation
python3 validation/cross_check_validation.py

# Package quality check
python3 validation/quality_control_validator.py

# Basic usage examples
python3 examples/basic_usage.py

# Advanced analysis examples
python3 examples/advanced_analysis.py
```

## 🆘 Need Help?

1. **Check health**: `python3 validation/health_check.py`
2. **Review troubleshooting**: `docs/TROUBLESHOOTING.md`
3. **Validate API access**: `python3 validation/cross_check_validation.py`
4. **Follow validated patterns**: `docs/SOLANA_DETECTIVE_WORKFLOW_THESAURUS.md`

---

*For complete documentation, see the [AI Handoff Guide](docs/AI_HANDOFF_GUIDE.md)*

