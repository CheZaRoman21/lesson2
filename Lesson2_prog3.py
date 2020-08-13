a = list()
a = [1,2,3,4,5,6,7,8,9,10]
num = int(input("Write a number for checking list: "))
if num>=a[0] and num<=a[len(a)-1]:
    print("This number is in the list.")
else:
    print("This number isn't in the list.")
print(a)
