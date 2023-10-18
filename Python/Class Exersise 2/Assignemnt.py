"""
Create Loan Class
    Inut()
    name
    amount
    no. of days 

    main()
    Loan calculator
"""
class Loan:
    def __init__(self, client_name, loan_amount, days_taken):
        self.client_name = client_name
        self.loan_amount = loan_amount
        self.days_taken = days_taken

    def calculate_total_amount(self):
        interest = self.loan_amount * 0.1
        extra_days = self.days_taken % 30

        if extra_days != 0:
            fine = self.loan_amount * 0.01 * extra_days
            total = self.loan_amount + interest + fine
        else:
            total = self.loan_amount + interest

        return total

# Get user input
name = str(input("Enter Client name: "))
loan_amount = float(input("Enter amount of loan: "))
days_taken = int(input("Enter days taken with loan: "))

# Create a Loan instance
loan = Loan(name, loan_amount, days_taken)

# Calculate and display the total amount
total_amount = loan.calculate_total_amount()
print(f"Total amount from {loan.client_name} is: {total_amount}")
