#ifndef NAIVE_H
#define NAIVE_H

#include <limits.h>

int naive(int size,int array[]){
    int max_sum = INT_MIN;
    for (int i = 0; i < size; i++){
        int current_sum = 0;
        for (int j = i; j < size; j++){
            current_sum += array[j];
            if (current_sum > max_sum){
                max_sum = current_sum; 
            }
        }
    }
    return max_sum;
}

#endif // !NAIVE_H
