import myProg

def menu():
    print("\n------ FUNCTION MENU ------")
    print("1. Replace Substring")
    print("2. Check Vowel/Consonant")
    print("3. Length of String")
    print("4. Diamond Pattern")
    print("5. Pyramid Pattern")
    print("6. Floyd's Triangle")
    print("7. Quadratic Equation Roots")
    print("8. Number of Digits (Recursive)")
    print("9. Sum of n Natural Numbers")
    print("10. Check Perfect Number")
    print("0. Exit")
    print("----------------------------")

while True:
    menu()
    choice = input("Enter your choice: ")

    if choice == '0':
        print("Thank You for using the Function Bank!!")
        break

    elif choice == '1':
        myProg.replace_subinstr_demo()
        a = input("Enter the main string: ")
        old = input("Enter the substring to replace: ")
        new = input("Enter the new substring: ")
        print("Modified string:", myProg.replace_subinstr(a, old, new))

    elif choice == '2':
        myProg.checkChar_demo()
        c = input("Enter a character: ")
        print("Character is:", myProg.checkChar(c))

    elif choice == '3':
        myProg.lenofstr_demo()
        s = input("Enter a string: ")
        print("Length:", myProg.lenofstr(s))

    elif choice == '4':
        myProg.diamondPattern_demo()
        rows = int(input("Enter number of rows: "))
        myProg.diamondPattern(rows)

    elif choice == '5':
        myProg.pyramid_demo()
        rows = int(input("Enter number of rows: "))
        myProg.pyramid(rows)

    elif choice == '6':
        myProg.floyd_demo()
        rows = int(input("Enter number of rows: "))
        myProg.floyd(rows)

    elif choice == '7':
        myProg.find_roots_demo()
        a = float(input("Enter coefficient a: "))
        b = float(input("Enter coefficient b: "))
        c = float(input("Enter coefficient c: "))
        myProg.find_roots(a, b, c)

    elif choice == '8':
        myProg.numberofdigit_demo()
        num = int(input("Enter a number: "))
        print("Number of digits:", myProg.numberofdigit(num))

    elif choice == '9':
        myProg.sumofn_demo()
        num = int(input("Enter a number: "))
        print(f"Sum of first {num} numbers is:", myProg.sumofn(num))

    elif choice == '10':
        myProg.is_perfect_demo()
        num = int(input("Enter a number: "))
        if myProg.is_perfect(num):
            print(f"{num} is a Perfect Number!")
        else:
            print(f"{num} is NOT a Perfect Number")

    else:
        print("Invalid choice! Please try again.")
