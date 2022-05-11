# Welcome to Laroux

[![CodeQL](https://github.com/waellison/laroux/actions/workflows/codeql-analysis.yml/badge.svg)](https://github.com/waellison/laroux/actions/workflows/codeql-analysis.yml)
[![License: AGPL v3](https://img.shields.io/badge/License-AGPL_v3-blue.svg)](https://www.gnu.org/licenses/agpl-3.0)

_Laroux_ is a simple, friendly LRU cache written in Python.

An LRU cache, or least-recently-used cache, stores items based on recency of access, and the least recently used items will be removed from the cache when new items are added.  Laroux defaults to a 32-member cache, but you may set the size of the cache as desired when using it:

```python
from your_code import Document
from laroux import LarouxCache

class Server:
  def __init__(self):
    self.cache = LarouxCache[Document]()
    self.port = 80

  def serve(url: str) -> Document:
    if self.cache.get(url) is not None:
      return self.cache[url]
    else:
      doc = fetch(url)
      self.cache.push(url, doc)
      return doc
```

Using an LRU cache is a reasonable and easy way to improve the performance of your Web application by running it in the server used on your load balancer.  As with all caching, experimentation is encouraged and you may need to tweak Laroux slightly to better suit your needs.  If you've made a change to Laroux that you think would be beneficial, don't hesitate to submit a pull request.
