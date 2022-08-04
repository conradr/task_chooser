class Task:
    def __init__(self,description, preferred_list):
        self.description = description
        self.duration = 10
        self.preferred_list = preferred_list

    def tasks_not_duplicate(task1, task2):
        if task1.description == task2.description:
            return "tasks are the same"