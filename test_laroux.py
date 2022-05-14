from laroux import LarouxCache, _LarouxCacheList, _ListIterator, _ListNode
import pytest


def test_new_cache_is_empty():
    cache = LarouxCache[str, str]()
    assert len(cache) == 0


def test_new_cache_size_is_correct():
    cache = LarouxCache[str, str](max_size=100)
    assert cache._max_size == 100


def test_change_cache_size():
    cache = LarouxCache[str, str](max_size=100)
    cache.resize(128)
    assert cache._max_size == 128


def test_cache_size_set_correctly():
    cache = LarouxCache[str, str]()
    cache.push("foo", "a")
    assert len(cache) == 1


def test_add_and_peek():
    cache = LarouxCache[str, str](max_size=3)
    cache.push("foo", "a")
    assert cache.peek() == "a"


def test_add_and_retrieve():
    cache = LarouxCache[str, str](max_size=3)
    cache.push("foo", "a")
    cache.push("bar", "b")
    assert cache["bar"] == "b"


def test_stringize_cache():
    cache = LarouxCache[str, str](max_size=1)
    cache.push("foo", "a")
    assert str(cache) == "['a']"


def test_new_list_is_empty():
    lst = _LarouxCacheList[str]()
    assert len(lst) == 0


def test_stringize_list_node():
    lst = _LarouxCacheList[str]()
    lst.push("a")


def test_list_size_set_correctly_on_add():
    lst = _LarouxCacheList[str]()
    lst.push("a")
    assert len(lst) == 1


def test_list_size_set_correctly_on_remove():
    lst = _LarouxCacheList[str]()
    lst.push("a")
    lst.remove(lst.peek())
    assert len(lst) == 0


def test_list_iteration():
    lst = _LarouxCacheList[str]()
    lst.push("a")
    lit = iter(lst)
    assert lit.current.value == "a"


def test_list_correct_order():
    lst = _LarouxCacheList[int]()
    for i in range(10):
        lst.push(i)
    for i, v in zip(range(0, 10, -1), lst):
        assert i == v.value


def test_list_arrayize():
    array = [1, 2, 3]
    lst = _LarouxCacheList[int]()
    for i in reversed(range(1, 4)):
        lst.push(i)
    lst_array = lst.arrayize()
    assert lst_array == array


def test_list_remove():
    lst = _LarouxCacheList[int]()
    for i in reversed(range(0, 10)):
        lst.push(i)
    node = lst.find(5)
    if node:
        lst.remove(node)
    assert len(lst) == 9
    assert 5 not in lst.arrayize()
