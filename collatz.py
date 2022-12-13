print("Введите любое целое число:")
a = int(input(":"))
arr1 = []
a = a * 3
a = a + 1
NumCount = 0
NumMax = 0
NumFashion = 0
print(a)
while a != 1:
    if a %2==0:
        b = a/2
        print(b)
    else:
        b = a*3
        b = b + 1
        print(b)
    a = b
    arr1.append(a)
for i in range(0, 3):
    if a %2==0:
        b = a/2
        print(b)
    else:
        b = a*3
        b = b + 1
        print(b)
    a = b
NumCount = len(arr1)
NumMax = max(arr1)
NumFashion = max(arr1, key=arr1.count)
if arr1[0]==NumFashion:
    NumFashion = "Все числа разные."
print("Кол-во чисел:"+str(NumCount))
print("Самое большое:"+str(NumMax))
print("Популярное:"+str(NumFashion))
