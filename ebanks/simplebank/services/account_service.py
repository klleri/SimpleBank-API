from ..errors import NotFoundError, BadRequestError

class AccountService:
    """
    Manages account balances and handles financial events like deposits,
    withdrawals, and transfers

    """
    
    
    def __init__(self):
        self._accounts = {}

    def reset(self):
        self._accounts.clear()

    def get_balance(self, account_id):
        """
        Retrieves the balance for a given account ID
        
        Args:
            account_id (str): ID of the account
        Returns:
            int: The balance of the account
        Raises:
            NotFoundError: If the account_id does not exist
        """
        if account_id not in self._accounts:
            raise NotFoundError()
        return self._accounts[account_id]

    def handle_event(self, e):
        """
        Processes a financial event based on its type
        
        Args:
            e (dict): A dictionary representing the event
        Returns:
            dict: The result of the processed event
        Raises:
            BadRequestError: If the event type is unknown or not provided
        """
        t = e.get('type')
        if t == 'deposit':
            return self._deposit(e)
        if t == 'withdraw':
            return self._withdraw(e)
        if t == 'transfer':
            return self._transfer(e)
        raise BadRequestError()

    def _deposit(self, e):
        """
        Handles a deposit eventk, increases the balance of the destination account
        If the destination account does not exist, it is created
        
        Args:
            e (dict): The event data, must contain 'destination' (str) and 'amount' (int)
        Returns:
            dict: A dictionary confirming the deposit, including the destination account ID and new balance
        """
        dest, amt = e['destination'], e['amount']
        bal = self._accounts.get(dest, 0) + amt
        self._accounts[dest] = bal
        return {'destination': {'id': dest, 'balance': bal}}

    def _withdraw(self, e):
        """
        Handles a withdrawal event, decreases the balance of the origin account
        
        Args:
            e (dict): The event data, must contain 'origin' (str) and 'amount' (int)
        Returns:
            dict: A dictionary confirming the withdrawal, including the origin account ID and new balance
        Raises:
            NotFoundError: If the origin account does not exist
        Note:
            This method currently does NOT check for sufficient funds before withdrawing
            It can result in a negative balance if amount > current balance
        """
        orig, amt = e['origin'], e['amount']
        if orig not in self._accounts:
            raise NotFoundError()
        self._accounts[orig] -= amt
        return {'origin': {'id': orig, 'balance': self._accounts[orig]}}

    def _transfer(self, e):
        """
       Handles a transfer event, decreases the balance of the origin account
       and increases the balance of the destination account
       If the destination account does not exist, it is created
       
       Args:
           e (dict): The event data, must contain 'origin' (str), 'destination' (str), and 'amount' (int).
       Returns:
           dict: A dictionary confirming the transfer, including the origin and destination
                 account IDs and their new balances.
                 Example: {'origin': {'id': '100', 'balance': 0}, 'destination': {'id': '200', 'balance': 15}}
       Raises:
           NotFoundError: If the origin account does not exist.
       Note:
           This method currently does NOT check for sufficient funds in the origin account
           before transferring. It can result in a negative balance for the origin account.
       """
        orig, dest, amt = e['origin'], e['destination'], e['amount']
        if orig not in self._accounts:
            raise NotFoundError()
        self._accounts[orig] -= amt
        self._accounts[dest] = self._accounts.get(dest, 0) + amt
        return {
            'origin': {'id': orig, 'balance': self._accounts[orig]},
            'destination': {'id': dest, 'balance': self._accounts[dest]}
        }
