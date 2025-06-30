"""
Custom exceptions for Solana Detective package
"""

class SolanaDetectiveError(Exception):
    """Base exception for all Solana Detective errors"""
    pass

class APIError(SolanaDetectiveError):
    """Raised when API request fails"""
    def __init__(self, message: str, status_code: int = None, response: dict = None):
        super().__init__(message)
        self.status_code = status_code
        self.response = response

class AuthenticationError(SolanaDetectiveError):
    """Raised when API authentication fails"""
    pass

class RateLimitError(SolanaDetectiveError):
    """Raised when API rate limit is exceeded"""
    def __init__(self, message: str, retry_after: int = None):
        super().__init__(message)
        self.retry_after = retry_after

class ValidationError(SolanaDetectiveError):
    """Raised when input validation fails"""
    pass

class EndpointNotFoundError(SolanaDetectiveError):
    """Raised when requested endpoint is not implemented"""
    pass

