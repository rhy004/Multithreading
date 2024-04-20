# Multithreading
## Methodology<br>
### 1> The code uses multiprocessing in Python to parallelize matrix multiplication.
### 2> It generates 100 random matrices and multiplies each with a constant matrix.
### 3> The number of threads is set to the CPU count for parallel processing.
### 4> A multiprocessing pool is created and used to map the matrix multiplication function to the constant matrix.
### 5> The pool is closed and joined to wait for all processes to finish.
### 6> The execution times for each thread count are recorded and displayed in a result table.
### 7> The execution times are plotted against the number of threads to visualize performance.<br>

## Result Table<br>
### the result table contains the number of threads and the corresponding execution time for each thread.
![result_table](https://github.com/rhy004/Multithreading/assets/91721588/a870aa9d-46d5-4fc4-b406-4d2b6b21df7c)

![cpu_usage](https://github.com/rhy004/Multithreading/assets/91721588/d8a15b73-332d-4657-88da-57eeced9f0bd)


## Result Graph<br>
### the result table is used to plot a graph showing the relationship between the number of threads and the execution time. The x-axis represents the number of threads, and the y-axis represents the time in seconds.

![multithreading_graph](https://github.com/rhy004/Multithreading/assets/91721588/8aa24ea9-9bae-44a8-bbef-75db359c3309)
