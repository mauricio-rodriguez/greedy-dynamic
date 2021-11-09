#ifndef KADANE_H
#define KADANE_H

#include <bits/stdc++.h>

int kadane(int size, int array[]){
    int current_sum = 0;
    int max_sum = INT_MIN;
    for (int i = 0; i < size; i++){
        if (array[i] > array[i] + current_sum){
            current_sum = array[i];
        }
        else current_sum += array[i];
        if (current_sum > max_sum)
            max_sum = current_sum; 
    }
    return max_sum;
}

#endif // !KADANE_H
