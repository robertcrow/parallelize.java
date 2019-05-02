#include <stdio.h>
#include <mpi.h>

int main (int argc, char *argv[]) {

	int rank_world;
	MPI_Comm cart;
	MPI_Init (&argc, &argv);
	MPI_Comm_rank (MPI_COMM_WORLD, &rank_world);

	int dims[] = { 3, 3 };
	int periods[] = { 1, 1 };
	MPI_Cart_create (MPI_COMM_WORLD, 2, dims, periods, 0, &cart);
	int rank;
	MPI_Comm_rank (cart, &rank);

	int coords[2];
    int m1[3][3] = {1,2,3,4,5,6,7,8,9};
    int m2[3][3] = {10,20,30,40,50,60,70,80,90};
    int current_node = 0;
	int left_node = 0;
    int o[3][3] = {0};

    // preprocessing - rearranging matrices' elements

    for (int i = 1; i <= (dims[1]-1); i++){

        for (int j = dims[1] - i - 1; j < dims[1]; j++) {

            current_node = i + (j - 1) * dims[0];
            left_node = current_node - j * dims[0];    
            int computed;
			int dest, src;
            MPI_Cart_rank (cart, coords, &computed);
            MPI_Cart_shift ( cart, 2, -i, &src, &dest);

            if (rank == 0 ) {
                printf("%d\t%d\n", src, dest);
            }
                 
            /*
            m1[i,j] = dest;

            MPI_Cart_shift ( cart, 2, -(j - 1), &src, &dest);

            m2[j,1] = dest;
            */

        }

    }

    //printf("first and last elem of m1:\t %d\t%d\n", m1[0], m1[8] );
    //printf("first and last elem of m2:\t %d\t%d\n", m2[0], m2[8] );


	MPI_Comm_free (&cart);
	MPI_Finalize();	
	return 0;
}
