# Welcome to Laroux

[![Codacy Badge](https://app.codacy.com/project/badge/Grade/b99d68b5653145749a44bc171bf08dd1)](https://www.codacy.com/gh/waellison/laroux/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=waellison/laroux&amp;utm_campaign=Badge_Grade)
[![Codacy Badge](https://app.codacy.com/project/badge/Coverage/b99d68b5653145749a44bc171bf08dd1)](https://www.codacy.com/gh/waellison/laroux/dashboard?utm_source=github.com&utm_medium=referral&utm_content=waellison/laroux&utm_campaign=Badge_Coverage)
[![build](https://github.com/waellison/laroux/actions/workflows/pytest.yml/badge.svg)](https://github.com/waellison/laroux/actions/workflows/pytest.yml)
[![CodeQL](https://github.com/waellison/laroux/actions/workflows/codeql-analysis.yml/badge.svg)](https://github.com/waellison/laroux/actions/workflows/codeql-analysis.yml)
[![License](https://img.shields.io/github/license/waellison/laroux)](#)

_Laroux_ is a simple, friendly LRU cache written in Python.

An LRU cache, or least-recently-used cache, stores items based on recency of access, and the least recently used items will be removed from the cache when new items are added.  Laroux defaults to a 32-member cache, but you may set the size of the cache as desired when using it:

```python
from your_code import Document
from laroux import LarouxCache

class Server:
  def __init__(self):
    self.cache = LarouxCache[str, Document](100)
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
