from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

n = 5

if rank == 0:
    for ele in range(1, n+1):
        req = comm.isend(ele, dest=1)
        req.wait()
        print("Process 0 sent element ", ele)
    req = comm.irecv(source=1)
    fact = req.wait()
    print("Factorial of ", n, " is ", fact)

    
elif rank == 1:
    fact = 1
    for ele in range(n):
        req = comm.irecv(source=0)
        fact = fact * req.wait()

    req = comm.isend(fact, dest=0)
    req.wait()