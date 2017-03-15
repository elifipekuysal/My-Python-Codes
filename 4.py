number = input("Bir sayı giriniz: ")
total= 0

for i in number :
    x = int(i)
    total += x*x*x

if total == int(number) :
    print("It is an armstrong number")
else :
    print("It is not an armstrong number")

