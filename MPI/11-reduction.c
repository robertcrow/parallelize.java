#include <mpi.h>
#include <stdio.h>
#include <string.h>
int main (int argc, char *argv[]) {
	int rank, size, src;
	int message;
	int tag = 42;
	MPI_Status status;

	MPI_Init (&argc, &argv);
	MPI_Comm_rank (MPI_COMM_WORLD, &rank);
	MPI_Comm_size (MPI_COMM_WORLD, &size);

	int inbuf, resultbuf;
	int root = 0;

	inbuf = rank;
	
	MPI_Reduce( &inbuf, &resultbuf, 1, MPI_INT, MPI_SUM, root, MPI_COMM_WORLD);
	if (rank == 0){
	printf("output:\t%i\n", resultbuf);
	}

	MPI_Finalize ();
	return 0;
}
