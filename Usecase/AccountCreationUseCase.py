from Domain.Account import Account
from Domain.Customer import Customer
import uuid

class AccountCreationUseCase:
    def create_account(self, customer_id, name, email, phone_number):
        # Generate a unique account ID and account number
        account_id = str(uuid.uuid4())
        account_number = str(uuid.uuid4()).replace('-', '')[:10]  # Example of a 10-digit account number

        # Create Customer and Account instances
        customer = Customer(customer_id, name, email, phone_number)
        new_account = Account(account_id, customer.customer_id, account_number)

        # Additional logic for storing the customer and account information can be added here

        return new_account
