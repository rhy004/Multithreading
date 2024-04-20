import numpy as np
import time
import multiprocessing as mp
import matplotlib.pyplot as plt

def matrix_multiply(constant_matrix):
    # Generate 100 random matrices of size 1000x1000
    random_matrices = [np.random.rand(1000, 1000) for _ in range(100)]
    
    start_time = time.time()
    result_matrices = [np.matmul(constant_matrix, matrix) for matrix in random_matrices]
    end_time = time.time()
    
    return end_time - start_time

if __name__ == '__main__':
    constant_matrix = np.random.rand(1000, 1000)
    
    # Number of threads to use
    num_threads = mp.cpu_count()
    
    # Create a pool of processes
    pool = mp.Pool(num_threads)
    
    # Map the function to the constant matrix for parallel processing
    times = pool.map(matrix_multiply, [constant_matrix]*num_threads)
    
    # Close the pool and wait for the processes to finish
    pool.close()
    pool.join()
    
    # Generate the result table
    result_table = [{'Threads': i, 'Time (s)': times[i-1]} for i in range(1, num_threads + 1)]
    for row in result_table:
        print(row)
    
    # Extract data for plotting
    threads = [row['Threads'] for row in result_table]
    times = [row['Time (s)'] for row in result_table]
    
    # Plot the graph
    plt.figure(figsize=(10, 6))
    plt.plot(threads, times, marker='o')
    plt.xlabel('Threads')
    plt.ylabel('Time (s)')
    plt.title('Execution Time')
    plt.grid(True)
    plt.show()
