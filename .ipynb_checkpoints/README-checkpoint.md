Report on Parallel Processing and Database Connection Management

1. Introduction
This report presents an analysis of parallel processing in two distinct scenarios: database connection management using multiprocessing and performance evaluation of square computations using different execution methods. The objective is to observe how multiprocessing improves or impacts performance compared to sequential execution.

2. Database Connection Management
The first part of the implementation involved simulating database connections with limited availability using multiprocessing. The connection pool was set to allow a maximum of three concurrent connections, while six processes attempted to access the database.

2.1 Observed Output:

Processes request database connections sequentially.

Once a connection is available, a waiting process acquires it.

Processes release connections after completing their operations, allowing other waiting processes to proceed.

No deadlocks or excessive delays occurred, indicating efficient connection management.

2.2 Key Findings:

The use of a semaphore ensured that only three processes accessed the database at a time.

Processes properly released connections, allowing smooth operation and preventing resource starvation.

This method effectively simulates real-world scenarios where database access needs to be regulated to prevent overload.

3. Square Computation Performance Analysis
The second part of the experiment compared different execution methods for computing squares of large numbers, evaluating sequential execution, multiprocessing, and the ProcessPoolExecutor.

3.1 Execution Times for 10^6 Numbers:

Sequential Execution Time: 0.0675 seconds

Multiprocessing Execution Time: 0.1733 seconds

ProcessPoolExecutor Execution Time: 99.2690 seconds

3.2 Execution Times for 10^7 Numbers:

Sequential Execution Time: 0.6386 seconds

Multiprocessing Execution Time: 1.0787 seconds

3.3 Key Observations:

Surprisingly, multiprocessing performed worse than sequential execution for the given dataset size.

The ProcessPoolExecutor method took significantly longer, likely due to overhead in managing multiple processes.

Multiprocessing is beneficial for highly computational tasks but may not be ideal for small-scale operations due to process management overhead.

4. Conclusion
The experiments provided insights into the trade-offs of multiprocessing. While effective for controlled database connection management, its benefits for computational tasks depend on the dataset size and task complexity. In scenarios where process creation overhead outweighs parallelization benefits, sequential execution remains optimal. Future improvements could involve testing with different CPU loads and optimizing process synchronization for better efficiency.