# 1 вариант
#line = input("Введите слово ")
#if line==line[::-1]:
#    print("Yes")
#else:
#    print("No")


# 2 вариант
print("Программа проверяет является ли введенная строка палиндромом ")
line = input("Введите строку: ")
f = filter(str.isalpha, line)
clear_line = "".join(f).lower()
reverse_line = "".join(reversed(clear_line))
if clear_line==reverse_line:
    print(f"Строка {line} является палиндромом")
else:
    print("No")
