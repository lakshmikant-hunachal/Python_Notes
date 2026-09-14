#create project using all python basics concepts:
#project name: calculate the percentage of marks obtained by a student in different subjects and display the result along with the grade.
name=input("Enter student name:")
num_subjects=int(input("Enter number of subjects:"))
marks=[]
for i in range(num_subjects):
    mark=int(input(f"Enter marks for subject {i+1}:"))
    marks.append(mark)
total_marks=sum(marks)
percentage = (total_marks / (num_subjects * 100)) * 100
print(f"Student: {name}")
print(f"Total Marks: {total_marks}")
print(f"Percentage: {percentage:.2f}%")
if percentage >= 90:
    grade = 'A'
elif percentage >= 80:
    grade = 'B'
elif percentage >= 70:
    grade = 'C'
elif percentage >= 60:
    grade = 'D'
else:
    grade = 'F'
print(f"Grade: {grade}")

if(percentage >= 90):
    print("Excellent performance!")
elif(percentage >= 80):
    print("Very good performance!")
elif(percentage >= 70):
    print("Good performance!")
elif(percentage >= 60):
    print("Average performance!")
else:
    print("Needs improvement!")

print("Thank you for using the student marks calculator!")
print("Have a great day!")
print("please provide your feedback on the project.")
print("Your feedback is valuable to us and will help us improve our project.")
print("developed by: lakshmikant")
