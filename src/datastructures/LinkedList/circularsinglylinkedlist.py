""" Circular Singly List Implementation

"""

from __future__ import annotations

import warnings
from typing import Any

from .nodes import SinglyLinkedListNode

__all__ = ['CircularSinglyLinkedList']

class CircularSinglyLinkedList:
    
    slots = ["_head","_tail","_length"]
    
    def __init__(self) -> None:
        self._head = None
        self._tail = None
        self._length = 0
    
    
    @property
    def head(self) -> CircularSinglyLinkedList | None:
        return self._head
    
    @head.setter
    def head(self, value: SinglyLinkedListNode) -> None:
        if isinstance(value, SinglyLinkedListNode) or value is None:
            self._head = value
        else:
            raise ValueError(
                f"Head can be of type SinglyLinkedListNode or None not {type(value)}")

    @property
    def tail(self) -> CircularSinglyLinkedList | None:
        return self._tail
    
    @tail.setter
    def tail(self, value: SinglyLinkedListNode) -> None:
        if isinstance(value, SinglyLinkedListNode) or value is None:
            self._tail = value
        else:
            raise ValueError("Tail can be of type SinglyLinkedListNode or None")

    @property
    def length(self) -> int:
        return self._length
    
    @length.setter
    def length(self, value: int) -> int:
        if isinstance(value, int):
            self._length = value
        else:
            raise ValueError("Length can be of type Integer only")
    
    def to_list(self) -> list:
        return list(self)

    def clear(self) -> None:
        self.head = None
        self.tail = None
        self.length = 0
    
    def append_node(self, node: SinglyLinkedListNode) -> None:
        if isinstance(node, SinglyLinkedListNode):
            if self.head:
                self.tail.next = node
                node.next = self.head
                self.tail = node
            else:
                self.head = node
                self.tail = node
                self.tail.next = self.head
            self.length += 1
        else:
            raise TypeError(
                "We can only append SinglyLinkedListNode to \
                CircularSinglyLinkedList"
                )
    
    def prepend_node(self, node: SinglyLinkedListNode) -> None:
        if isinstance(node, SinglyLinkedListNode):
            if self.head:
                node.next = self.head
                self.head = node
                self.tail.next = self.head
            else:
                self.head = node
                self.tail = node
                self.tail.next = self.head
            self.length += 1    
        else:
            raise TypeError(
                f"we can only append SinglyLinkedListNode to"
                "Circular Singly Linked list"
            )

    def insert_node(self, node: SinglyLinkedListNode, index: int) -> None:
        if isinstance(index, int):
            index = self._handle_negative_index(index)
        else:
            raise TypeError(
                "Index must be an integer"
            )

        if isinstance(node, SinglyLinkedListNode):
            if index == 0:
                self.prepend(node)
            elif index == self.length:
                self.append(node)
            else:
                current_pos = 0
                current_node = self.head
                while current_pos < index-1 and current_node is not None:
                    current_node = current_node.next
                    current_pos += 1
                node.next = current_node.next
                current_node.next = node
                self.length += 1
        else:
            raise TypeError(
                f"we can only insert SinglyLinkedListNode to"
                "Circular Singly Linked list"
            )


    def append(self, value: Any) -> None:
        if isinstance(value, SinglyLinkedListNode):
            self.append_node(value)
        else:
            self.append_node(SinglyLinkedListNode(value))


    def prepend(self, value: Any) -> None:
        if isinstance(value, SinglyLinkedListNode):
            self.prepend_node(value)
        else:
            self.prepend_node(SinglyLinkedListNode(value))

    def insert(self, value: Any, index: int) -> None:
        if isinstance(value, SinglyLinkedListNode):
            self.insert_node(value, index)
        else:
            self.insert_node(SinglyLinkedListNode(value), index)



    def _handle_negative_index(self, index: int) -> int:
        # Condition to handle neg index < length
        # (smaller negative index than length)
        # this will make sure that we pop the first element incase of
        # negative index less than -1*length
        if index < 0:
            index = max(self.length + index, 0)
        if index > self.length:
            index = self.length
        return index

    def __str__(self) -> str:
        str_repr = ''
        current_node = self.head
        while current_node is not None:
            str_repr += str(current_node.data) + ' -> '
            current_node = current_node.next
            if current_node is self.head:
                break
        str_repr += 'Done'
        return f'{self.__class__.__name__}: [{str_repr}]'

    def __repr__(self) -> str:
        return self.__str__()

    def __len__(self) -> int:
        return self.length

    def __bool__(self) -> bool:
        return bool(self.head or self.tail or self.length)

    def __iter__(self):
        current = self.head
        while current:
            yield current.data
            current = current.next
            if current is self.head:
                break