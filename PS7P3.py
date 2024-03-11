def calculate_bonus(employee_data):
    bonuses_sum = 0
    for employee in employee_data:
        last_name, salary = employee.split(",")
        salary = float(salary)
        if salary >= 100000.00:
            bonus_rate = 0.20
        elif salary == 50000.00:
            bonus_rate = 0.15
        else:
            bonus_rate = 0.10

        bonus = salary * bonus_rate
        print(f"Employee: {last_name}, Salary: {salary}, Bonus: {bonus}")
        bonuses_sum += bonus

    print(f"Total bonuses paid out: {bonuses_sum}")

employee_data = [
    "Doe,100000.00",
    "Smith,50000.00",
    "Johnson,75000.00",
    "Brown,120000.00"
]

calculate_bonus(employee_data)