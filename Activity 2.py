nGrade = float(input("Enter your numeric grade: "))# Ask user for numeric grade input


if nGrade >= 90:
    lGrade = "A+"
elif nGrade >= 80:
    lGrade = "A"
elif nGrade >= 70:
    lGrade = "B"
elif nGrade >= 60:
    lGrade = "C"
elif nGrade >= 50:
    lGrade = "D"
else:
    lGrade = "F" # Converting numeric grade into corresponding letter grade


print(f"Your letter grade is {lGrade}.")# Output the letter grade
