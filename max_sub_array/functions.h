#ifndef FUNCTIONS_H
#define FUNCTIONS_H

#include <random>
#include <vector>
#include <iostream>
#include <bits/stdc++.h>

#include "naive.h"
#include "divide_conquer.h"
#include "kadane.h"

using namespace std;

void write_in_csv(int n, vector<float> &naive,vector<float> &divide,vector<float> &kadane){
    ofstream file;
    file.open ("times.csv",ios::out);
    file<<"n_elements,Naive,Divide,Kadane\n";
    for (int i = 0; i < n; i++){
        file<<(i+1)*5<<","<<naive[i]<<","<<divide[i]<<","<<kadane[i]<<'\n';
    }
    file.close();
}

vector<float> naive_kadane_tests(int n_test,int **array,int (*func)(int, int [])){
    vector<float> times;
    for (int i = 0;i < n_test;i++){
        auto start = chrono::high_resolution_clock::now();
    
        // unsync the I/O of C and C++.
        ios_base::sync_with_stdio(false);
        func(i*5,array[i]);
        auto end = chrono::high_resolution_clock::now();
        double time_taken = 
            chrono::duration_cast<chrono::nanoseconds>(end - start).count();
    
        time_taken *= 1e-9;
        times.push_back(time_taken);
    }
    return times;
}


vector<float> divide_tests(int n_test,int **array,int (*func)(int [],int, int)){
    vector<float> times;
    for (int i = 0;i < n_test;i++){
        auto start = chrono::high_resolution_clock::now();
    
        // unsync the I/O of C and C++.
        ios_base::sync_with_stdio(false);
        func(array[i], 0, i * 5);
        auto end = chrono::high_resolution_clock::now();
        double time_taken = 
            chrono::duration_cast<chrono::nanoseconds>(end - start).count();
    
        time_taken *= 1e-9;
        times.push_back(time_taken);
    }
    return times;
}

void randomize_array(int n,int array[]){
    std::random_device rd;  //Will be used to obtain a seed for the random number engine
    std::mt19937 gen(rd()); //Standard mersenne_twister_engine seeded with rd()
    std::uniform_int_distribution<> distrib(-10, 10);
    for (int i = 0; i < n; i++){
        array[i] = distrib(gen);
    }
}

void testing(int n_test = 10){
    int **array;
    array = new int * [n_test]; 
    for (int i = 0; i < n_test; i++){
        array[i] = new int[i*5];
        randomize_array(i*5, array[i]);
    }
    auto naive_times = naive_kadane_tests(n_test,array,&naive);
    auto divide_times = divide_tests(n_test,array,&divide_conquer);
    auto kadane_times = naive_kadane_tests(n_test,array,&kadane);
    write_in_csv(n_test, naive_times,divide_times,kadane_times);

    for (int i = 0; i < n_test ; i++) delete array[i];
    delete [] array;
}

#endif // !FUNCTIONS_H
