#ifndef DIVIDE_CONQUER_H
#define DIVIDE_CONQUER_H


int divide_conquer_cross(int array[], int low, int mid, int high){
    int left_sum = INT_MIN;
    int sum = 0;

    for (int i = mid; i >= low; i--){
        sum = sum + array[i];
        if (sum > left_sum){
            left_sum = sum;
        }
    }

    int right_sum = INT_MIN;
    sum = 0;

    for (int i = mid +1 ; i <= high; i++){
        sum = sum + array[i];
        if (sum > right_sum){
            right_sum = sum;
        }
    }
    return left_sum + right_sum;
}

int divide_conquer(int array[], int low, int high){
    if (high == low) return array[low];
    int mid = (low + high)/2;
    int left_sum = divide_conquer(array, low, mid);
    int right_sum = divide_conquer(array, mid + 1, high);
    int cross_sum = divide_conquer_cross(array, low, mid, high);

    if (left_sum >= right_sum && left_sum >= cross_sum)
        return left_sum;
    else if (right_sum >= left_sum && right_sum >= cross_sum)
        return right_sum;
    else 
        return cross_sum;

}

#endif // !DIVIDE_CONQUER_H