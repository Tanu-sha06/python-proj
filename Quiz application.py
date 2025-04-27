question=[
{
    "prompt":" 1. What is the correct file extension for Python files?",
    "options":["a.pyth","b.pt","c.py","d.pyt "],
    "Answer":"c"
},
{
    "prompt":"2.How do you create a variable in Python?",
    "options":[" a.let x = 5","b.x = 5","c.var x = 5","d.x := 5"],
    "Answer":"b"
},
{
    "prompt":"3.What will print(2 ** 3) output? ",
    "options":["a.6","b.8","c.9","d.5 "],
    "Answer":"b"
},
{
    "prompt":"4.What data type is the result of 5 / 2 in Python 3? ",
    "options":["a.Integer","b.String","c.Float","d.Boolean"],
    "Answer":"c"
},
{
    "prompt":"5.How do you create a list in Python?",
    "options":["a.{1,2,3}","b.[1,2,3]","c.(1,2,3)","d.list(1,2,3)"],
    "Answer":"b"
},
{
    "prompt":"6.How do you access the third element in a list named my_list?",
    "options":["a.my_list[2]","b.my_list(3)","c.my_list[3]","d.my_list{2}"],
    "Answer":"a"
},
{
    "prompt":"7.What keyword is used to define a function in Python?",
    "options":["a.define","b.function","c.def","d.func"],
    "Answer":"c"
},
{
    "prompt":"8.What is the output of the following code? \n for i in range(3): \n print(i)",
    "options":["a.0 1 2","b.1 2 3","c.0 1 2 3","d.1 2"],
    "Answer":"a"
},
{
    "prompt":"9.What does the return statement do in a function?",
    "options":["a.Exits the program","b.Exits the loop","c.Sends a value back to the caller","d.Prints a value"],
    "Answer":"c"
},
{
    "prompt":"10.What is a class in Python?",
    "options":["a.A blueprint for creating objects","b.A type of function","c.A loop structure","d.A data type"],
    "Answer":"a"
},
{
    "prompt":"11.How do you create an object from a class?",
    "options":["a.object className()","b.className = new object()","c.obj = className()","d.create className"],
    "Answer":"c"
},
{
    "prompt":"12.What is self used for in class methods?",
    "options":["a.Refers to the class itself","b.Refers to the current object","c.A random variable","d.It is optional"],
    "Answer":"b"
},
{
    "prompt":"13.What is the difference between a list and a tuple?",
    "options":["a.Tuples are mutable, lists are immutable","b.Lists are mutable, tuples are immutable","c.Both are mutable","d.Both are immutable"],
    "Answer":"b"
},
{
    "prompt":"14.What is exception handling?",
    "options":["a.Handling errors gracefully","b.Handling loops","c.Handling function calls","d.Handling class instances"],
    "Answer":"a"
},
{
    "prompt":"15.What is a decorator in Python?",
    "options":["a.A function that modifies another function","b.A function that decorates a list","c.A loop in Python","d.A variable that holds a function"],
    "Answer":"a"
}]
def run_quiz(Questions):
    score = 0
    for question in Questions:
        print(question["prompt"])
        for option in question["options"]:
            print(option)
        answer = input("Enter your option (a,b,c): ").lower()
        if answer == question["Answer"]:
            print("\n Correct answer\n")
            score += 1
        else:
            print("\n Wrong, the correct answer was: \n", question["Answer"])
    print(f"\n You got {score}/{len(Questions)} correct \n")
run_quiz(question)