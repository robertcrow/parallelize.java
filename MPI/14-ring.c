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
	int flag = 0;

	while (!flag) {

		proc1 = i % size - 1;

		if (rank == proc1){
			MPI_Send (&rank, 1, MPI_INT, proc2, tag, MPI_COMM_WORLD);
		}

		proc2 = proc1 + 1;

		if (rank == proc2){
			MPI_Recv (&rank, 1, MPI_INT, proc1, tag, MPI_COMM_WORLD, MPI_STATUS_IGNORE); 

		}

		i += 1;

		if (i >= 100){
			flag = 1;
			printf("ring communication timeout....\n");

		}


	}
	MPI_Finalize ();
	return 0;
}
