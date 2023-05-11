from mpi4py import MPI 

comm = MPI.COMM_WORLD 
rank = comm.Get_rank() 

if rank == 0:
    variable_to_share = 100
    variable_recv = comm.bcast(variable_to_share, root=0)
else:
    variable_recv = comm.
bcast(None, root=0)

print("process = %d" %rank + " variable received = %d " %variable_recv)