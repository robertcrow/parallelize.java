#include <mpi.h>
#include <stdio.h>
#include <string.h>
int main (int argc, char *argv[]) {
	int rank, size, src;
	char message[50];
	int tag = 42;
	MPI_Status status;

	MPI_Init (&argc, &argv);
	MPI_Comm_rank (MPI_COMM_WORLD, &rank);
	MPI_Comm_size (MPI_COMM_WORLD, &size);

	for (int i = 1; i < size; i++) {
		if (i == rank) {
			printf("Size:%d, rank:%d\n", size, rank);
		}
		MPI_BARRIER(MPI_COMM_WORLD);
	}
			
	MPI_Finalize ();
	return 0;
}
