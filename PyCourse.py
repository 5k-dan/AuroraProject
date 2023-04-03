#from todofunctions import get_todos, write_todos
import todofunctions
import time

now = time.strftime("%b %d, %Y %H:%M;%S")
print(f"It is {now}")
while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()


    if user_action.startswith("add"):
        todo = user_action[4:]

        todos = todofunctions.get_todos('todos.txt')


        todos.append(todo + '\n')

        todofunctions.write_todos(todos)

    elif user_action.startswith("show"):
        todos = todofunctions.get_todos('todos.txt')

        for index, item in enumerate(todos):
            item = item.strip('\n')
            print(f"{index + 1}-{item}")

    elif user_action.startswith("edit"):
        try:
             number = int(user_action[5:])
             print(number)
             number = number - 1

             todos = todofunctions.get_todos('todos.txt')

             new_todo = input("Enter new todo: ")
             todos[number] = new_todo + '\n'

             todofunctions.write_todos(todos)
        except ValueError:
            print("Your command is not valid.")
            continue               # this makes the code start all over again because it's a while loop


    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])

            todos = todofunctions.get_todos('todos.txt')
            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            todofunctions.write_todos(todos)

            message = f"Todo {todo_to_remove} was removed from the list."
            print(message)
        except IndexError:
            print("There is no item with that number.")
            continue
    elif user_action.startswith("exit"):
        break
    else:
        print("Command is not valid.")



print("Bye")