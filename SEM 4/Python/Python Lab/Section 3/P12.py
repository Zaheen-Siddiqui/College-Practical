def calculate_net_salary(employee_type, monthly_salary, hourly_rate, absent_days, incentives, income_tax):
    if employee_type == "permanent":
        daily_salary = monthly_salary / 30
        deduction = daily_salary * absent_days
        gross_salary = monthly_salary + incentives
    else:
        working_days = 30 - absent_days
        gross_salary = (hourly_rate * 8 * working_days) + incentives
        deduction = 0
    return gross_salary - income_tax - deduction

def get_input(prompt, cast_type, condition=lambda x: True, error="Invalid input."):
    while True:
        try:
            value = cast_type(input(prompt).strip())
            if condition(value):
                return value
            else:
                print(error)
        except ValueError:
            print(error)

etype = get_input("Enter Employee Type (Permanent/Temporary): ", str,
                  lambda x: x.lower() in ["permanent", "temporary"],
                  "Please enter 'Permanent' or 'Temporary'.").lower()

msalary = get_input("Enter Monthly Salary: ₹", float, lambda x: x >= 0)
hrate = get_input("Enter Hourly Rate: ₹", float, lambda x: x >= 0)
absent = get_input("Enter number of absent days: ", int, lambda x: 0 <= x <= 30)
bonus = get_input("Enter Incentives/Bonus: ₹", float, lambda x: x >= 0)
tax = get_input("Enter Income Tax: ₹", float, lambda x: x >= 0)

net = calculate_net_salary(etype, msalary, hrate, absent, bonus, tax)
print(f"\nNet Salary = ₹{net:.2f}")
