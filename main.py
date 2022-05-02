import random

HELP = """
help - напечатать справку по программе
add - добавить задачу в список (название задачи запрашиваем у пользователя)
show - напечатать все добавленные задачи
exit - выйти из программы
random - добавить случайную задачу на дату сегодня"""
RANDOM_TASKS = ["записаться на курс","Купить продукты","Прочитать книгу","Написать письмо"]
tasks = {
  
}
today=[] 
tomorrow=[]
other=[]

run = True

def add_todo(date,task):
    if date in tasks:
      tasks[date].append(task)
    else:
      tasks[date] = [task]
    print("Задача",task, "добавлена на дату",date)
      
while run:
  command = input("Введите команду:")
  if command =="help":
    print(HELP)
  elif command =="exit":
    print("Спасибо за использование! До свидания!")
    break  
  elif command == "show":
    date = input("Введите дату для отображения списка задач: ")
    if date in tasks:
      for task in tasks[date]:
        print('-',task)
    else:
      print("Такой даты нет")
        
  elif command == "add":    
    task = input("Введите название задачи: ")
    date = input("Введите дату для добавления задачи: ")
    add_todo(date, task)
    # if date == "Сегодня":
    #   today.append(task)
    # elif date == "Завтра":
    #   tomorrow.append(task)
    # else:
    #   other.append(task)
    # дя 2-го ДЗ
  elif command =="random":
    task = random.choice(RANDOM_TASKS)
    add_todo("Сегодня", task)
  else:
    print("Неизвестная команда!")
    # print(today, tomorrow, other)
 