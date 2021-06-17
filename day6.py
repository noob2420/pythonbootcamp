# program to remove a key from  a dictionary
a = {}
while True:
    num1 = int(input("Enter 1 to add elements in dictionary ,2 to remove, 3 to exit "))
    if num1 == 1:
        c = eval(input("enter key :"))
        d = eval(input("enter value :"))
        a[c] = d
    if num1==2 :
        f=eval(input("enter the key to be deleted"))
        if f in a:
            del a[f]
            print("success")
        else:
            print("not found")
    if num1==3:
        break
print(a)

#python program to map two list into  a dictionary
print("enter 2 list of equal length to map into dictionary")
a=eval(input("enter a list1 : "))
b=eval(input("enter a list2 : "))
c={}
for i in range(len(a)):
    c[a[i]]=b[i]
print(c)

#program to find the length of the set
a=eval(input("Enter a set to find its length : "))
print("Length of the Set : ",len(a))