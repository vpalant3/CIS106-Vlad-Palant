students_data = [
    ["Smith", "I", 4],
    ["Johnson", "O", 3],
    ["Williams", "I", 5]
]

in_district_cost = 250.00
out_district_cost = 500.00

total_tuition = 0
total_students = 0

for student_info in students_data:
    last_name, district_code, credits_taken = student_info
    if district_code == "I":
        cost_per_credit = in_district_cost
    else:
        cost_per_credit = out_district_cost
    
    tuition_owed = credits_taken * cost_per_credit
    total_tuition += tuition_owed
    total_students += 1
    print(f"Student: {last_name}, Credits Taken: {credits_taken}, Tuition Owed: {tuition_owed}")

print(f"Total Tuition: {total_tuition}, Total Students: {total_students}")