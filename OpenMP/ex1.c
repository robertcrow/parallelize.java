#include <stdio.h>
#include <omp.h>

#define N 6

void main(){

    #pragma omp parallel
    
    {   
        int tmp1 = 1;
        int tmp2 = 1;

        int n_threads = omp_get_num_threads();
        int thread = omp_get_thread_num();

        for(int i=1; i<N; i++){
            tmp1 *= i;
            tmp2 *= 2*i;    
            printf("thread %d/%d:\t%d\t%d\n", thread+1, n_threads, tmp1, tmp2);
        }   

    }

}