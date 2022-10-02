def errorfinding():
    a=0
    b=0
    print("Division simulator, type 'exit' to leave")
    while (a or b !="exit"):
        a = input("Enter 'a' value or 'exit': ")
        if a.lower() =="exit":
            print("Goodbye. ")
            break
        b = input("Enter 'b' value or 'exit': ")
        if b.lower =="exit":
            print("Goodbye. ")
            break
        try:
            c=int(a)/int(b)
            print(c)
        except ZeroDivisionError:
            print("Division by zero is not allowed")
        except ValueError:
            print(f"{a} or {b} is not a number, please try again")
        finally:
            print("Out of try except blocks ")


if __name__ == '__main__':
    errorfinding()