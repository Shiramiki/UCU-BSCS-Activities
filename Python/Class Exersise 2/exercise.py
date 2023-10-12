def main():
    x - get_num()
    print(f"x is {x}")

def get_num():
    while True:
        try:
            x=int(input("What is x?"))
        except ValueError:
            print("x isn't an int")
        else:
            break
        finally:
            print("This always works")
    return x

main()