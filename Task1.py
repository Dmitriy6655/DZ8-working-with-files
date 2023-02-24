# Задача No49. Решение в группах
# Создать телефонный справочник с
# возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер
# телефона - данные, которые должны находиться
# в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в
# текстовом файле
# 3. Пользователь может ввести одну из
# характеристик для поиска определенной
# записи(Например имя или фамилию
# человека)
# 4. Использование функций. Ваша программа
# не должна быть линейной


# Задача 38: Дополнить телефонный справочник возможностью
# изменения и удаления данных.
# Пользователь также может ввести имя или фамилию,
# и Вы должны реализовать функционал
# для изменения и удаления данных.

print("Телефонный справочник Ver.23.1")
# print("***Инструкция***" + "\n" + "Команды для работы:" + "\n" +
#       "add - ввод новых данных" + "\n" +
#       "ed - редактирование данных" + "\n" +
#       "sch - поиск данных" + "\n" +
#       "all - печать всего справочника" + "\n" +
#       "ex - выход из программы")

# Имя файла
nameFileTxt = 'phonebook2.txt'


###Цикл программы
def obrabotka():
    exit = True
    while exit == True:
        print("Команды: add - ввод; " +
              "ed - редакт.; " +
              "sch - поиск; " +
              "all - весь спр.; " +
              "ex - выход. ")
        comand = input("Введите команду: ")

        if comand == "add":
            k = str(input("Введите нового абонента в формате ФИО номер тел.: "))
            print(newSubscriberLogin(k))
            continue

        if comand == "ed":
            ed = input("Поиск абонента: ").lower()
            # функция печати списка с найденным(и) абонентами
            dictPrint(searchSubscriber(ed))
            # печать данных от функции проверки и ф-ии редактирования
            jkl = searchSubscriber(ed)
            print(examination(jkl))
            continue

        if comand == "all":
            # функция печати всего справочника
            printAllAbon()
            continue

        if comand == "sch":
            sch = input("Поиск абонента: ").lower()
            # функция печати списка с найденным(и) абонентами
            dictPrint(searchSubscriber(sch))
            continue

        if comand == "ex":
            print("До скорой встречи!")
            break

        else:
            print("Ошибка ввода!")


##Ввод нового абонента
def newSubscriberLogin(k):
    with open(nameFileTxt, "a") as somefile:
        somefile.write("\n" + k.lower())
        return "Абонент добавлен"


# проверка найден ли абонент
def examination(dict):
    if dict.get("er") == None:
        # передаем словарь с найденными абонентами в функцию "redactAbon"
        # для редактирования

        redactAbon(dict)
        # Печать результата выполнения
        return redactAbon(dict)


##Поиск абонента
def searchSubscriber(ed):
    with open(nameFileTxt, "r") as file:
        dictionary = {}
        contents = file.readlines()
        for num in range(len(contents)):
            if ed in contents[num]:
                ind = str(num)
                dictionary[ind] = contents[num]

        if len(dictionary) < 1:
            dict2 = {}
            dict2['er'] = 'Данные не найдены.'
            return dict2

        else:
            return dictionary


##Замена абонента в файле
def redactAbon(dict2):
    ex = True
    while ex == True:
        rowSelection = input("Укажите номер строки или введите *** 2 раза: ")

        if rowSelection == '***' and len(rowSelection) == 3:
            return 'Редактирование выполнено.'

        if rowSelection in dict2:
            newData = str(input("Выполните редактирование(при вводе пустой строки," +
                                    "абенент будет удален): "))

            with open(nameFileTxt, 'r') as f:
                old_data = f.read()
                data = dict2[rowSelection]
                new_data = old_data.replace(data, newData +'\n')
                new_data = new_data.lower()

            with open(nameFileTxt, 'w') as f:
                f.writelines(new_data + "\n")
                print('Готово!')
            continue




        elif rowSelection not in dict2 and rowSelection != '***':
            print("Повторите ввод!")
            continue




##Печать словаря
def dictPrint(dict1):
    for key, value in dict1.items():
        print(f"Строка: {key}  Абонент: {value} ")


# Печать всего списка
def printAllAbon():
    with open(nameFileTxt, "r") as file:
        for message in file:
            list1 = []
            list1.append(message)
            list1 = [line.strip() for line in file.readlines() if len(line.strip()) != 0]
            # print(message, end="\n")
        print("* * * Весь список абонентов * * *")
        for i in list1:
            print(i)
        return 1


##Продолжение выполнения программы
obrabotka()
