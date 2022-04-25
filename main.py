import laroux

# I need a proper testing suite.

lru_cache = laroux.LarouxCache[str](max_size=3)

lru_cache.push("a")
print(lru_cache)
lru_cache.push("b")
print(lru_cache)
lru_cache.push("c")
print(lru_cache)
lru_cache.push("d")
print(lru_cache)
bee = lru_cache["b"]
print(lru_cache)
