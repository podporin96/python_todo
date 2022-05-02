HELP = """
help - напечатать справку по программе
add - добавить задачу в список (название задачи запрашиваем у пользователя)
show - напечатать все добавленные задачи
end - выйти из программы
random - добавить случайную задачу на дату сегодня"""
RANDOM_TASK = "Записаться на курс "
tasks = {
  
}

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
  elif command =="end":
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
  elif command =="random":
    add_todo("Сегодня", RANDOM_TASK)
  else:
    print("Неизвестная команда!")
print("До свидания") 