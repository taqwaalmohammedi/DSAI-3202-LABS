DSAI 3202 - Assignment 1 - Part 1 Report

1. Introduction

This report presents the results and observations of the process synchronization simulation and parallel computation using multiprocessing. The objective of this assignment was to implement a controlled database connection pool and evaluate the performance of different multiprocessing techniques for computing squares of large datasets.

2. Process Synchronization Simulation

2.1 Description

A database connection pool was implemented to allow multiple processes to access database connections in a controlled manner. The connection pool had a maximum of three available connections, but six processes attempted to access it simultaneously. A semaphore mechanism was used to ensure that only three processes could hold a connection at any given time.

2.2 Observed Output

Starting Process Simulation...
Process 0 is waiting for a connection...
Process 0 acquired DB_Conn_2.
Process 1 is waiting for a connection...
Process 1 acquired DB_Conn_2.
Process 2 is waiting for a connection...
Process 2 acquired DB_Conn_2.
Process 3 is waiting for a connection...
Process 4 is waiting for a connection...
Process 5 is waiting for a connection...
Process 2 released DB_Conn_2.
Process 3 acquired DB_Conn_2.
Process 1 released DB_Conn_2.
Process 4 acquired DB_Conn_2.
Process 0 released DB_Conn_2.
Process 5 acquired DB_Conn_2.
Process 3 released DB_Conn_2.
Process 5 released DB_Conn_2.
Process 4 released DB_Conn_2.

2.3 Analysis

The simulation correctly enforces the limit of three simultaneous connections.

Processes beyond the limit must wait until an existing process releases a connection.

Connections appear to be labeled incorrectly (DB_Conn_2 is repeatedly assigned) rather than distinct labels (DB_Conn_1, DB_Conn_2, DB_Conn_3).

The process execution order is not strictly sequential due to the randomized sleep time in each process.

2.4 Recommendations

Ensure unique connection identifiers when a process acquires a connection.

Log which process acquires/releases which connection to improve traceability.

3. Square Computation Tests

3.1 Description

The second part of the assignment evaluates different multiprocessing techniques to compute squares of numbers efficiently. Various methods were tested on datasets containing 10⁶ and 10⁷ random numbers.

3.2 Observed Output

Starting Square Computation Tests...
Running tests for 10^6 numbers:
Sequential Execution Time: 0.0675 seconds
Multiprocessing Execution Time: 0.1733 seconds

3.3 Analysis

Sequential Execution is faster than Multiprocessing Execution for 10⁶ numbers.

This contradicts expectations because multiprocessing is generally expected to improve performance.

Possible causes:

Process creation overhead: Multiprocessing has an initial overhead for creating new processes, making it inefficient for small workloads.

I/O bottlenecks: If the multiprocessing approach involves excessive memory access or inter-process communication, it may slow down execution.

3.4 Recommendations

Perform tests on 10⁷ numbers to determine if multiprocessing becomes more efficient at a larger scale.

Optimize multiprocessing techniques by:

Using Pool.map instead of individual apply_async calls to minimize inter-process communication.

Experimenting with concurrent.futures.ProcessPoolExecutor for better task distribution.

4. Conclusion

The process synchronization simulation correctly manages limited database connections but requires a fix for unique connection identifiers.

Multiprocessing performance for square computation is currently slower than sequential execution, likely due to process creation overhead.

Further optimizations are needed to improve multiprocessing efficiency, especially for larger datasets.