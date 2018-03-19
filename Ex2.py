print("Insert a string:")
str = input()
l = len(str)

if l<2 :
    print("")
else :
    print(str[0]+str[1]+str[l-2]+str[l-1])