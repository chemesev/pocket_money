#! /usr/bin/env python3
import sqlite3

def first_start():
    temp_name = input("Как вас зовут? ")
    temp_budget = input("Каков ваш стартовый бюджет? ")
    temp_budget = float(temp_budget)
    c.execute('CREATE TABLE user_info (name text, budget real)')
    temp = (temp_name, temp_budget,)
    c.execute('INSERT INTO user_info VALUES (?,?) ', temp)
    db_connect.commit()

def edit_budget(user_input, budget_inc):
    if user_input[0] == '-':
        budget_inc -= float(user_input[1:])
        return budget_inc
    else:
        budget_inc += float(user_input)
        return budget_inc

def main_text():
    print('Добро пожаловать,', usr_name)
    print('Это тестовая программа, сохранение данных ВОЗМОЖНО(ура!)')
    print('Но программисто всё так же криворук')
    print('Чтобы добавить к бюджету - напишите, сколько нужно добавить.')
    print('Чтобы отнять допишите минус перед числом и, без пробела, сколько нужно отнять')
    print('Для выхода - напишите exit или закройте программу')
    print('Удачи')
    return None

if __name__ == '__main__':
    db_connect = sqlite3.connect('my_pocket.db')
    try:
        c = db_connect.cursor()
        c.execute('SELECT * FROM user_info')
    except sqlite3.OperationalError as err:
        first_start()

    c.execute('SELECT * FROM user_info')
    for row in c:
        usr_name = row[0]
        usr_budget = row[1]

    #usr_data = (usr_budget, usr_name)
    main_text()
    print('Текущий бюджет:', usr_budget)

    while True:
        var = input()
        if var == 'exit':
            break
        try:
            usr_budget = edit_budget(var, usr_budget)
        except ValueError:
            print('Нужны числа')
        c.execute('UPDATE user_info SET budget=? WHERE name = ?''',(usr_budget, usr_name,))
        print('Текущий бюджет:', usr_budget)

    db_connect.close()
