#include <mpi.h>
#include <stdio.h>
#include <math.h>

int main(int argc, char *argv[]){
	
	double t1,t2;
	t1 = MPI_Wtime();
	double xo, xend, h;
	xo = 0.0;
	xend = 1.0;
	h = 0.001;
	double n_steps = (xend - xo) / h;
	double integral = 0.0;
	for (int i = 0; i <= (int) n_steps; i++) {
		
		printf("%i\n", i);
		integral = integral + h / (1 + pow(xo + h*i + h/2,2));
	
	}

	printf("integral value:\t %lf\n", 4*integral);
	//int rank, size;
	//MPI_Init (&argc, &argv);
	//MPI_Comm_rank (MPI_COMM_WORLD, &rank);
	//MPI_Comm_size (MPI_COMM_WORLD, &size);
	//printf("size:\t%i,\t rank:\t%i\n", size, rank);
	//MPI_Finalize();
	t2 = MPI_Wtime();
	printf("elapsed time:\t %lf\n", t2-t1);
	return 0;

}
