# Questions
questions = [
    "1. What is the difference between @staticmethod and @classmethod?",
    "2. Use of *args and **kwargs?",
    "3. What is a generator?",
    "4. How is memory managed in Python?",
    "5. What is the difference between deepcopy and shallow copy?",
    "6. Difference between 'is' and '=='?",
    "7. What is a lambda function?",
    "8. Use of 'with' statement?",
    "9. What are decorators?",
    "10. Mutable vs Immutable types?",
    "11. Use of __init__ method?",
    "12. What does @property do?",
    "13. How Python handles multiple inheritance?",
    "14. Built-in data structure?",
    "15. copy vs deepcopy?",
    "16. Which creates a tuple?",
    "17. Use of 'pass'?",
    "18. Use of 'break'?",
    "19. Keyword for error handling?",
    "20. Function to take user input?"
]

# Options
options = [
    ["a) staticmethod no self, classmethod has cls", "b) same", "c) staticmethod uses self", "d) classmethod outside"],
    ["a) many values", "b) args and kwargs", "c) for comments", "d) only lambda"],
    ["a) code writer", "b) returns list", "c) uses yield", "d) uses return"],
    ["a) user", "b) garbage collector", "c) not managed", "d) pointers"],
    ["a) copy refs", "b) deepcopy all", "c) same", "d) shallow better"],
    ["a) is - value", "b) is - identity", "c) same", "d) == faster"],
    ["a) multi-line", "b) one-line", "c) module", "d) loop"],
    ["a) loops", "b) error handle", "c) resource clean", "d) print"],
    ["a) modifies functions", "b) errors", "c) comment", "d) loop"],
    ["a) mutable can't change", "b) immutable can change", "c) tuple, str = imm", "d) all mutable"],
    ["a) destructor", "b) constructor", "c) loop", "d) module"],
    ["a) call method", "b) method to variable", "c) debug", "d) loop"],
    ["a) depth", "b) left-right", "c) MRO", "d) not support"],
    ["a) queue", "b) stack", "c) set", "d) tree"],
    ["a) same", "b) copy is deep", "c) copy shallow", "d) deep fast"],
    ["a) (1,2)", "b) [1,2]", "c) {1,2}", "d) tuple[]"],
    ["a) exit", "b) skip", "c) do nothing", "d) start"],
    ["a) exit", "b) skip", "c) restart", "d) end"],
    ["a) except", "b) error", "c) catch", "d) fault"],
    ["a) scanf", "b) cin", "c) input", "d) gets"]
]

# Correct options
answers = ['a', 'b', 'c', 'b', 'b', 'b', 'b', 'c', 'a', 'c', 'b', 'b', 'c', 'c', 'c', 'a', 'c', 'a', 'a', 'c']

# Quiz
def quiz_game():
    score = 0
    print("Welcome to the Python Interview Quiz\n")

    for i in range(len(questions)):
        print(questions[i])
        for opt in options[i]:
            print(opt)
        ans = input("Your answer (a/b/c/d): ").strip().lower()

        if ans == answers[i]:
            print("Correct!\n")
            score += 1
        else:
            print("Wrong! Correct answer is:", answers[i], "\n")

    print("Final Score:", score, "/", len(questions))
    if score >= 15:
        print("Excellent! You’re ready.")
    elif score >= 10:
        print("Good work, revise more.")
    else:
        print("Keep learning, you’ll improve.")

# Run it
quiz_game()