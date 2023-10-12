name = str(input("Enter Client name: "))
loan = float(input("Enter amount of loan: "))
days = int(input("Enter days taken with loan: "))
extraDays = days % 30
interest = loan * 0.1

if (extraDays != 0):
    fine = loan * 0.01 * extraDays
    total = loan + interest + fine
else:
    total = loan + interest

print(f"Total amount from Peter is : \t {total}")
