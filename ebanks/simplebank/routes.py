from flask import Blueprint, request, jsonify
from .services.account_service import AccountService

# Create a Blueprint that help organize routes
api_bp = Blueprint('api', __name__)
svc = AccountService()

@api_bp.route('/reset', methods=['POST'])
def reset():
    """
    Resets the application state, clearing all accounts and balances
    
    Returns:
        A string 'OK' and HTTP status code 200 on success.
    """
    svc.reset()
    return 'OK', 200

@api_bp.route('/balance', methods=['GET'])
def balance():
    """
    Retrieves the balance of a specific account.
    
    Returns:
        The account balance as a string and HTTP status code 200 on success
        If the account is not found, the AccountService will raise a NotFoundError,
        which will be handled by the global error handler (defined in errors.py)
    """
    acc_id = request.args.get('account_id')
    bal    = svc.get_balance(acc_id)  
    return str(bal), 200

@api_bp.route('/event', methods=['POST'])
def event():
    """
    Processes the event, which can be a deposit, withdrawal or transfer

    Returns:
        A JSON object with the result of the operation and HTTP status code 201 on success
        If the request is malformed or the event type is invalid, a BadRequestError
        will be raised and handled by the global error handler
        If an account involved in the operation is not found, a NotFoundError will be raised
    """
    payload = request.get_json(force=True)
    result = svc.handle_event(payload)
    return jsonify(result), 201
