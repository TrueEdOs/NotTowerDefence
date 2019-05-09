class RunnableStack:
    def __init__(self):
        self.tasks = []

    def push(self, task):
        self.tasks.append(task)

    def pop(self):
        self.tasks.pop()

    def __len__(self):
        return len(self.tasks)

    def last_task(self):
        if len(self) == 0:
            return None
        return self.tasks[len(self) - 1]

    def is_empty(self):
        return len(self) == 0

    def set_one_task(self, task):
        self.tasks.clear()
        self.push(task)

    def clear(self):
        self.tasks.clear()
