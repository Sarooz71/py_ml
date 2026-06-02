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
