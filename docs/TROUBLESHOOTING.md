# Troubleshooting Guide 🔧

**Common issues and solutions for the Solana Detective toolkit**

## 🚨 Quick Diagnostics

### **Health Check**
```bash
python3 validation/health_check.py
```

### **Package Import Test**
```python
try:
    from solana_detective import SolanaDetective
    print("✅ Package imported successfully")
except ImportError as e:
    print(f"❌ Import error: {e}")
```

## 🔧 Installation Issues

### **Package Not Found**
```
ModuleNotFoundError: No module named 'solana_detective'
```

**Solutions:**
1. **Extract the package**:
   ```bash
   tar -xzf solana_detective_corrected_package.tar.gz
   ```

2. **Add to Python path**:
   ```bash
   export PYTHONPATH="${PYTHONPATH}:/path/to/solana-detective-toolkit"
   ```

3. **Install as package**:
   ```bash
   pip install -e .
   ```

### **Permission Denied**
```
PermissionError: [Errno 13] Permission denied
```

**Solutions:**
1. **Check file permissions**:
   ```bash
   ls -la solana_detective/
   chmod +r solana_detective/*.py
   ```

2. **Run with proper permissions**:
   ```bash
   sudo python3 script.py  # Use cautiously
   ```

### **Python Version Issues**
```
SyntaxError: invalid syntax
```

**Solutions:**
1. **Check Python version**:
   ```bash
   python3 --version  # Should be 3.7+
   ```

2. **Use correct Python**:
   ```bash
   python3.9 script.py  # Use specific version
   ```

## 🔑 API Key Issues

### **Missing API Key**
```
ValueError: API key is required
```

**Solutions:**
1. **Set environment variable**:
   ```bash
   export SOLANA_TRACKER_API_KEY="your_key_here"
   ```

2. **Check configuration**:
   ```bash
   echo $SOLANA_TRACKER_API_KEY
   ```

3. **Pass directly in code**:
   ```python
   detective = SolanaDetective(api_key="your_key_here")
   ```

### **Invalid API Key**
```
APIError: API request failed with status 401
```

**Solutions:**
1. **Verify API key format** (no extra spaces)
2. **Generate new API key** from dashboard
3. **Check API key permissions**
4. **Test with curl**:
   ```bash
   curl -H "x-api-key: YOUR_KEY" https://data.solanatracker.io/credits
   ```

## 🌐 Network Issues

### **Connection Timeout**
```
requests.exceptions.ConnectTimeout
```

**Solutions:**
1. **Check internet connectivity**:
   ```bash
   ping google.com
   ```

2. **Test API endpoint**:
   ```bash
   curl -I https://data.solanatracker.io
   ```

3. **Increase timeout**:
   ```python
   detective = SolanaDetective(timeout=60)
   ```

4. **Check firewall settings**

### **SSL Certificate Issues**
```
requests.exceptions.SSLError
```

**Solutions:**
1. **Update certificates**:
   ```bash
   pip install --upgrade certifi
   ```

2. **Disable SSL verification** (not recommended):
   ```python
   detective = SolanaDetective(verify_ssl=False)
   ```

### **DNS Resolution Issues**
```
requests.exceptions.ConnectionError: Failed to resolve
```

**Solutions:**
1. **Check DNS settings**:
   ```bash
   nslookup data.solanatracker.io
   ```

2. **Try different DNS**:
   ```bash
   # Use Google DNS
   echo "nameserver 8.8.8.8" >> /etc/resolv.conf
   ```

## 📊 API Response Issues

### **Rate Limit Exceeded**
```
APIError: API request failed with status 429
```

**Solutions:**
1. **Wait for reset** (usually 1 minute)
2. **Implement delays**:
   ```python
   detective = SolanaDetective(rate_limit_delay=1.0)
   ```
3. **Upgrade API plan**
4. **Check concurrent usage**

### **Invalid Response Format**
```
JSONDecodeError: Expecting value
```

