"""
Core API client for Solana Detective package
Implements all 47 Solana Tracker API endpoints
"""

import json
import time
import logging
from typing import Dict, Any, List, Optional, Union
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

from .config import Config
from .exceptions import (
    APIError, 
    AuthenticationError, 
    RateLimitError, 
    ValidationError,
    EndpointNotFoundError
)

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class SolanaDetective:
    """
    Comprehensive Solana blockchain analysis client
    
    Provides access to all 47 Solana Tracker API endpoints with:
    - Built-in error handling and retries
    - Rate limiting protection
    - Response validation
    - Comprehensive logging
    """
    
    def __init__(self, api_key: str = None, config: Config = None, **kwargs):
        """
        Initialize Solana Detective client
        
        Args:
            api_key: Solana Tracker API key
            config: Configuration object
            **kwargs: Additional configuration options
        """
        if config:
            self.config = config
        else:
            self.config = Config(api_key=api_key, **kwargs)
        
        # Set up HTTP session with retries
        self.session = requests.Session()
        
        retry_strategy = Retry(
            total=self.config.get("max_retries"),
            backoff_factor=1,
            status_forcelist=[429, 500, 502, 503, 504],
        )
        
        adapter = HTTPAdapter(max_retries=retry_strategy)
        self.session.mount("http://", adapter)
        self.session.mount("https://", adapter)
        
        # Set default headers
        self.session.headers.update({
            "x-api-key": self.config.get("api_key"),
            "User-Agent": self.config.get("user_agent"),
            "Content-Type": "application/json"
        })
        
        logger.info(f"SolanaDetective client initialized with base URL: {self.config.get('base_url')}")
    
    def _make_request(self, 
                     method: str, 
                     endpoint: str, 
                     params: Dict[str, Any] = None,
                     data: Dict[str, Any] = None,
                     timeout: int = None) -> Dict[str, Any]:
        """
        Make HTTP request to Solana Tracker API
        
        Args:
            method: HTTP method (GET, POST)
            endpoint: API endpoint path
            params: Query parameters
            data: Request body data
            timeout: Request timeout
            
        Returns:
            API response as dictionary
            
        Raises:
            APIError: When API request fails
            AuthenticationError: When authentication fails
            RateLimitError: When rate limit is exceeded
        """
        url = f"{self.config.get('base_url')}{endpoint}"
        timeout = timeout or self.config.get("timeout")
        
        # Add rate limiting delay
        time.sleep(self.config.get("rate_limit_delay"))
        
        try:
            logger.debug(f"Making {method} request to {url}")
            
            response = self.session.request(
                method=method,
                url=url,
                params=params,
                json=data,
                timeout=timeout,
                verify=self.config.get("verify_ssl")
            )
            
            # Handle different response status codes
            if response.status_code == 200:
                return response.json()
            elif response.status_code == 401:
                raise AuthenticationError("Invalid API key")
            elif response.status_code == 429:
                retry_after = int(response.headers.get("Retry-After", 60))
                raise RateLimitError(f"Rate limit exceeded. Retry after {retry_after} seconds", retry_after)
            else:
                try:
                    error_data = response.json()
                except:
                    error_data = {"error": response.text}
                
                raise APIError(
                    f"API request failed with status {response.status_code}: {error_data}",
                    status_code=response.status_code,
                    response=error_data
                )
                
        except requests.exceptions.Timeout:
            raise APIError(f"Request timeout after {timeout} seconds")
        except requests.exceptions.ConnectionError:
            raise APIError("Connection error - unable to reach API")
        except requests.exceptions.RequestException as e:
            raise APIError(f"Request failed: {str(e)}")
    
    def _validate_token_address(self, token: str) -> str:
        """Validate token address format"""
        if not token or not isinstance(token, str):
            raise ValidationError("Token address must be a non-empty string")
        if len(token) < 32 or len(token) > 44:
            raise ValidationError("Invalid token address format")
        return token
    
    def _validate_wallet_address(self, wallet: str) -> str:
        """Validate wallet address format"""
        if not wallet or not isinstance(wallet, str):
            raise ValidationError("Wallet address must be a non-empty string")
        if len(wallet) < 32 or len(wallet) > 44:
            raise ValidationError("Invalid wallet address format")
        return wallet
    
    # ========================================
    # TOKEN ENDPOINTS (13 endpoints)
    # ========================================
    
    def get_token_info(self, token: str) -> Dict[str, Any]:
        """
        Get comprehensive token information
        
        Args:
            token: Token address
            
        Returns:
            Token information including pools, events, and risk data
        """
        token = self._validate_token_address(token)
        return self._make_request("GET", f"/tokens/{token}")
    
    def get_tokens_by_pool(self, pool_address: str) -> Dict[str, Any]:
        """
        Get tokens by pool address
        
        Args:
            pool_address: Pool address
            
        Returns:
            Token information for the specified pool
        """
        if not pool_address:
            raise ValidationError("Pool address is required")
        return self._make_request("GET", f"/tokens/by-pool/{pool_address}")
    
    def get_token_holders(self, token: str, page: int = 1, limit: int = 250) -> Dict[str, Any]:
        """
        Get token holders with pagination
        
        Args:
            token: Token address
            page: Page number (default: 1)
            limit: Items per page (default: 250, max: 500)
            
        Returns:
            List of token holders with balances and percentages
        """
        token = self._validate_token_address(token)
        params = {"page": page, "limit": min(limit, 500)}
        return self._make_request("GET", f"/tokens/{token}/holders", params=params)
    
    def get_token_holders_top(self, token: str) -> Dict[str, Any]:
        """
        Get top 20 token holders
        
        Args:
            token: Token address
            
        Returns:
            List of top 20 holders with balances and percentages
        """
        token = self._validate_token_address(token)
        return self._make_request("GET", f"/tokens/{token}/holders/top")
    
    def get_token_ath(self, token: str) -> Dict[str, Any]:
        """
        Get token all-time high information
        
        Args:
            token: Token address
            
        Returns:
            All-time high price data and timestamps
        """
        token = self._validate_token_address(token)
        return self._make_request("GET", f"/tokens/{token}/ath")
    
    def get_deployer_tokens(self, wallet: str, page: int = 1, limit: int = 250) -> Dict[str, Any]:
        """
        Get tokens deployed by a wallet
        
        Args:
            wallet: Deployer wallet address
            page: Page number (default: 1)
            limit: Items per page (default: 250, max: 500)
            
        Returns:
            List of tokens deployed by the wallet
        """
        wallet = self._validate_wallet_address(wallet)
        params = {"page": page, "limit": min(limit, 500)}
        return self._make_request("GET", f"/deployer/{wallet}", params=params)
    
    def search_tokens(self, query: str, limit: int = 10) -> Dict[str, Any]:
        """
        Search for tokens by name or symbol
        
        Args:
            query: Search query
            limit: Number of results to return
            
        Returns:
            List of matching tokens
        """
        if not query:
            raise ValidationError("Search query is required")
        params = {"query": query, "limit": limit}
        return self._make_request("GET", "/search", params=params)
    
    def get_latest_tokens(self, page: int = 1, limit: int = 250) -> Dict[str, Any]:
        """
        Get latest tokens
        
        Args:
            page: Page number (default: 1)
            limit: Items per page (default: 250, max: 500)
            
        Returns:
            List of latest tokens
        """
        params = {"page": page, "limit": min(limit, 500)}
        return self._make_request("GET", "/tokens/latest", params=params)
    
    def get_tokens_multi(self, tokens: List[str]) -> Dict[str, Any]:
        """
        Get information for multiple tokens (GET method)
        
        Args:
            tokens: List of token addresses
            
        Returns:
            Information for all requested tokens
        """
        if not tokens or not isinstance(tokens, list):
            raise ValidationError("Tokens must be a non-empty list")
        params = {"tokens": ",".join(tokens)}
        return self._make_request("GET", "/tokens/multi", params=params)
    
    def post_tokens_multi(self, tokens: List[str]) -> Dict[str, Any]:
        """
        Get information for multiple tokens (POST method)
        
        Args:
            tokens: List of token addresses
            
        Returns:
            Information for all requested tokens
        """
        if not tokens or not isinstance(tokens, list):
            raise ValidationError("Tokens must be a non-empty list")
        data = {"tokens": tokens}
        return self._make_request("POST", "/tokens/multi", data=data)
    
    def get_trending_tokens(self, timeframe: str = None) -> Dict[str, Any]:
        """
        Get trending tokens
        
        Args:
            timeframe: Optional timeframe filter
            
        Returns:
            List of trending tokens
        """
        if timeframe:
            return self._make_request("GET", f"/tokens/trending/{timeframe}")
        else:
            return self._make_request("GET", "/tokens/trending")
    
    def get_tokens_by_volume(self, timeframe: str = None) -> Dict[str, Any]:
        """
        Get tokens sorted by volume
        
        Args:
            timeframe: Optional timeframe filter
            
        Returns:
            List of tokens sorted by volume
        """
        if timeframe:
            return self._make_request("GET", f"/tokens/volume/{timeframe}")
        else:
            return self._make_request("GET", "/tokens/volume")
    
    def get_tokens_multi_all(self) -> Dict[str, Any]:
        """
        Get all tokens (multi endpoint)
        
        Returns:
            Information for all tokens
        """
        return self._make_request("GET", "/tokens/multi/all")
    
    def get_tokens_multi_graduated(self) -> Dict[str, Any]:
        """
        Get graduated tokens only
        
        Returns:
            Information for graduated tokens
        """
        return self._make_request("GET", "/tokens/multi/graduated")
    
    # ========================================
    # PRICE ENDPOINTS (6 endpoints)
    # ========================================
    
    def get_token_price(self, token: str, price_changes: bool = False) -> Dict[str, Any]:
        """
        Get current token price
        
        Args:
            token: Token address
            price_changes: Include price change percentages
            
        Returns:
            Current price and optional price changes
        """
        token = self._validate_token_address(token)
        params = {"token": token}
        if price_changes:
            params["priceChanges"] = "true"
        return self._make_request("GET", "/price", params=params)
    
    def get_price_history(self, token: str, time_from: int, time_to: int) -> Dict[str, Any]:
        """
        Get historical price data
        
        Args:
            token: Token address
            time_from: Start time (unix timestamp)
            time_to: End time (unix timestamp)
            
        Returns:
            Historical price data
        """
        token = self._validate_token_address(token)
        params = {
            "token": token,
            "time_from": time_from,
            "time_to": time_to
        }
        return self._make_request("GET", "/price/history", params=params)
    
    def get_price_at_timestamp(self, token: str, timestamp: int) -> Dict[str, Any]:
        """
        Get price at specific timestamp
        
        Args:
            token: Token address
            timestamp: Unix timestamp
            
        Returns:
            Price at the specified timestamp
        """
        token = self._validate_token_address(token)
        params = {
            "token": token,
            "timestamp": timestamp
        }
        return self._make_request("GET", "/price/history/timestamp", params=params)
    
    def get_price_range(self, token: str, time_from: int, time_to: int) -> Dict[str, Any]:
        """
        Get lowest and highest price in time range
        
        Args:
            token: Token address
            time_from: Start time (unix timestamp)
            time_to: End time (unix timestamp)
            
        Returns:
            Lowest and highest prices in the range
        """
        token = self._validate_token_address(token)
        params = {
            "token": token,
            "time_from": time_from,
            "time_to": time_to
        }
        return self._make_request("GET", "/price/history/range", params=params)
    
    def post_token_price(self, price_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Post token price data
        
        Args:
            price_data: Price data to post
            
        Returns:
            Response from price posting
        """
        return self._make_request("POST", "/price", data=price_data)
    
    def get_multiple_token_prices(self, tokens: List[str] = None) -> Dict[str, Any]:
        """
        Get prices for multiple tokens (GET method)
        
        Args:
            tokens: List of token addresses (optional)
            
        Returns:
            Prices for multiple tokens
        """
        params = {}
        if tokens:
            params["tokens"] = ",".join(tokens)
        return self._make_request("GET", "/price/multi", params=params)
    
    def post_multiple_token_prices(self, tokens: List[str]) -> Dict[str, Any]:
        """
        Get prices for multiple tokens (POST method)
        
        Args:
            tokens: List of token addresses
            
        Returns:
            Prices for multiple tokens
        """
        if not tokens or not isinstance(tokens, list):
            raise ValidationError("Tokens must be a non-empty list")
        data = {"tokens": tokens}
        return self._make_request("POST", "/price/multi", data=data)
    
    # ========================================
    # WALLET ENDPOINTS (8 endpoints)
    # ========================================
    
    def get_wallet_tokens(self, owner: str) -> Dict[str, Any]:
        """
        Get wallet token holdings
        
        Args:
            owner: Wallet address
            
        Returns:
            List of tokens held by the wallet
        """
        owner = self._validate_wallet_address(owner)
        return self._make_request("GET", f"/wallet/{owner}")
    
    def get_wallet_basic(self, owner: str) -> Dict[str, Any]:
        """
        Get basic wallet information
        
        Args:
            owner: Wallet address
            
        Returns:
            Basic wallet information
        """
        owner = self._validate_wallet_address(owner)
        return self._make_request("GET", f"/wallet/{owner}/basic")
    
    def get_wallet_page(self, owner: str, page: int) -> Dict[str, Any]:
        """
        Get wallet tokens with pagination
        
        Args:
            owner: Wallet address
            page: Page number
            
        Returns:
            Paginated wallet token holdings
        """
        owner = self._validate_wallet_address(owner)
        return self._make_request("GET", f"/wallet/{owner}/page/{page}")
    
    def get_wallet_trades(self, owner: str, page: int = 1, limit: int = 100) -> Dict[str, Any]:
        """
        Get wallet trading history
        
        Args:
            owner: Wallet address
            page: Page number for pagination
            limit: Number of trades per page
            
        Returns:
            Wallet trading history
        """
        owner = self._validate_wallet_address(owner)
        params = {"page": page, "limit": limit}
        return self._make_request("GET", f"/wallet/{owner}/trades", params=params)
    
    def get_wallet_chart(self, owner: str) -> Dict[str, Any]:
        """
        Get wallet performance chart data
        
        Args:
            owner: Wallet address
            
        Returns:
            Wallet performance chart data
        """
        owner = self._validate_wallet_address(owner)
        return self._make_request("GET", f"/wallet/{owner}/chart")
    
    # ========================================
    # TRADE ENDPOINTS (3 endpoints)
    # ========================================
    
    def get_pool_trades(self, token_address: str, pool_address: str, page: int = 1, limit: int = 100) -> Dict[str, Any]:
        """
        Get trades for a specific token/pool combination
        
        Args:
            token_address: Token address
            pool_address: Pool address
            page: Page number for pagination
            limit: Number of trades per page
            
        Returns:
            List of trades for the token/pool
        """
        token_address = self._validate_token_address(token_address)
        params = {"page": page, "limit": limit}
        return self._make_request("GET", f"/trades/{token_address}/{pool_address}", params=params)
    
    def get_wallet_token_trades(self, token_address: str, pool_address: str, owner: str) -> Dict[str, Any]:
        """
        Get trades for a specific wallet on a token/pool
        
        Args:
            token_address: Token address
            pool_address: Pool address
            owner: Wallet address
            
        Returns:
            Trades by the wallet on the token/pool
        """
        token_address = self._validate_token_address(token_address)
        owner = self._validate_wallet_address(owner)
        return self._make_request("GET", f"/trades/{token_address}/{pool_address}/{owner}")
    
    def get_token_wallet_trades(self, token_address: str, owner: str) -> Dict[str, Any]:
        """
        Get all trades by a wallet for a specific token
        
        Args:
            token_address: Token address
            owner: Wallet address
            
        Returns:
            All trades by the wallet for the token
        """
        token_address = self._validate_token_address(token_address)
        owner = self._validate_wallet_address(owner)
        return self._make_request("GET", f"/trades/{token_address}/by-wallet/{owner}")
    
    # ========================================
    # CHART DATA ENDPOINTS (2 endpoints)
    # ========================================
    
    def get_chart_data(self, 
                      token: str, 
                      pool: str = None,
                      interval: str = "1h",
                      time_from: int = None,
                      time_to: int = None,
                      market_cap: bool = False,
                      remove_outliers: bool = True) -> Dict[str, Any]:
        """
        Get OHLCV chart data for a token or token/pool
        
        Args:
            token: Token address
            pool: Pool address (optional)
            interval: Time interval (1s, 5s, 15s, 1m, 3m, 5m, 15m, 30m, 1h, 2h, 4h, 6h, 8h, 12h, 1d, 3d, 1w, 1mn)
            time_from: Start time (Unix timestamp)
            time_to: End time (Unix timestamp)
            market_cap: Return market cap data instead of pricing
            remove_outliers: Remove outliers from data
            
        Returns:
            OHLCV chart data
        """
        token = self._validate_token_address(token)
        
        params = {
            "type": interval,
            "marketCap": str(market_cap).lower(),
            "removeOutliers": str(remove_outliers).lower()
        }
        
        if time_from:
            params["time_from"] = time_from
        if time_to:
            params["time_to"] = time_to
        
        if pool:
            return self._make_request("GET", f"/chart/{token}/{pool}", params=params)
        else:
            return self._make_request("GET", f"/chart/{token}", params=params)
    
    def get_holders_chart(self, token: str) -> Dict[str, Any]:
        """
        Get holders chart data for a token
        
        Args:
            token: Token address
            
        Returns:
            Holders chart data over time
        """
        token = self._validate_token_address(token)
        return self._make_request("GET", f"/holders/chart/{token}")
    
    def get_token_holders_chart(self, token: str) -> Dict[str, Any]:
        """
        Get token holders chart data (alternative endpoint)
        
        Args:
            token: Token address
            
        Returns:
            Token holders chart data over time
        """
        token = self._validate_token_address(token)
        return self._make_request("GET", f"/chart/holders/{token}")
    
    # ========================================
    # PNL DATA ENDPOINTS (3 endpoints)
    # ========================================
    
    def get_wallet_pnl(self, wallet: str) -> Dict[str, Any]:
        """
        Get profit/loss data for a wallet
        
        Args:
            wallet: Wallet address
            
        Returns:
            Wallet PnL data across all tokens
        """
        wallet = self._validate_wallet_address(wallet)
        return self._make_request("GET", f"/pnl/{wallet}")
    
    def get_first_buyers(self, token: str, limit: int = 100) -> Dict[str, Any]:
        """
        Get first buyers of a token
        
        Args:
            token: Token address
            limit: Number of first buyers to return
            
        Returns:
            List of first buyers with their purchase data
        """
        token = self._validate_token_address(token)
        params = {"limit": limit}
        return self._make_request("GET", f"/first-buyers/{token}", params=params)
    
    def get_wallet_token_pnl(self, wallet: str, token: str) -> Dict[str, Any]:
        """
        Get profit/loss data for a wallet on a specific token
        
        Args:
            wallet: Wallet address
            token: Token address
            
        Returns:
            Wallet PnL data for the specific token
        """
        wallet = self._validate_wallet_address(wallet)
        token = self._validate_token_address(token)
        return self._make_request("GET", f"/pnl/{wallet}/{token}")
    
    # ========================================
    # TOP TRADERS ENDPOINTS (3 endpoints)
    # ========================================
    
    def get_top_traders_all(self, page: int = None) -> Dict[str, Any]:
        """
        Get top traders across all tokens
        
        Args:
            page: Page number for pagination (optional)
            
        Returns:
            List of top traders across all tokens
        """
        if page:
            return self._make_request("GET", f"/top-traders/all/{page}")
        else:
            return self._make_request("GET", "/top-traders/all")
    
    def get_top_traders_token(self, token: str) -> Dict[str, Any]:
        """
        Get top traders for a specific token
        
        Args:
            token: Token address
            
        Returns:
            List of top traders for the token
        """
        token = self._validate_token_address(token)
        return self._make_request("GET", f"/top-traders/{token}")
    
    # ========================================
    # STATS AND EVENTS ENDPOINTS (4 endpoints)
    # ========================================
    
    def get_token_stats(self, token: str, pool: str = None) -> Dict[str, Any]:
        """
        Get statistics for a token or token/pool
        
        Args:
            token: Token address
            pool: Pool address (optional)
            
        Returns:
            Token or token/pool statistics
        """
        token = self._validate_token_address(token)
        
        if pool:
            return self._make_request("GET", f"/stats/{token}/{pool}")
        else:
            return self._make_request("GET", f"/stats/{token}")
    
    def get_live_events(self) -> Dict[str, Any]:
        """
        Get live events across all tokens
        
        Returns:
            Live events data
        """
        return self._make_request("GET", "/live-events")
    
    def get_token_events(self, token_address: str) -> Dict[str, Any]:
        """
        Get events for a specific token
        
        Args:
            token_address: Token address
            
        Returns:
            Token events data
        """
        token_address = self._validate_token_address(token_address)
        return self._make_request("GET", f"/events/{token_address}")
    
    def get_pool_events(self, token_address: str, pool_address: str) -> Dict[str, Any]:
        """
        Get events for a specific token/pool combination
        
        Args:
            token_address: Token address
            pool_address: Pool address
            
        Returns:
            Pool events data
        """
        token_address = self._validate_token_address(token_address)
        return self._make_request("GET", f"/events/{token_address}/{pool_address}")
    
    # ========================================
    # CREDITS ENDPOINT (1 endpoint)
    # ========================================
    
    def get_credits(self) -> Dict[str, Any]:
        """
        Get API credits information
        
        Returns:
            Current API credits and usage information
        """
        return self._make_request("GET", "/credits")
    
    # ========================================
    # UTILITY METHODS
    # ========================================
    
    def get_available_endpoints(self) -> List[str]:
        """
        Get list of all available endpoint methods
        
        Returns:
            List of all available endpoint method names
        """
        endpoints = []
        for attr_name in dir(self):
            if (not attr_name.startswith('_') and 
                callable(getattr(self, attr_name)) and
                attr_name not in ['get_available_endpoints']):
                endpoints.append(attr_name)
        return sorted(endpoints)
    
    def health_check(self) -> Dict[str, Any]:
        """
        Perform health check by testing credits endpoint
        
        Returns:
            Health check results
        """
        try:
            credits = self.get_credits()
            return {
                "status": "healthy",
                "api_accessible": True,
                "credits_remaining": credits.get("credits", "unknown"),
                "timestamp": time.time()
            }
        except Exception as e:
            return {
                "status": "unhealthy", 
                "api_accessible": False,
                "error": str(e),
                "timestamp": time.time()
            }

