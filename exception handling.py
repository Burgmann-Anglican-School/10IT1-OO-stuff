my_num = input("Enter a number: ")

while my_num:
    try:
        my_num = my_num
        my_num = 10 + my_num
        print(f"10 divided by your number is: {my_num}")
    except ValueError:
        print(f"You entered {my_num}, that is not a number")
    #except ZeroDivisionError:
    #    print(f"Why would you do that...😔")
    except:
        print("A thing happened 🤭")
    my_num = input("Enter a number: ")
    