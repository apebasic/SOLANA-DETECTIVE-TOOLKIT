# API Key Management 🔑

**Complete guide for obtaining, configuring, and managing Solana Tracker API keys**

## 🎯 Overview

The Solana Detective toolkit requires a valid **Solana Tracker API key** to access blockchain data. This guide covers everything you need to know about API key management.

## 📝 Obtaining an API Key

### **Step 1: Visit Solana Tracker**
1. Go to [https://solanatracker.io/](https://solanatracker.io/)
2. Click on **"API"** or **"Get API Access"**
3. Sign up for an account if you don't have one

### **Step 2: Choose a Plan**
- **Free Tier**: Limited requests per month
- **Paid Tiers**: Higher rate limits and additional features
- **Enterprise**: Custom limits and support

### **Step 3: Generate API Key**
1. Navigate to your **Dashboard** or **API Keys** section
2. Click **"Generate New API Key"** or **"Create API Key"**
3. **Copy and save** the API key immediately (it may not be shown again)

## 🔧 Configuration Methods

### **Method 1: Environment Variable (Recommended)**

#### **Linux/macOS:**
```bash
# Temporary (current session only)
export SOLANA_TRACKER_API_KEY="your_api_key_here"

# Permanent (add to ~/.bashrc or ~/.zshrc)
echo 'export SOLANA_TRACKER_API_KEY="your_api_key_here"' >> ~/.bashrc
source ~/.bashrc
```

#### **Windows:**
```cmd
# Command Prompt
set SOLANA_TRACKER_API_KEY=your_api_key_here

# PowerShell
$env:SOLANA_TRACKER_API_KEY="your_api_key_here"

# Permanent (System Properties > Environment Variables)
```

### **Method 2: Configuration File**
```bash
# Edit config.json
{
  "api_key": "your_api_key_here",
  "base_url": "https://data.solanatracker.io",
  "timeout": 30
}
```

### **Method 3: Direct Code Initialization**
```python
from solana_detective import SolanaDetective

# Pass API key directly
detective = SolanaDetective(api_key="your_api_key_here")
```

## ✅ Verification

### **Test API Key Validity**
```python
from solana_detective import SolanaDetective

try:
    detective = SolanaDetective()  # Uses environment variable
    # Test with a simple call
    credits = detective.get_credits()
    print(f"✅ API Key valid. Credits remaining: {credits}")
except Exception as e:
    print(f"❌ API Key issue: {e}")
```

### **Run Health Check**
```bash
python3 validation/health_check.py
```

## 🔄 API Key Rotation

### **When to Rotate**
- **Security breach** or suspected compromise
- **Regular security practice** (every 90 days)
- **Team member changes** with API access
- **Switching between environments** (dev/prod)

### **Rotation Process**
1. **Generate new API key** in Solana Tracker dashboard
2. **Update configuration** using one of the methods above
3. **Test new key** with health check
4. **Revoke old key** in dashboard
5. **Update documentation** if key is shared

## 🚨 Troubleshooting

### **Common Error Messages**

#### **"API key is required"**
```
ValueError: API key is required. Provide via api_key parameter or SOLANA_TRACKER_API_KEY environment variable.
```
**Solution**: Set API key using one of the configuration methods above.

#### **"Invalid API key" (401 Unauthorized)**
```
APIError: API request failed with status 401: {'error': 'Invalid API key'}
```
**Solutions**:
- Verify API key is correct (no extra spaces/characters)
- Check if API key has expired
- Ensure API key has proper permissions
- Generate a new API key if needed

#### **"Rate limit exceeded" (429 Too Many Requests)**
```
APIError: API request failed with status 429: {'error': 'Rate limit exceeded'}
```
**Solutions**:
- Wait for rate limit reset (usually 1 minute)
- Upgrade to higher tier plan
- Implement request throttling in your code
- Check if multiple processes are using same key

#### **"Wrong API endpoint" (404 Not Found)**
```
APIError: API request failed with status 404: {'message': 'This is not the Data API endpoint. Please use https://data.solanatracker.io for the Data API.'}
```
**Solution**: Ensure base URL is set to `https://data.solanatracker.io`

### **Diagnostic Commands**

#### **Check Environment Variable**
```bash
echo $SOLANA_TRACKER_API_KEY
```

#### **Test API Connectivity**
```bash
curl -H "x-api-key: YOUR_API_KEY" https://data.solanatracker.io/credits
```

#### **Validate Configuration**
```python
from solana_detective.config import Config
config = Config()
print(f"API Key set: {'Yes' if config.api_key else 'No'}")
print(f"Base URL: {config.base_url}")
```

## 🔒 Security Best Practices

### **API Key Protection**
- **Never commit** API keys to version control
- **Use environment variables** instead of hardcoding
- **Restrict API key permissions** if possible
- **Monitor API key usage** regularly

### **Access Control**
- **Limit API key sharing** to necessary team members
- **Use separate keys** for different environments
- **Implement key rotation** schedule
- **Log API key usage** for audit trails

### **Environment Separation**
```bash
# Development
export SOLANA_TRACKER_API_KEY="dev_key_here"

# Production
export SOLANA_TRACKER_API_KEY="prod_key_here"
```

## 📊 Rate Limits & Usage

### **Understanding Rate Limits**
- **Requests per minute**: Varies by plan
- **Daily/Monthly limits**: Check your dashboard
- **Burst limits**: Short-term request spikes

### **Monitoring Usage**
```python
# Check remaining credits
detective = SolanaDetective()
credits = detective.get_credits()
print(f"Credits remaining: {credits}")
```

### **Optimizing Usage**
- **Cache responses** when appropriate
- **Batch requests** when possible
- **Use pagination** for large datasets
- **Implement exponential backoff** for retries

## 🆘 Emergency Procedures

### **Compromised API Key**
1. **Immediately revoke** the compromised key
2. **Generate new API key**
3. **Update all configurations**
4. **Review access logs** for suspicious activity
5. **Notify team members** if applicable

### **Service Outage**
1. **Check Solana Tracker status** page
2. **Verify network connectivity**
3. **Test with different endpoints**
4. **Contact support** if issue persists

---

*Last updated: June 30, 2025*

