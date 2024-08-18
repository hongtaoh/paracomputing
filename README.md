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

## Task parallelism

If we only leverage task parallelism:

```py
def process_data_task_parallelism(n, r):
    """Task parallelism
    """
    data = get_data(n, r)
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [
            executor.submit(func1, data),
            executor.submit(func2, data),
            executor.submit(func3, data),
        ]
        results = [f.result() for f in futures]
    return results 

results_task_parallelism = []
for n in ns:
    for r in rs:
        results_task_parallelism.append(process_data_task_parallelism(n, r))
```

## Data parallelism

If we only leverage data parallelism:

```py
with concurrent.futures.ProcessPoolExecutor() as executor:
    futures = [executor.submit(process_data_no_parallelism, n, r) for n in ns for r in rs]
    results_data_parallel = [f.result() for f in futures]
```

## Task parallelism + Data parallelism

```py
with concurrent.futures.ProcessPoolExecutor() as executor:
    futures = [executor.submit(process_data_task_parallelism, n, r) for n in ns for r in rs]
    results_parallel = [f.result() for f in futures]
```

## Result

```bash
Data Parallelism + Task Parallelism execution time: 0.1675 seconds
Task Parallelism Only execution time: 0.3905 seconds
Data Parallelism Only execution time: 0.1355 seconds
No Parallelism execution time: 0.3898 seconds
```
