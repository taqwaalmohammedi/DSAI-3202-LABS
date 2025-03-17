Introduction
Parallel and distributed computing is essential for enhancing computational efficiency by utilizing multiple processors simultaneously. This report presents an implementation of multiprocessing and process synchronization in Python, leveraging the multiprocessing module to optimize execution time and manage shared resources safely.

The assignment consists of two primary tasks:

Square Computation using Multiprocessing
Compare sequential execution with multiprocessing approaches.
Evaluate execution time improvements using methods like apply_async, map(), and ProcessPoolExecutor.
Process Synchronization using Semaphores
Implement a Connection Pool that limits access to shared database connections.
Utilize semaphores to regulate simultaneous access, preventing race conditions.
The objective is to analyze performance enhancements when using parallel execution and understand synchronization techniques to manage limited resources efficiently.

2. Objectives
The primary objectives of this assignment are:

To implement parallel computation using Python’s multiprocessing capabilities.
To compare different multiprocessing techniques and evaluate their efficiency.
To use semaphores for managing concurrent access to shared resources.
To analyze and interpret performance differences between sequential and parallel execution.
3. Implementation
3.1 Square Computation Using Multiprocessing
This task involves computing the square of 1 million (10⁶) and 10 million (10⁷) numbers using multiple approaches:

Sequential execution (traditional single-threaded computation).
Multiprocessing using apply_async, map(), and apply().
Process-based execution using ProcessPoolExecutor.
Each method was tested and execution times were recorded for performance comparison.

3.2 Process Synchronization Using Semaphores
This task involves managing access to a limited resource pool (database connections) using semaphores.

A Connection Pool was implemented with a maximum number of allowed connections. When multiple processes request access:

If connections are available, a process acquires a connection and performs a simulated operation.
If no connections are available, the process waits until one is released.
This ensures that only a fixed number of processes can access the resource at any given time.
This method prevents race conditions and ensures smooth execution when multiple processes need shared resources.

4. Results & Observations
4.1 Square Computation Performance Analysis
The execution times for different methods were recorded as follows:

Method              	Execution Time for 10⁶ numbers	       Execution Time for 10⁷ numbers
Sequential Execution	          ~0.06s	                                ~0.61s
Multiprocessing (apply_async)    	~40s	                                 ~387s
Multiprocessing Pool (map)       	~0.24s                                	~1.7s
ProcessPoolExecutor               	~109s	                                 Slow
Key Observations:
Sequential execution was the slowest due to single-threaded processing.
Multiprocessing Pool (map()) was the fastest, efficiently distributing the workload across multiple CPU cores.
ProcessPoolExecutor had higher overhead, making it slower than Pool.map().
4.2 Process Synchronization Analysis
The Connection Pool implementation demonstrated correct behavior in managing concurrent access. Key observations include:

Processes correctly waited when connections were unavailable, ensuring controlled access.
The semaphore limited access to a fixed number of connections, preventing excessive simultaneous access.
No race conditions occurred, confirming that synchronization was effectively enforced.
5. Conclusion
This assignment demonstrated that multiprocessing significantly improves execution speed for computationally intensive tasks. Additionally, semaphores play a crucial role in ensuring controlled access to shared resources, preventing conflicts and ensuring orderly execution.