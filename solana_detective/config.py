"""
Configuration management for Solana Detective package
"""

import os
import json
from typing import Dict, Any, Optional

class Config:
    """Configuration manager for Solana Detective"""
    
    # Default configuration
    DEFAULT_CONFIG = {
        "base_url": "https://api.solanatracker.io",
        "timeout": 30,
        "max_retries": 3,
        "retry_delay": 1,
        "rate_limit_delay": 0.1,
        "user_agent": "SolanaDetective/1.0.0",
        "verify_ssl": True
    }
    
    def __init__(self, api_key: str = None, config_file: str = None, **kwargs):
        """
        Initialize configuration
        
        Args:
            api_key: Solana Tracker API key
            config_file: Path to JSON configuration file
            **kwargs: Additional configuration options
        """
        self.config = self.DEFAULT_CONFIG.copy()
        
        # Load from config file if provided
        if config_file and os.path.exists(config_file):
            with open(config_file, 'r') as f:
                file_config = json.load(f)
                self.config.update(file_config)
        
        # Load from environment variables
        self.config.update({
            "api_key": api_key or os.getenv("SOLANA_TRACKER_API_KEY"),
            "base_url": os.getenv("SOLANA_TRACKER_BASE_URL", self.config["base_url"]),
            "timeout": int(os.getenv("SOLANA_TRACKER_TIMEOUT", self.config["timeout"])),
            "max_retries": int(os.getenv("SOLANA_TRACKER_MAX_RETRIES", self.config["max_retries"]))
        })
        
        # Override with provided kwargs
        self.config.update(kwargs)
        
        # Validate required configuration
        if not self.config.get("api_key"):
            raise ValueError("API key is required. Provide via api_key parameter or SOLANA_TRACKER_API_KEY environment variable.")
    
    def get(self, key: str, default: Any = None) -> Any:
        """Get configuration value"""
        return self.config.get(key, default)
    
    def set(self, key: str, value: Any) -> None:
        """Set configuration value"""
        self.config[key] = value
    
    def to_dict(self) -> Dict[str, Any]:
        """Return configuration as dictionary"""
        return self.config.copy()
    
    def save(self, file_path: str) -> None:
        """Save configuration to file"""
        with open(file_path, 'w') as f:
            json.dump(self.config, f, indent=2)
    
    @classmethod
    def from_file(cls, file_path: str, api_key: str = None) -> 'Config':
        """Create configuration from file"""
        return cls(api_key=api_key, config_file=file_path)

