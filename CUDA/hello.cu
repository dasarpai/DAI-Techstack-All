// hello.cu
#include <stdio.h>

__global__ void hello_cuda() {
    printf("Hello, CUDA World from GPU!\n");
}

int main() {
    // Launch the kernel with one block and one thread
    hello_cuda<<<1, 1>>>();

    // Wait for GPU to finish before accessing on host
    cudaDeviceSynchronize();

    printf("Hello, CUDA World from CPU!\n");
    return 0;
}

