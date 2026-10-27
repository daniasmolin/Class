class Task:
    def __init__(self, title, description, deadline):
        self.title = title
        self.description = description
        self.deadline = deadline
        self.completed = False

    def __str__(self):
        status = "Виконано" if self.completed else "Не виконано"
        return f"Назва: {self.title}\nДедлайн: {self.deadline}\nСтан: {status}\nОпис: {self.description}"


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, description, deadline):
        new_task = Task(title, description, deadline)
        self.tasks.append(new_task)

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)

    def mark_task_completed(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].completed = True

    def display_tasks(self):
        if not self.tasks:
            print("Список завдань порожній.")
            return
        for i, task in enumerate(self.tasks):
            print(f"[{i}]\n{task}\n")



manager = TaskManager()

manager.add_task("Вивчити Python", "Прочитати про класи", "2026-03-01")
manager.add_task("Купити продукти", "Молоко, хліб", "2026-02-28")

print("Початковий список завдань:")
manager.display_tasks()

manager.mark_task_completed(0)

print("Після позначення першого завдання як виконаного:")
manager.display_tasks()