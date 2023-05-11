from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if rank == 0:
    array_to_share = [0, 1, 2, 3]
    data_recv =comm.scatter(array_to_share, root=0)
else:
    data_recv = comm.scatter(None, root=0)

print("Process", rank, "received", data_recv)