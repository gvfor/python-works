for row in range(7,0,-1):

    for sp in range(1,7-row):

        print(" ",end="")

    for col in range(1,row+1):

        print("* ",end="")

    print()
