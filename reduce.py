from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

# Define the data to be reduced
data = rank * 2

# Reduce the data using the sum operation
result = comm.reduce(data, op=MPI.SUM, root=0)

# Print the result
if rank == 0:
    print("Result of reduction:", result)