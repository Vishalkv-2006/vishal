dsa = int(input("Enter marks in DSA (out of 100): "))
french = int(input("Enter marks in French (out of 100): "))
maths2 = int(input("Enter marks in Maths2 (out of 100): "))
discreetmaths = int(input("Enter marks in Discreet Maths (out of 100): "))
aiml = int(input("Enter marks in AIML (out of 100): "))


subjects = [dsa, french, maths2, discreetmaths, aiml]
if any(m < 0 or m > 100 for m in subjects):
    print("Error: Marks should be between 0 and 100.")
else:
    
    total = sum(subjects)
    percentage = total / len(subjects)

    
    if percentage >= 90:
        grade = "A+"
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 50:
        grade = "D"
    else:
        grade = "F"

    
    print("\n----- Student Report -----")
    print(f"DSA: {dsa}")
    print(f"French: {french}")
    print(f"Maths2: {maths2}")
    print(f"Discreet Maths: {discreetmaths}")
    print(f"AIML: {aiml}")
    print(f"Total Marks: {total} / 500")
    print(f"Percentage: {percentage:.2f}%")
    print(f"Grade: {grade}")
