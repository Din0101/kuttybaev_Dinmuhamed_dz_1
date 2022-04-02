
user_lst = []
user_lst2=[]
i = 1
while i < 1000:
    user_lst.append(i * i * i)
    i += 2
i=0
while i < 500:
    user_lst[i] += 17
    i += 1
print("Список кубов нечетных чисел: " , user_lst)
for element in user_lst:
    user_lst2.append(str(element))
for element in user_lst2:
    i = 0
    sum_elem = 0
    while i < len(element):
        sum_elem += int(element[i])
        i += 1
    if sum_elem % 7 == 0:
        print("число, сумма цифр кратная 7 :" , element)

