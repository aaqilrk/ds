from mpi4py import MPI 

comm=MPI.COMM_WORLD
rank = comm.rank

print("my rank is : " , rank) 

if rank==0:
    data_send= "a"
    destination_process = 1
    source_process = 1

    data_received=comm.recv(source=source_process) 
    comm.send(data_send,dest=destination_process)

    print("sending data", data_send, "to process", destination_process) 
    print("data received is", data_received)

if rank==1:
    data_send= "b"
    destination_process = 0
    source_process = 0 
    
    comm.send(data_send,dest=destination_process) 
    data_received=comm.recv(source=source_process)

    print("sending data is", data_send, "to process", destination_process)
    print("data received is", data_received)