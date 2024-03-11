loop_control = input("Do you want to continue (Yes/No)? ")
if loop_control == "Yes":
    count = 0
    sum_gross_pay = 0

    while loop_control == "Yes":
        last_name = input("Enter employee last name: ")
        hours_worked = float(input("Enter hours worked: "))
        rate_of_pay = float(input("Enter rate of pay: "))
        
        if hours_worked > 40:
            gross_pay = (40 * rate_of_pay) + ((hours_worked - 40) * rate_of_pay * 1.5)
        else:
            gross_pay = hours_worked * rate_of_pay

        sum_gross_pay += gross_pay
        count += 1

        print(f"Employee {last_name} gross pay is {gross_pay}")

        loop_control = input("Do you want to continue entering employee data (Yes/No)? ")

    print(f"Total gross pay of all employees: {sum_gross_pay}")
    print(f"Total  number of employees: {count}")
    
    if count != 0:
        avg_pay = sum_gross_pay / count
        print(f"Average pay: {avg_pay}")
