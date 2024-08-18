# A Super Brief Introduction to Parallel Computing 

There are two types of parallelism: data parallelism and task parallelism. 

For example, we have the following three functions:

```python
def func1(data):
    return data * 2

def func2(data):
    return data ** 2

def func3(data):
    return data / 2
```

We get data this way:

```py
def get_data(n, r):
    return n * r
```

Suppose

```py
ns = [10, 20, 30]
rs = [0.1, 0.5, 0.9]
```