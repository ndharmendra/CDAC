# find odd number from given listlst = [i for i in input("Eneter numbers: ").split(",")]for n in lst:    if int(n) % 2 != 0:        print(n, end=",")