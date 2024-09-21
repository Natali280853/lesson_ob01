# Менеджер задач
# Task - задача
# (description; data_end; completed) - описание задачи; срок выполнения;
# статус (выполнено=True/не выполнено=False)

class Task:

    def __init__(self, description, data_end):
        self.description = description
        self.data_end = data_end
        self.completed = False


class TaskManager:

    def __init__(self):
        self.tasks = []

    def add_task(self, description, data_end):
        new_task = Task(description, data_end)
        self.tasks.append(new_task)
        print(f"Добавлена новая задача: {description}")

    def mark_task_completed(self, task_index):
        if int(task_index) < int(len(self.tasks)):
            self.tasks[task_index].completed = True

            curr_description = self.tasks[task_index].description
            print(f"Задача \"{curr_description}\" отмечена, как выполненная.")
        else:
            print("Неверный индекс задачи.")

    def list_current_tasks(self):
        current_tasks = [task for task in self.tasks if not task.completed]
        if current_tasks:
            print("Текущие задачи:")
            for index, task in enumerate(current_tasks):
                print(f"{index + 1}. {task.description} (срок: {task.data_end})")
        else:
            print("Все задачи выполнены.")


task_manager = TaskManager()
task_manager.add_task("Написать программу на Python", "18.09.24")
task_manager.add_task("Пройти следующий урок", "19.09.24")
task_manager.add_task("Составить отчет о выполненной работе", "25.09.24")

task_manager.mark_task_completed(0)

task_manager.list_current_tasks()
