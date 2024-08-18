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

and

```py
ns = [10, 20, 30]
rs = [0.1, 0.5, 0.9]
```

## No parallelism 

If we don't use any parallelism, we process data and implement the three functions this way:

```py
def process_data_no_parallelism(n, r):
    data = get_data(n, r)
    result1 = func1(data)
    result2 = func2(data)
    result3 = func3(data)
    return result1, result2, result3

results_no_parallelism = []
for n in ns:
    for r in rs:
        results_no_parallelism.append(process_data_no_parallelism(n, r))
```