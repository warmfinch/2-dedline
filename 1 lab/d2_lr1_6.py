symbol = input("символ: ")
height = int(input("высота: "))
width = int(input("ширина: "))

i = 0
while i < height:
    j = 0
    while j < width:
        print(symbol, end="")
        j += 1
        
    print()
    i += 1