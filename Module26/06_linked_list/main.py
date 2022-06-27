from typing import Any, Optional


class Node:
    """Инициализация метода
    self.value  - значение
    self.next - следующее значение
    """
    def __init__(self, value: Optional[Any] = None, next: Optional['Node'] = None) -> None:
        self.value = value
        self.next = next

    def __str__(self) -> str:
        return '[{value}]'.format(value=str(self.value))


class LinkedList:
    """Инициализация связанного списка
    self.head -иначально None (головной элемент списка),
    потом становится узлом
    """
    def __init__(self) -> None:
        self.head: Optional[Node] = None
        self.length = 0

    def __str__(self) -> str:
        if self.head is not None:
            current = self.head
            values = [str(current.value)]
            while current.next is not None:
                current = current.next
                values.append(str(current.value))
            return '[{values}]'.format(values=' '.join(values))
        return 'LinkedList []'

    def append(self, element: Any) -> None:
        """Метод добавления элемента в список
        new_node = Node(element)
        Новый элемент добавление элемента в конец списка
        Если self.head is None - то self.head будет новый элемент и вернуть
        """
        new_node = Node(element)
        if self.head is None:
            self.head = new_node
            return

        """Следующий last = self.head
        Если следующий элемент есть - берем его и последним узлом
        делаем соседний элемент
        Увеличиваем счетчик на 1"""
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
        self.length += 1

    def remove(self, index) -> None:
        """Удаление элемента по индексу
        cur_node - начало
        cur_index - изначально 0
        Сравниваем длину с нулем и индексом -если 0 или меньше индекса -выходим
        """
        cur_node = self.head
        cur_index = 0
        if self.length == 0 or self.length < - index:
            raise IndexError

        """Проверка является ли текущий индекс пустым"""
        if cur_node is not None:
            if index == 0:
                self.head = cur_node.next
                self.length -= 1
                return

        """Проверка текущего индекса с переданным
        предыдущий  prev = cur_node
        """
        while cur_node is not None:
            if cur_index == index:
                break
            prev = cur_node
            cur_node = cur_node.next
            cur_index += 1

        prev.next = cur_node.next
        self.length -= 1

    def get(self, index) -> None:
        """Получение элемента по индексу
        cur_node - начало
        cur_index - изначально 0
        Сравниваем длину с нулем и индексом -если 0 или меньше индекса -выходим
        """
        cur_node = self.head
        cur_index = 0
        if self.length == 0 or self.length < - index:
            raise IndexError

        """Проверка является ли текущий индекс пустым"""
        if cur_node is not None:
            if index == 0:
                self.head = cur_node.next
                self.length -= 1
                return

        """Проверка текущего индекса с переданным
        предыдущий  prev = cur_node
        Когда нашли - возвращаем cur_node
        """
        while cur_node is not None:
            if cur_index == index:
                break
            prev = cur_node
            cur_node = cur_node.next
            cur_index += 1
        return cur_node


my_list = LinkedList()
my_list.append(10)
my_list.append(20)
my_list.append(30)
print('Текущий список:', my_list)
print('Получение третьего элемента:', my_list.get(2))
print('Удаление второго элемента.')
my_list.remove(1)
print('Новый список:', my_list)
