from Usecase.AccountCreationUseCase import AccountCreationUseCase
from Usecase.TransactionUseCase import TransactionUseCase
from Usecase.AccountStatementUseCase import AccountStatementUseCase
from Infrastructure.AccountRepository import AccountRepository

# Initialize the AccountRepository
account_repo = AccountRepository()

# Initialize Use Cases
account_creation_use_case = AccountCreationUseCase()
transaction_use_case = TransactionUseCase(account_repo)
statement_use_case = AccountStatementUseCase(account_repo)

# Step 1: Create a new customer and account
customer_id = "cust123"
customer_name = "John Doe"
customer_email = "john.doe@example.com"
customer_phone = "123-456-7890"

new_account = account_creation_use_case.create_account(customer_id, customer_name, customer_email, customer_phone)
account_repo.save_account(new_account)

print(f"New account created with ID: {new_account.account_id} for customer {customer_name}")

# Step 2: Make some transactions
transaction_use_case.make_transaction(new_account.account_id, 1000, 'deposit')  # Deposit
transaction_use_case.make_transaction(new_account.account_id, 200, 'withdraw')  # Withdraw

# Step 3: Generate an account statement
account_statement = statement_use_case.generate_account_statement(new_account.account_id)
print("\nAccount Statement:")
print(account_statement)

# Optional: Creating another account for the same customer and repeating steps
second_account = account_creation_use_case.create_account(customer_id, customer_name, customer_email, customer_phone)
account_repo.save_account(second_account)
transaction_use_case.make_transaction(second_account.account_id, 500, 'deposit')  # Deposit to second account

# Generate statement for the second account
second_account_statement = statement_use_case.generate_account_statement(second_account.account_id)
print("\nSecond Account Statement:")
print(second_account_statement)

# Retrieve all accounts for the customer
customer_accounts = account_repo.find_accounts_by_customer_id(customer_id)
print(f"\nCustomer {customer_name} has {len(customer_accounts)} accounts.")
