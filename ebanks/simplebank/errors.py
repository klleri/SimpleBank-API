from flask import jsonify

class NotFoundError(Exception):
    """Custom exception to indicate that a requested resource was not found
    """
    pass

class BadRequestError(Exception): 
    """Custom exception to indicate that the client's request is invalid
    """
    pass

def register_error_handlers(app):
    """
   Registers custom error handlers for the Flask application.
   When a NotFoundError or BadRequestError is raised anywhere in the application
   and not caught locally, these handlers will be invoked to generate a
   standardized HTTP response.

   Args:
       app (Flask): The Flask application instance.
   """
    @app.errorhandler(NotFoundError)
    def handle_not_found(e):
        """
        Handles NotFoundError exceptions.
        Returns a '0' as the response body and an HTTP status code 404 (Not Found)   
        """
        return '0', 404

    @app.errorhandler(BadRequestError)
    def handle_bad_request(e):
        """
        Handles BadRequestError exceptions
        Returns a '0' as the response body and an HTTP status code 400 (Bad Request)
        """
        return '0', 400
