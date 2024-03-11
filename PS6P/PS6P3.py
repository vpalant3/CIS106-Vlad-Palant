user_response = input("Do you want to continue (Yes/No)?: ")
if user_response == "Yes":
    count_students = 0
    while True:
        last_name = input("Enter your last name: ")
        score1 = float(input("Enter your first exam score: "))
        score2 = float(input("Enter your second exam score: "))
        avg_score = (score1 + score2) / 2
        print(f"{last_name} - Average Exam Score: {avg_score}")
        count_students += 1
        if input("Do you want to enter data for another student (Yes/No)?: ") != "Yes":
            break
    print(f"Number of students entered: {count_students}")