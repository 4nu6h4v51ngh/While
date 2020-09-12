userInput = int(input("Please enter the amount of rows: "))
count = 1
spacing = 0


rows = 0
while(userInput <= rows):
    rows += count
    print()
    while(spacing <= userInput):
        spacing += count
        print(" ")
        while(numberStars <= 0):
            print(actualStars)