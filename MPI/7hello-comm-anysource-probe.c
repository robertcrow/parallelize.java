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

	if (rank != 0) {
		sprintf (message, "Hello, I am thread %d\n", rank);
		MPI_Send (message, strlen(message) + 1, MPI_CHAR, 0, tag, MPI_COMM_WORLD); /* dlaczego strlen + 1? */
	} else {
		for (int no = 1; no < size; no++) {
			MPI_Probe (MPI_ANY_SOURCE, MPI_ANY_TAG, MPI_COMM_WORLD, &status);
			printf ("Receiving message from process %d with tag %d\n", status.MPI_SOURCE, status.MPI_TAG);
			MPI_Recv (message, 50, MPI_CHAR, MPI_ANY_SOURCE, MPI_ANY_TAG, MPI_COMM_WORLD, MPI_STATUS_IGNORE); 
			printf ("%s", message);
		}
	}		
	MPI_Finalize ();
	return 0;
}