**Solutions:**
1. **Check API status** at Solana Tracker
2. **Verify endpoint URL**
3. **Test with simple request**:
   ```python
   result = detective.get_credits()
   ```

### **Empty Response**
```
{'trades': [], 'nextCursor': None}
```

**Possible Causes:**
- **No data available** for the requested parameters
- **Incorrect wallet address** format
- **Time range** outside available data
- **Token not tracked** by the API

**Solutions:**
1. **Verify input parameters**
2. **Test with known good data**
3. **Check API documentation** for parameter requirements

## 🔍 Data Analysis Issues

### **Unexpected Data Types**
```
TypeError: unsupported operand type(s)
```

**Solutions:**
1. **Check data structure**:
   ```python
   print(type(result))
   print(result.keys() if isinstance(result, dict) else result)
   ```

2. **Handle missing fields**:
   ```python
   price = trade.get('price', {}).get('usd', 0)
   ```

3. **Validate data before processing**:
   ```python
   if 'trades' in result and result['trades']:
       # Process trades
   ```

### **Memory Issues with Large Datasets**
```
MemoryError
```

**Solutions:**
1. **Use pagination**:
   ```python
   trades = detective.get_wallet_trades(wallet, limit=100)
   ```

2. **Process in chunks**
3. **Increase system memory**
4. **Use generators** for large datasets

## 🕐 Timestamp Issues

### **Timezone Confusion**
**Problem**: Timestamps in different timezones

**Solutions:**
1. **Convert to consistent timezone**:
   ```python
   from datetime import datetime, timezone
   import pytz
   
   # Convert Unix timestamp to EST
   est = pytz.timezone('US/Eastern')
   dt = datetime.fromtimestamp(timestamp/1000, tz=est)
   ```

2. **Store both Unix and readable**:
   ```python
   time_data = {
       'unix': timestamp,
       'est': dt.strftime('%Y-%m-%d %H:%M:%S %Z')
   }
   ```

### **Invalid Timestamp Format**
```
ValueError: timestamp out of range
```

**Solutions:**
1. **Check timestamp scale** (seconds vs milliseconds)
2. **Validate timestamp range**:
   ```python
   if timestamp > 1000000000000:  # Milliseconds
       timestamp = timestamp / 1000
   ```

## 🔄 Workflow Issues

### **Incomplete Trade Pairs**
**Problem**: Buy without corresponding sell

**Solutions:**
1. **Check for partial positions**
2. **Handle open positions**:
   ```python
   if not sell_transactions:
       # Position still open
       current_value = current_price * amount_held
   ```

### **Duplicate Transactions**
**Problem**: Same transaction appearing multiple times

**Solutions:**
1. **Deduplicate by transaction hash**:
   ```python
   unique_trades = {trade['tx']: trade for trade in trades}.values()
   ```

2. **Filter by time range**
3. **Check for different pools** of same token

## 🆘 Emergency Procedures

### **Complete System Failure**
1. **Check all dependencies**:
   ```bash
   python3 -c "import requests; print('Requests OK')"
   ```

2. **Reinstall package**:
   ```bash
   rm -rf solana_detective/
   tar -xzf solana_detective_corrected_package.tar.gz
   ```

3. **Reset configuration**:
   ```bash
   cp config.json.backup config.json
   ```

### **Data Corruption**
1. **Validate API responses**
2. **Cross-check with blockchain explorer**
3. **Re-fetch data** from API
4. **Contact support** if persistent

## 📞 Getting Help

### **Self-Help Resources**
1. **Run diagnostics**: `python3 validation/health_check.py`
2. **Check logs** for error details
3. **Review API documentation**
4. **Test with minimal example**

### **Community Support**
1. **GitHub Issues** (if repository is public)
2. **Solana Tracker Support** for API issues
3. **Stack Overflow** for Python/technical issues

### **Reporting Bugs**
Include in your report:
- **Error message** (full traceback)
- **Python version** and OS
- **API key status** (valid/invalid, don't share the key)
- **Minimal code** to reproduce the issue
- **Expected vs actual** behavior

---

*Last updated: June 30, 2025*

