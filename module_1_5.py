#2
immutable_var=1,2,4,5,'H',True
print('Immutable tuple: ', immutable_var)
#3
#immutable_var[0]=77 # Кортежи нельзя поменять, они неизменны,если не содержат внутри список.
#4
mutable_list=([0,777,555],"НЕ изменить_1",456,"буква") #кортеж со [списком] в данном случае можно метять, только значения списка внутри кортежа
mutable_list[0][1]="замена возможна"
print("Mutable list: ", mutable_list)