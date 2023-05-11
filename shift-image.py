from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

if rank == 0:
    send_data = np.array(
        [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9,10,11,12],
        ]
    )

    recv_data = np.empty(4, dtype=int)
    comm.Scatter(send_data, recv_data, root=0)
else:
    send_data = None
    recv_data = np.empty(4, dtype=int)
    comm.Scatter(send_data, recv_data, root=0)

shifted_data = recv_data + 10

if rank == 0:
    final_data = np.empty([size, 4], dtype=int)
    comm.Gather(shifted_data, final_data, root=0)
else:
    final_data = None
    comm.Gather(shifted_data, final_data, root=0)

if rank == 0:
    print(final_data)