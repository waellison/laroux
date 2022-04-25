"""
Laroux: a simple, friendly LRU cache.

Copyright (c) 2022 by William Ellison.

Laroux is free software: you can redistribute it and/or modify it under the
terms of the GNU General Public License as published by the Free Software
Foundation, either version 3 of the License, or (at your option) any later
version.

Laroux is distributed in the hope that it will be useful, but WITHOUT ANY
WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
FOR A PARTICULAR PURPOSE.  See the GNU General Public License for details.

You should have received a copy of the GNU General Public License along with
Laroux.  If not, see <https://www.gnu.org/licenses>.
"""
from typing import Union, Generic, TypeVar

_T = TypeVar('T')

# Removal from the backing list is a O(N) operation.  If I added a
# class to make the list node retrievable via the backing hash table,
# I could get constant-time retrieval from the list together with
# the benefit of being able to maintain order as desired.


class LarouxCache(Generic[_T]):
    def __init__(self, max_size: int = 32):
        self._max_size: int = max_size
        self._hash_table = dict()
        self._cache_list: _LarouxCacheList[_T] = _LarouxCacheList[_T]()
        self._length: int = 0

    def __len__(self) -> int:
        return self._length

    def resize(self, new_size: int) -> None:
        self._max_size = new_size

    def push(self, value: _T) -> None:
        if "__hash__" not in dir(value):
            raise ValueError("child object of Laroux cache must be hashable")

        value_hash = hash(value)
        self._hash_table[value_hash] = value
        self._cache_list.push(value)
        self._length += 1
        self._evict()

    def _evict(self) -> None:
        if len(self) > self._max_size:
            last = self._cache_list.head.prev
            self._hash_table.pop(hash(last), 'oops')
            self._cache_list.pop()
            self._length -= 1

    def peek(self) -> Union[_T, None]:
        return self._cache_list.peek().value

    def __getitem__(self, item: _T) -> Union[_T, None]:
        retval = self._hash_table.get(hash(item), None)

        if retval:
            connected_node = self._cache_list.find(retval)
            _ = self._cache_list.remove(connected_node)
            self._cache_list.push(retval)

        return retval

    def __str__(self):
        return str([n.value for n in self._cache_list])


class _ListNode(Generic[_T]):
    def __init__(self, value: Union[_T, None]):
        self.value = value
        self.prev: Union[_ListNode[_T], None] = None
        self.next: Union[_ListNode[_T], None] = None
    
    def __str__(self) -> str:
        return str(self.value)

class _ListIterator(Generic[_T]):
  def __init__(self, linked_list):
    self.current = linked_list.head.next
    self.sentinel = linked_list.head
  
  def __next__(self):
    if self.current == self.sentinel:
      raise StopIteration
    retval = self.current
    self.current = self.current.next
    return retval


class _LarouxCacheList(Generic[_T]):
    def __init__(self):
        self.head: _ListNode[_T] = _ListNode(None)
        self.head.prev: _ListNode[_T] = self.head
        self.head.next: _ListNode[_T] = self.head
        self._length: int = 0

    def __len__(self) -> int:
        return self._length

    def peek(self) -> _ListNode[_T]:
        return self.head.next

    def push(self, value: _T) -> None:
        node = _ListNode[_T](value)
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def __iter__(self) -> _ListIterator:
        return _ListIterator(self)

    def find(self, value) -> Union[_ListNode[_T], None]:
        here: _ListNode[_T] = self.head.next

        while here != self.head:
            if hash(here.value) == hash(value):
                return here
            else:
                here = here.next

        return None

    def remove(self, node: Union[_ListNode[_T], None]) -> Union[_T, None]:
        if node:
            previous = node.prev
            following = node.next
            previous.next = following
            following.prev = previous
            node.next = None
            node.prev = None
            return node.value
        return None

    def pop(self) -> None:
        last = self.head.prev.prev
        last.next = self.head
        self.head.prev = last

    def __str__(self) -> str:
        return str([str(n) for n in self])
        