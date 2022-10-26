from users import Person

# Create a new Person entry in the database
Person_1 = Person('Mutulu', 10, 12345)

# Deposit PayCheck
Person_1.add_pay_check(1000)
# Deposit PayCheck
Person_1.add_pay_check(75)

# Add Expense
Person_1.add_expense(200)
# Add Expense
Person_1.add_expense(23)

# Request Balance
Person_1.get_balance()

# Request All User Data
Person_1.print_all_info()

# Request Usage Percentage
Person_1.get_use_percentage()
