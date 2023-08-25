class ToDo_List:
    def __init__(self, tasks_list):
        self.tasks_list = tasks_list

    def add_a_task(self, task2add):
        if task2add not in self.tasks_list:
            self.tasks_list.append(task2add)
            self.list_of_tasks()
        else:
            print("\nTask already in\n")

    def remove_a_task(self, task2remove):
        if task2remove not in self.tasks_list:
            print("\nTask not present\n")
            self.list_of_tasks()
        else:
            self.tasks_list.remove(task2remove)
            self.list_of_tasks()

    def list_of_tasks(self):
        print("=== The list of tasks is ===")
        for i,item in enumerate(self.tasks_list):
            print(f"{i}. {item}")
        print("")


print("============= Welcome To-Do list =============")
my_List = []
todo_list = ToDo_List(my_List)
while True:
    print(
        """==> Choose an option:
1. Add a task
2. Remove a task
3. List of all tasks
4. Exit"""
    )
    op_selected = input("==> Enter your choice: ")
    if op_selected == "1":
        task_to_add = input("==> Enter your task: ")
        todo_list.add_a_task(task_to_add)
    elif op_selected == "2":
        task_to_remove = input("==> Enter task to remove: ")
        todo_list.remove_a_task(task_to_remove)
    elif op_selected == "3":
        todo_list.list_of_tasks()
    elif op_selected == "4":
        print("*** Exiting The program... ")
        break
    else:
        print("*** Wrong Input ***")