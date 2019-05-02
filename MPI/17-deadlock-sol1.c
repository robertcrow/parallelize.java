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
	int previous = (rank - 1 + size) % size;
	
	#define elems 100000
	MPI_Datatype type = MPI_INT;
	int toSend[elems] = {};
	int toRecv[elems];

	printf ("Rank %d/%d, sending\n", rank, size);
	MPI_Isend (&toSend, elems, MPI_INT, next, 0, MPI_COMM_WORLD, &request);
	printf ("Rank %d/%d, receiving\n", rank, size);
	MPI_Irecv (&toRecv, elems, MPI_INT, previous, 0, MPI_COMM_WORLD, &request);
	printf ("Message reached node:\t %d \t from node :\t %d\n", next, previous);

	MPI_Finalize();
	return 0;

}
