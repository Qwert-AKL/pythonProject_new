spisok_vsjakoj_figni=['1','Cлон',',буква','имя']
print(spisok_vsjakoj_figni)
spisok_vsjakoj_figni[2]='клоп'
print(spisok_vsjakoj_figni)
spisok_vsjakoj_figni.append ('клопик') # нужно добавлять ковычки. Команда добавляет данные в конец списка
print(spisok_vsjakoj_figni)
spisok_vsjakoj_figni.extend('string') # распределяет слово по символьно
print(spisok_vsjakoj_figni)
spisok_vsjakoj_figni.extend(['СЛОВО',2,4,"cписок"]) #добавление более чем 1
print(spisok_vsjakoj_figni)
spisok_vsjakoj_figni.remove("cписок")    #удаление из списка
print(spisok_vsjakoj_figni)
print("Cлон" in spisok_vsjakoj_figni) #in проверяет наличие в списке словва СЛОН
print("Cлон" not in spisok_vsjakoj_figni) # not in проверка отсутсвия  списке
print(spisok_vsjakoj_figni[0:5:1])   #вывод списка через срезы [начало символ 0: конец символов 5: шаг:1]