user_number = int(input("Введите число от 1 до 100:"))
if user_number == 1:
    print(user_number, " процент")
elif user_number > 1 and user_number < 5:
    print(user_number, " процента")
elif user_number > 4 and user_number <=100:
    print(user_number, " процентов")
else:
    print("Введите число от 1 до 100")