from laroux import LarouxCache
import pytest

def test_new_cache_is_empty():
  cache = LarouxCache[str, str]()
  assert len(cache) == 0

