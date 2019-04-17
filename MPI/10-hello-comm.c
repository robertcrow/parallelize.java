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

	if (rank != 0) {
		//sprintf (message, "%d\n", rank);
		//MPI_Send (&rank, 1, MPI_INT, 0, tag, MPI_COMM_WORLD); /* dlaczego strlen + 1? */
		int tmp3 = 1;
		MPI_Send(&tmp3,1,MPI_INT, 0 , tag, MPI_COMM_WORLD);
	} else {
		int tmp = 100;
		int tmp2 = 0;
		for (int src = 1; src < size; src++) {
			MPI_Recv (&message, 1, MPI_INT, MPI_ANY_SOURCE, tag, MPI_COMM_WORLD, &status);
			/*MPI_Recv (message, 50, MPI_CHAR, src, tag, MPI_COMM_WORLD, MPI_STATUS_IGNORE); */
			
			tmp2 = tmp2 + message;
		}
		tmp2 = tmp2 + tmp;
		printf("total output:\t%i \n", tmp2);

		
	}		
	MPI_Finalize ();
	return 0;
}
