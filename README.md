# Iterator-Generator-Examples
Iterator and Generator Usage Examples in Python

### Overview

- **Iterators**: An iterator is an object in Python that implements the iterator protocol, consisting of the methods `__iter__()` and `__next__()`. Iterators allow you to loop over data without needing to load everything into memory at once, which makes them memory efficient for large datasets.
  
- **Generators**: A generator is a special type of iterator created using functions and the `yield` keyword. Unlike a regular iterator, a generator computes values one at a time as they are needed, making it useful for generating large sequences of data without consuming large amounts of memory.
