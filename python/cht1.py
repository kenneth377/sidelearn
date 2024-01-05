num = int(input("Input number: "))

if num%4 == 0:
    if num % 100==0:
        if num % 400==0:
            print("Leap")
        else:
            print("Not leap")       
    else:
        print("Leap")
else:
    print("Not Leap")
