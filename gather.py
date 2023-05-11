from mpi4py import MPI

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

data = comm.gather(rank**2, root=0) 

if rank == 0:
    for i in range(size):
        print(" process %s receiving %s from process %s" %(rank , data[i] , i))