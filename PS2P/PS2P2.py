last_name = input("Enter your last name: ")
midterm_score = float(input("Enter your midterm exam score: "))
final_score = float(input("Enter your final exam score: "))

total_points = (0.4 * midterm_score) + (0.6 * final_score)
print("Last Name:", last_name)
print("Total Exam Points:", total_points)