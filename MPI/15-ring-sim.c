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

	int i = 0;
	int proc1, proc2;
	int flag = 1;

	printf("%d\n", size);
	int sender, receiver;
	receiver = (rank + 1) % size;
	sender = (rank -1 + size) % size;
		MPI_Send (&rank, 1, MPI_INT, receiver, tag, MPI_COMM_WORLD);
		MPI_Recv (&rank, 1, MPI_INT, sender, tag, MPI_COMM_WORLD, MPI_STATUS_IGNORE);

		//i += 1;

		//if (i >= 10) {
		//	printf("communication timeout.....\n");
		//	;
		//}
	



	MPI_Finalize ();
	return 0;
}
