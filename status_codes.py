class Status:
    OK = 200  # Everything worked as expected
    CREATED = 201  # A resource was successfully created in response to a POST request. The Location header contains the URL pointing to the newly created resource
    NO_CONTENT = 204  # The request was handled successfully and the response contains no body content (like a DELETE request)
    NOT_MODIFIED = 304  # The resource was not modified. You can use the cached version
    BAD_REQUEST = 400  # Bad request. This could be caused by various actions by the user, such as providing invalid JSON data in the request body, providing invalid action parameters, etc
    UNAUTHORIZED = 401  # Authentication failed
    FORBIDDEN = 403  # The authenticated user is not allowed to access the specified API endpoint
    NOT_FOUND = 404  # The requested resource does not exist
    METHOD_NOT_ALLOWED = 405  # Method not allowed. Please check the Allow header for the allowed HTTP methods
    UNSUPPORTED_MEDIA_TYPE = 415  # Unsupported media type. The requested content type or version number is invalid
    UNPROCESSABLE_ENTITY = 422  # Data validation failed (in response to a POST request, for example). Please check the response body for detailed error messages.
    TOO_MANY_REQUESTS = 429  # Too many requests. The request was rejected due to rate limiting
    INTERNAL_SERVER_ERROR = 500  # Internal server error. This could be caused by internal program errors
