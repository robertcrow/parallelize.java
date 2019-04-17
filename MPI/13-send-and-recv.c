#include <mpi.h>
#include <stdio.h>
#include <math.h>

int main(int argc, char *argv[]){
	
	int rank, size, root;
	root = 0;
	int tag = 100;
 	
	MPI_Init(&argc, &argv);
	MPI_Comm_rank (MPI_COMM_WORLD, &rank);
	MPI_Comm_size (MPI_COMM_WORLD, &size);	
	MPI_Request request;
	// setting-up the 0 node
	double integral = 0.0;
	double bucket[size-1];

	if (rank == 0) {
		for (int i = 0; i < size; i++){
			MPI_Irecv(&bucket[i], 1, MPI_DOUBLE, i, 100, MPI_COMM_WORLD, &request);
		}
	}
	

	printf("Irecv completed\n");
	// main integration loop
		
	double xo;
	double xend;
	double h;
	double x1;
	double x2;
        xo = 0.0;
        xend = 1.0;
        h = 0.001;

        double range = (xend - xo) / size; 
        x1 = rank * range;
        x2 = (rank + 1) * range;
        int n_steps = (int) ((x2 - x1) / h);

        for (int i = 0; i <= n_steps-1; i++) {

                integral = integral + h / (1 + pow(x1 + h*i + h/2,2));

        }
	
	printf("for loop completed on node\n");

	if (rank != 0) {
		MPI_Isend(&integral, 1, MPI_DOUBLE, 0, tag, MPI_COMM_WORLD, &request);
	}

	printf("sending completed\n");

	if (rank == 0){
		MPI_Wait(&request, MPI_STATUS_IGNORE);
		double score = integral;
		for (int k = 1; k < size; k++){
			score += bucket[k];
		}
		printf("pi value: \t%lf\n", 4 * score);
	}

	MPI_Finalize();
	
	return 0;

}
