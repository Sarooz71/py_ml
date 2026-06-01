# tuple 
# name , age , score, department = student_record
# print("\")

#sets automatically remove duplicates

course_A = {"Saroj","Bishesh","Govinda"}
course_B = {"Dinita","Dipson","Sanana"}

print("Course A student: ", course_A)
print("Course B student: ", course_B)

#set operations (great for finding overlaps)

print("\n Students in both courses", course_A & course_B)
print("Student in either course: ", course_A | course_B)
print("Only in Coures A ", course_A - course_B)
print("Only in one Coures", course_A ^ course_B)

# Remove duplicates from list using set

scores_with_duplicates = [85,92,85,78,92,95,85]
unique_scores = list(set(scores_with_duplicates))
print("\n Original scores:", scores_wth_duplicates)
print("Unique_scores", uni)
