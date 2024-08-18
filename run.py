import time
import math
import concurrent.futures

def get_data(n, r):
    return n * r  # Scale size by a factor

def func1(data):
    result = 0
    for i in range(100000):  # Increased workload
        result += math.sin(data + i)
    return result

def func2(data):
    result = 1
    for i in range(1, 100000):  # Increased workload
        result *= (data + i) ** 0.5
    return result

def func3(data):
    result = 0
    for i in range(100000):  # Increased workload
        result += math.log(data + i)
    return result

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

def process_data_no_parallelism(n, r):
    data = get_data(n, r)
    result1 = func1(data)
    result2 = func2(data)
    result3 = func3(data)
    return result1, result2, result3

if __name__ == "__main__":
    ns = [100, 200, 300, 400, 500]  # Increased size
    rs = [0.1, 0.3, 0.5, 0.7, 0.9]  # Increased size
    
    # Measure time for data parallelism + task parallelism
    start_time = time.time()
    with concurrent.futures.ProcessPoolExecutor() as executor:
        futures = [executor.submit(process_data_task_parallelism, n, r) for n in ns for r in rs]
        results_parallel = [f.result() for f in futures]
    parallel_time = time.time() - start_time

    # Measure time for task parallelism only
    start_time = time.time()
    results_task_parallelism = []
    for n in ns:
        for r in rs:
            results_task_parallelism.append(process_data_task_parallelism(n, r))
    task_parallelism_time = time.time() - start_time

    # Measure time for data parallelism only
    start_time = time.time()
    with concurrent.futures.ProcessPoolExecutor() as executor:
        futures = [executor.submit(process_data_no_parallelism, n, r) for n in ns for r in rs]
        results_data_parallel = [f.result() for f in futures]
    data_parallelism_time = time.time() - start_time

    # Measure time for no parallelism 
    start_time = time.time()
    results_no_parallelism = []
    for n in ns:
        for r in rs:
            results_no_parallelism.append(process_data_no_parallelism(n, r))
    no_parallelism_time = time.time() - start_time

    print(f"Data Parallelism + Task Parallelism execution time: {parallel_time:.4f} seconds")
    print(f"Task Parallelism Only execution time: {task_parallelism_time:.4f} seconds")
    print(f"Data Parallelism Only execution time: {data_parallelism_time:.4f} seconds")
    print(f"No Parallelism execution time: {no_parallelism_time:.4f} seconds")

    