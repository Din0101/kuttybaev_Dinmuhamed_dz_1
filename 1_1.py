vrem = int(input("Введите секунды:"))
if vrem >= 0:
    if vrem < 60:
        print(str(vrem)+' сек')
    elif vrem < 3600:
        print(str(vrem // 60) + ' мин ' + str(vrem % 60) + ' сек')
    elif vrem < 216000:
        print(str(vrem // 3600) + ' час ' + str(vrem % 3600 // 60) + ' мин ' + str(vrem % 3600 % 60) + ' сек')
    else:
        print(str(vrem // 216000) + ' дн ' + str(vrem % 216000 // 3600) + ' час ' + str(vrem % 216000 % 3600 // 60) + ' мин '
              + str(vrem % 216000 % 3600 % 60) + ' сек')
else:
    print("Время не может быть отрицательным")