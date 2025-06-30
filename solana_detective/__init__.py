"""
Solana Detective - Comprehensive Solana Blockchain Analysis Toolkit
==================================================================

A complete Python package for interacting with the Solana Tracker API.
Provides access to all 47 documented endpoints with built-in error handling,
rate limiting, and comprehensive documentation.

Usage:
    from solana_detective import SolanaDetective
    
    detective = SolanaDetective(api_key="your_api_key_here")
    
    # Get token price
    price = detective.get_token_price(token="token_address")
    
    # Get wallet trades  
    trades = detective.get_wallet_trades(wallet="wallet_address")
    
    # Get token holders
    holders = detective.get_token_holders_top(token="token_address")

Features:
    - All 47 Solana Tracker API endpoints
    - Built-in rate limiting and error handling
    - Comprehensive response validation
    - Cross-AI compatibility design
    - Production-ready code quality

Author: AI-Generated Package
Version: 1.0.0
License: MIT
"""

__version__ = "1.0.0"
__author__ = "AI-Generated Package"
__license__ = "MIT"

from .client import SolanaDetective
from .exceptions import (
    SolanaDetectiveError,
    APIError,
    AuthenticationError,
    RateLimitError,
    ValidationError
)

__all__ = [
    "SolanaDetective",
    "SolanaDetectiveError", 
    "APIError",
    "AuthenticationError",
    "RateLimitError",
    "ValidationError"
]

