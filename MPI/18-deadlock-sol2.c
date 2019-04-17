#include <mpi.h>
#include <stdio.h>
#include <stdlib.h>
int main (int argc, char **argv) {

	MPI_Init (&argc, &argv);
	int rank, size;
	MPI_Comm_rank (MPI_COMM_WORLD, &rank);
	MPI_Comm_size (MPI_COMM_WORLD, &size);
    MPI_Request request;

	int next = (rank + 1) % size;
	int previous = (rank -1 + size) % size;
    int tag = 42; 
	
	#define elems 100000
	MPI_Datatype type = MPI_INT;
	int toSend[elems] = {};
	int toRecv[elems];

	
    MPI_Sendrecv(&toSend, elems, MPI_INT, next, tag, &toRecv, 
    elems, MPI_INT, previous, tag, MPI_COMM_WORLD, MPI_STATUS_IGNORE);
    
    printf ("Node:\t %d \t received message from node :\t %d \t and sent message to \t%d\n",
    rank, previous, next);
	MPI_Finalize();
	return 0;

}
