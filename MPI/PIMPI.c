#include <mpi.h>
#include <stdio.h>
#include <math.h>

int main(int argc, char *argv[]){
	
	double t1,t2;
	t1 = MPI_Wtime();

	int rank, size, root;
	root = 0;
	

	MPI_Init(&argc, &argv);
	MPI_Comm_rank (MPI_COMM_WORLD, &rank);
	MPI_Comm_size (MPI_COMM_WORLD, &size);	


	double xo, xend, h, x1, x2;
	
	xo = 0.0;
	xend = 1.0;
	h = 0.001;
	double range = (xend - xo) / size; 
	x1 = rank * range;
	x2 = (rank+1) * range;
	
	int n_steps = (int) ((x2 - x1) / h);
	double integral = 0.0;

	for (int i = 0; i <= n_steps-1; i++) {

		integral = integral + h / (1 + pow(x1 + h*i + h/2,2));
	
	}
	
	double resultbuf;

	MPI_Reduce(&integral, &resultbuf, 1, MPI_DOUBLE, MPI_SUM, root, MPI_COMM_WORLD);
	
	if (rank == 0){
	printf("integral value:\t %lf\n", 4*resultbuf);
	}

	MPI_Finalize();
	
	t2 = MPI_Wtime();
	printf("elapsed time:\t %lf\n", t2-t1);
	return 0;

}
