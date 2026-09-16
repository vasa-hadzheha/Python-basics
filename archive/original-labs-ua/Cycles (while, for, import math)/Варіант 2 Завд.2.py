n = int(input("Введіть ціле число: "))

count = 0

while n >= 0:
    f=n%10
    if f==0:
        count+=1
    n=n//10
    if n==0:
        break
print("Кількість нулів={0}".format(count))