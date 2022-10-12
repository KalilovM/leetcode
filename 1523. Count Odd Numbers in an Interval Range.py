low = 4
high = 6
result = (high - low) / 2

if low % 2 != 0 and high % 2 != 0:
    print(int(result + 1),"res 1")
elif low % 2 == 0 and high % 2 != 0:
    print(int(result + 1),"res 2")
elif low % 2 != 0 and high % 2 == 0:
    print(int(result + 1),"res 3")
else:
    print(int(result),"no res")
