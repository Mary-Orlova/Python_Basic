class Stack:

    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if len(self.stack) == 0:
            return None
        removed = self.stack.pop()
        return removed


class TaskManager:
    def __init__(self):
        self.stack = []

    task: str
    priority: int

    def new_task(self, task, priority):
        self.task = task
        self.priority = priority
        self.stack.append(str(priority)+" "+task)
        return self.stack

    def __str__(self):
        return str(self.stack)



stack_1 = Stack()
stack_1.push('1')
stack_1.push('2')
stack_1.push('3')
stack_1.pop()
print(stack_1.stack, '\n')

manager = TaskManager()
manager.new_task(task="сделать уборку", priority=4)
manager.new_task(task="помыть посуду", priority=4)
manager.new_task(task="отдохнуть", priority=1)
manager.new_task(task="поесть", priority=2)
manager.new_task(task="сдать дз", priority=2)

actual_stack = sorted(manager.stack)

for task in actual_stack:
    print(task)



