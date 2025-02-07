FILE_NAME = 'to_do_list.txt'
def add_task():
    task = input('Enter a task: ').strip()
    if task == '':
        raise Exception('Task cannot be empty')
    try:
        with open(FILE_NAME, 'a') as file:
            file.write(task + '\n')
            print('Task added:', task)
    except:
        print('Somthing went wrong')


def show_tasks():
    try:
        if not open(FILE_NAME, 'r').read():
            print('No tasks')
        with open(FILE_NAME, 'r') as file:
            tasks = file.readlines()
            for index, task in enumerate(tasks, start=1):
                    print(f"{index}. {task}", end='')
    except:
        print('Somthing went wrong')


def delete_task():
    try:
        with open(FILE_NAME, 'r', encoding='utf-8') as file:
            tasks = file.readlines()
        
        if not tasks:
            print('No tasks to delete')
            return

        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task.strip()}")

        index = int(input('Enter the index of the task to delete: '))

        if index < 1 or index > len(tasks):
            print('Invalid index')
            return

        with open(FILE_NAME, 'w', encoding='utf-8') as file:
            for i, task in enumerate(tasks, start=1):
                if i != index:
                    file.write(task)
        
        print('Task deleted successfully')

    except ValueError:
        print('Invalid input! Please enter a number.')
    except Exception as e:
        print(f'Error: {e}')

def main():
    while True:
        print('1. Add task')
        print('2. Show tasks')
        print('3. Delete task')
        print('4. Exit')
        choice = input('Enter your choice: ')
        if choice == '1':
            add_task()
            print("----------------------------------------")
        elif choice == '2':
            show_tasks()
            print("----------------------------------------")
        elif choice == '3':
            delete_task()
            print("----------------------------------------")
        elif choice == '4':
            break
        else:
            print('Invalid choice')#
            

if __name__ == '__main__':
    main()