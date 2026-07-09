questions = [
    ["Who developed Python?", "James Gosling", "Guido van Rossum", "Dennis Ritchie", "Bjarne Stroustrup", 2],
    ["Which symbol is used for comments in Python?", "//", "/*", "#", "&", 3],
    ["What is the output of print(2 + 3 * 4)?", "20", "14", "24", "10", 2],
    ["Which data type is mutable?", "tuple", "string", "list", "int", 3],
    ["What keyword is used to define a function?", "func", "define", "def", "function", 3],
    ["Which function is used to get user input?", "scan()", "input()", "get()", "read()", 2],
    ["What is the result of len('Python')?", "5", "6", "7", "8", 2],
    ["Which operator is used for exponentiation?", "^", "**", "//", "%", 2],
    ["Which collection stores key-value pairs?", "list", "tuple", "dictionary", "set", 3],
    ["What is the output of print(type(10))?", "<class 'int'>", "<class 'float'>", "<class 'str'>", "<class 'list'>", 1],
    ["Which keyword is used for conditional statements?", "loop", "if", "case", "switch", 2],
    ["What is the output of print(10 // 3)?", "3.33", "3", "4", "1", 2],
    ["Which method adds an item to a list?", "insert()", "append()", "add()", "push()", 2],
    ["What is the output of bool(0)?", "True", "False", "None", "Error", 2],
    ["Which loop is used when the number of iterations is unknown?", "for", "while", "do-while", "repeat", 2]
]
prizes=[1000,2000,3000,4000,5000,6000,7000,8000,9000,10000,11000,12000,13000,14000,15000]
score=0
i=0
print('''
🎮 PYTHON QUIZ RULES 🎮

1. Total Questions: 15
2. Each question has 4 options.
3. Enter only 1, 2, 3, or 4.
4. Correct Answer  ➜ +₹1000 prize increase.
5. Wrong Answer    ➜ -₹1000 prize deduction.
6. Score more than 7 to pass.
7. Final score and prize will be shown at the end.

🍀 Best of Luck!
''')
for qno, question in enumerate(questions, start=1):
    print(f"Question {qno}. {question[0]}")
    print(f"1).{question[1]}")
    print(f"2).{question[2]}")
    print(f"3).{question[3]}")
    print(f"4).{question[4]}")

    a=int(input("Enter your ans(select any 1 option): "))

    if question[5]==a:
        print("hey your ans is correct\n🎉")
        print("You won ",prizes[i])
        score+=1
        i+=1
    else:
        print("😑 your ans is wrong\n❌")
        print("You loss 1000")
        i-=1
        if i < 0:
            i = 0
        

if score>7:
    print("🎊🎊🎊\nCONGRATULATIONS! you pass this quiz")
else:
    print("you fail this quiz try again")
print(f"Your final score is {score}")
