first=int(input("Ввведите ПЕРВОЕ целое число:  "))
second=int(input("Ввведите ВТОРОЕ целое число: "))
third=int(input("Ввведите ТРЕТЬЕ целое число: "))
print("Три числа введены \n")
if first != second != third and first !=third:
    print('Количество целых и равных между собой чисел: ', 0)
elif first == second and second == third and third == first:
    print('Количество целых и равных между собой чисел: ', 3)
elif first == second or second == third or first == third or third== first or second==first:
    print('Количество целых и равных между собой чисел: ', 2)