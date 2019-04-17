#include <mpi.h>
#include <stdio.h>
#include <math.h>

int main(int argc, char *argv[]){
	
	int rank, size, root;
	root = 0;

	int tag = 100; 
	int message = 0;
	
	MPI_Init(&argc, &argv);
	MPI_Comm_rank (MPI_COMM_WORLD, &rank);
	MPI_Comm_size (MPI_COMM_WORLD, &size);	
	
	printf("program initialized on core:\t%d\n", rank);

	if (rank == 0){
		MPI_Send(&rank, 1, MPI_INT, 1, tag, MPI_COMM_WORLD);
		MPI_Recv(&message, 1, MPI_INT, 1, tag, MPI_COMM_WORLD, MPI_STATUS_IGNORE);	
	} else if (rank == 1) {
		MPI_Send(&rank, 1, MPI_INT, 0, tag, MPI_COMM_WORLD);
		//MPI_Ssend(&rank, 1, MPI_INT, 0, tag, MPI_COMM_WORLD); // solution no1
		MPI_Recv(&message, 1, MPI_INT, 0, tag, MPI_COMM_WORLD, MPI_STATUS_IGNORE);
		//MPI_Send(&rank, 1, MPI_INT, 0, tag, MPI_COMM_WORLD);  // solution no2

	}

	MPI_Finalize();
	
	printf("status of core%d: finished\n", rank);
	return 0;

}
