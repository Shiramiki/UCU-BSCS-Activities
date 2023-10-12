num = 0
total=count=0

while num != "done":
    num=(input("Please enter a number: "))
    try:
        number=int(num)
        print(number)
        total= total + number
        count += 1
    except:
        print("bad data \n Invalid input")
        num=(input("Please enter a number: "))

    else:
        print("This is our else")
    
    finally:
        print("This always works")
    
average= total/count
print(f"Total = {total},\t Count = {count}, \t Average = {average}")
