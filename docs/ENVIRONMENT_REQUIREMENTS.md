# Environment Requirements 🔧

**System requirements for running the Solana Detective toolkit**

## 🐍 Python Requirements

### **Minimum Version**
- **Python 3.7+** (Recommended: Python 3.9 or higher)
- **pip 20.0+** for package installation

### **Required Python Packages**
```
requests>=2.25.0
```

Install via:
```bash
pip install -r requirements.txt
```

## 💻 Operating System Compatibility

### **✅ Fully Supported**
- **Linux** (Ubuntu 18.04+, CentOS 7+, Debian 9+)
- **macOS** (10.14+)
- **Windows** (Windows 10+)

### **📋 System Dependencies**
- **Internet connectivity** (required for API calls)
- **Shell access** (for package extraction and setup)
- **File system write permissions** (for configuration and logs)

## 🔧 Installation Verification

### **1. Python Version Check**
```bash
python3 --version
# Should output: Python 3.7.x or higher
```

### **2. Package Installation Test**
```bash
# Extract the package
tar -xzf solana_detective_corrected_package.tar.gz

# Test import
python3 -c "from solana_detective import SolanaDetective; print('✅ Package imported successfully')"
```

### **3. Basic Functionality Test**
```bash
# Run the health check
python3 validation/health_check.py
```

## 🌐 Network Requirements

### **Required Endpoints**
- **Primary API**: `https://data.solanatracker.io`
- **Fallback API**: `https://api.solanatracker.io`

### **Firewall Configuration**
- **Outbound HTTPS (443)** must be allowed
- **No inbound connections** required

## 🔑 API Key Requirements

### **Solana Tracker API Key**
- **Required**: Valid API key from [Solana Tracker](https://solanatracker.io/)
- **Rate Limits**: Varies by subscription tier
- **Setup**: See `API_KEY_MANAGEMENT.md`

## ⚠️ Known Compatibility Issues

### **Python 2.x**
- **Not supported** - Python 3.7+ required

### **Very Old Systems**
- **CentOS 6 and older**: May require manual Python 3.7+ installation
- **Ubuntu 16.04 and older**: May require Python version upgrade

### **Restricted Environments**
- **Corporate firewalls**: May block API endpoints
- **Air-gapped systems**: Will not work (requires internet)

## 🔍 Troubleshooting Environment Issues

### **Import Errors**
```bash
# Check Python path
python3 -c "import sys; print(sys.path)"

# Add current directory to path
export PYTHONPATH="${PYTHONPATH}:/path/to/solana-detective-toolkit"
```

### **Permission Errors**
```bash
# Check file permissions
ls -la solana_detective/

# Fix permissions if needed
chmod +x validation/health_check.py
```

### **Network Connectivity**
```bash
# Test API endpoint connectivity
curl -I https://data.solanatracker.io

# Test with API key
curl -H "x-api-key: YOUR_API_KEY" https://data.solanatracker.io/tokens/trending
```

## 📊 Performance Considerations

### **Memory Usage**
- **Minimum**: 512MB RAM
- **Recommended**: 1GB+ RAM for large data analysis

### **Storage**
- **Package size**: ~1MB
- **Log files**: Variable (can be disabled)
- **Cache**: Minimal (API responses not cached by default)

## 🔄 Version Compatibility Matrix

| Python Version | Status | Notes |
|---------------|--------|-------|
| 3.7.x | ✅ Supported | Minimum version |
| 3.8.x | ✅ Supported | Recommended |
| 3.9.x | ✅ Supported | Recommended |
| 3.10.x | ✅ Supported | Tested |
| 3.11.x | ✅ Supported | Tested |
| 3.12.x | 🧪 Testing | Should work |

---

*Last updated: June 30, 2025*

