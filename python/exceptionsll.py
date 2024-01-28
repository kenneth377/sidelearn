while True:
    try:
        num = int(input("Please enter number: "))

        print("{}".format(num+ "4"))
        break
    except ValueError:
        print("Error occured")