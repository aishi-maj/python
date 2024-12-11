# Define the dictionary of students and their scores
students_scores = {
    'Alice': 85,
    'Bob': 92,
    'Charlie': 88,
    'David': 75
}

# Find the student with the highest score
top_student = max(students_scores, key=students_scores.get)

# Print the result
print("Student with the highest score:", top_student)
print("Highest score:", students_scores[top_student])
