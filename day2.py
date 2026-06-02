# Tuples are similar to lists but are immutable (cannot be changed after creation)

# Tuples cannot be changed after creation
student_record = ("Alice", 20, 85.5, "Computer Science")
print("Student Record Tuple:", student_record)

# Accessing tuple elements
print("Name:", student_record[0])
print("Age:", student_record[1])

# Tuple unpacking
name, age, score, department = student_record
print("\nUnpacked:", name, "is", age, "years old, scored", score, "in", department)

# When to use tuples?
# - Fixed data that shouldn't change
# - Dictionary keys (lists can't be keys)
# - Returning multiple values from a function


print("\n--- Sets ---")
print("="*50)
# Sets are unordered collections of unique items (no duplicates allowed)
# Sets automatically remove duplicates
course_A = {"Alice", "Bob", "Charlie", "Diana"}
course_B = {"Charlie", "Diana", "Eve", "Frank"}

print("Course A students:", course_A)
print("Course B students:", course_B)

# Set operations (great for finding overlaps)
print("\nStudents in both courses:", course_A & course_B)
print("Students in eith`er course:", course_A | course_B)
print("Only in Course A:", course_A - course_B)
print("Only in one course:", course_A ^ course_B)

# Remove duplicates from list using set
scores_with_duplicates = [85, 92, 85, 78, 92, 95, 85]
unique_scores = list(set(scores_with_duplicates))
print("\nOriginal scores:", scores_with_duplicates)
print("Unique scores:", unique_scores)

print("\n--- Dictionaries ---")
print("="*50)
# Dictionaries store key-value pairs and are very useful for structured data
# Dictionaries store data with keys
student = {
    "name": "Alice",
    "age": 20,
    "scores": [85, 92, 78],
    "department": "Computer Science",
    "is_active": True
}

print("Student Dictionary:")
print(student)

# Accessing values
print("\nStudent name:", student['name'])
print("Student scores:", student['scores'])
print("Average score:", sum(student['scores'])/len(student['scores']))

# Adding/updating values
student["grade"] = "A"
student["age"] = 21
print("\nAfter update:", student)

alis_score = student['scores']

alice_passing_scores = [score for score in alis_score if score >= 80]
print("\nAlice Passing scores (>=80):", alice_passing_scores)

# Looping through dictionaries
print("\nDictionary items:")
for key, value in student.items():
    print(" ", key, ":", value)

# Dictionary comprehension
# scores_dict = {}
# for i in range(1, 6):
#     scores_dict["Student_" + str(i)] = np.random.randint(60, 100)
# print("\nGenerated scores:", scores_dict)

# Conditional statements
# Function to determine grade based on score
def get_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

# Test the function
test_scores = [95, 85, 75, 65, 55]
for score in test_scores:
    grade = get_grade(score)
    print("Score:", score, "→ Grade:", grade)

# Multiple conditions
def check_eligibility(score, attendance):
    if score >= 60 and attendance >= 75:
        return "Eligible for exam"
    elif score >= 60 and attendance < 75:
        return "Low attendance - Not eligible"
    elif score < 60 and attendance >= 75:
        return "Low score - Need improvement"
    else:
        return "Not eligible - Both score and attendance low"

print("\nEligibility Check:")
print("Score 85, Attendance 80%:", check_eligibility(85, 80))
print("Score 85, Attendance 70%:", check_eligibility(85, 70))
print("Score 55, Attendance 80%:", check_eligibility(55, 80))