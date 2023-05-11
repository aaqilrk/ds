from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if rank == 0:
    data = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9,10,11,12],
    ]
    recv_data = comm.scatter(data, root=0)
else:
    data = None
    recv_data = comm.scatter(data, root=0)

partial_sum = sum(recv_data)
print("rank: ", rank, " partial_sum: ", partial_sum)

if rank == 0:
    final_sum = comm.reduce(partial_sum, op=MPI.SUM, root=0)
    print("final_sum: ", final_sum)
else:
    comm.reduce(partial_sum, op=MPI.SUM, root=0)