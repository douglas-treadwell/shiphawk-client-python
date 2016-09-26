class ShiphawkError(Exception):
    """Base for Shiphawk related errors"""
    def __init__(self, response):
        Exception.__init__(self)
        self.response = response


class GeneralError(ShiphawkError):
    """Raised when an HTTP status code 400 is received."""
    pass


class UnauthorizedError(ShiphawkError):
    """Raised when an HTTP status code 401 is received."""
    pass


class AccessDeniedError(ShiphawkError):
    """Raised when an HTTP status code 403 is received."""
    pass


class NotFoundError(ShiphawkError):
    """Raised when an HTTP status code 404 is received."""
    pass


class UnprocessableEntityError(ShiphawkError):
    """Raised when an HTTP status code 422 is received."""
    pass


class InformShiphawkError(ShiphawkError):
    """Raised when an HTTP status code 500 is received."""
    pass


class UnavailableError(ShiphawkError):
    """Raised when an HTTP status code 502 or 503 is received."""
    pass


error_map = {
    400: GeneralError,
    401: UnauthorizedError,
    403: AccessDeniedError,
    404: NotFoundError,
    422: UnprocessableEntityError,
    500: InformShiphawkError,
    502: UnavailableError,
    503: UnavailableError
}


def raise_if_error(response):
    if (response.status_code // 100) != 2:
        raise (error_map.get(response.status_code, ShiphawkError)(response))
