#include <mpi.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char *argv[])
{

    int rank, size, src;
    int tag = 42;
    MPI_Status status;

    MPI_Init(&argc, &argv);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);

    #define num 10000
    int message[num] = {0};
    int flag = 1;

    int sender, receiver;

    receiver = (rank + 1) % size;
    sender = (rank - 1 + size) % size;

    if (rank % 2 == 0)
    {
        MPI_Send(&message, num, MPI_INT, receiver, tag, MPI_COMM_WORLD);
        MPI_Recv(&message, num, MPI_INT, sender, tag, MPI_COMM_WORLD, MPI_STATUS_IGNORE);
        printf("Message reached node:\t %d \t from node :\t %d\n", receiver, sender);
    }

    else
    {
        MPI_Send(&message, num, MPI_INT, sender, tag, MPI_COMM_WORLD);
        MPI_Recv(&message, num, MPI_INT, receiver, tag, MPI_COMM_WORLD, MPI_STATUS_IGNORE);
        printf("Message reached node:\t %d \t from node :\t %d\n", receiver, sender);
    }

    MPI_Finalize();
    return 0;
}
