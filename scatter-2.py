from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if rank == 0:
    array_to_share = np.array([0, 1, 2, 3, 4, 5, 6, 7])
    data_recv = np.empty(2, dtype=int)
    comm.Scatter(array_to_share, data_recv, root=0)
else:
    data_recv = np.empty(2, dtype=int)
    comm.Scatter(None, data_recv, root=0)

print("Process", rank, "received", data_recv)