print("Enter marks recieved in 5 subjects")
markOne = int(input("Enter marks for subject 1: "))
markTwo = int(input("Enter marks for subject 2: "))
markThree = int(input("Enter marks for subject 3: "))
markFour = int(input("Enter the marks for subject 4:"))
markFive = int(input("Enter the marks for subject 5:"))
tot = markOne + markTwo + markThree + markFour + markFive
avg = int(tot / 5)
if avg not in range(0, 101):
    print("Invalid marks entered")
elif avg in range(91, 101):
    print("Nice Job, you passed, you become genius lah, A+")
elif avg in range(81, 91):
    print("Good job, here's a A, such a average")
elif avg in range(71, 81):
    print("Not bad, you passed, you become average lah, stoopid, B+")
elif avg in range(61, 71):
    print("You passed, you become average lah, stoopid, C-")
elif avg in range(51, 61):
    print("You passed, you become average lah, stoopid, D-")
elif avg in range(0, 51):
    print("You failed, you gonna work in Starbucks, stoopid, F-")