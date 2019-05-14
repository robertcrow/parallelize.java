#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <omp.h>


void main(){
    
    int tmp;
    
    #pragma omp parallel 
    {tmp = omp_get_num_threads();}

    int dim_size[2];
    dim_size[0] = 100 * tmp;
    dim_size[1] = 100 * tmp;

    double *arr = (double *)malloc(dim_size[0] * dim_size[1] * sizeof(double));

    // writing valuer off arr

    int offset = 1;

    arr[0] = -2.0;
    arr[1] = 1.0;
    arr[dim_size[0] * dim_size[1] -1] = -2.0;
    arr[dim_size[0] * dim_size[1] -2] = 1.0;


    #pragma omp for 
    for(int i = 1; i < dim_size[0]-1; i++ ){
        arr[dim_size[0] * i + offset] = -2.0;
        arr[dim_size[0] * i + offset - 1] = 1.0; // left
        arr[dim_size[0] * i + offset + 1] = 1.0; // right
    }

    double *b = (double *)malloc(dim_size[0] * sizeof(double));
    double tmp4 = 0.0;
    #pragma omp for
    for(int i = 0; i < dim_size[0]; i++ ){
        b[i] = sin((M_PI * i) / omp_get_thread_num());
        tmp4 += b[i];
    }







    double tmp3 = 0.0;
    for(int i = 0; i < dim_size[0] * dim_size[1]; i++ ){
        tmp3 += arr[i];
    }
    
    printf("sum:\t%lf\n", tmp4);
    
    for(int i = 0; i < dim_size[0]; i++ ){
        for(int j = 0; j < dim_size[1]; j++){
 

            

        }


        
    }
    // #pragma omp parallel shared()
    
    // {   

    //     int tmp = omp_get_num_threads();
    //     printf("%d", tmp);
    //     int tmp1 = 1;
    //     int tmp2 = 1;

    //     int n_threads = omp_get_num_threads();
    //     int thread = omp_get_thread_num();

    //     // for(int i=1; i<N; i++){

    //     // }   

    // }

}