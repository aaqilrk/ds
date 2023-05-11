from mpi4py import MPI
import numpy as np
import time

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# create an array of n numbers on process 0
if rank == 0:
    array_to_share = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
    data_recv = np.empty(2, dtype=int)
    comm.Scatter(array_to_share, data_recv, root=0)
else:
    data_recv = np.empty(2, dtype=int)
    comm.Scatter(None, data_recv, root=0)

# find the partial sum on each process
partial_sum = data_recv.sum()

# print the partial sum on each process
print(f"Process {rank} received {data_recv} and partial sum {partial_sum}")

# reduce the partial sums to get the final sum
final_sum = comm.reduce(partial_sum, op=MPI.SUM, root=0)

# print the final sum on process 0
if rank == 0:
    time.sleep(2)
    print(f"Final sum: {final_sum}")