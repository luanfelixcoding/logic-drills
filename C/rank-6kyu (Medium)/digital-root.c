/*
Codewars Challenge: Digital Root
Rank: 6 kyu
URL: https://www.codewars.com/kata/541c8630095125aba6000c00
*/

#include <stdio.h>

int digital_root(int n){
    if(n < 10){
        return n;
    }

    int sum = 0;
    while(n > 0){
        sum += n % 10; // It gets the last number of n = 932 --> 2
        n /= 10; // It removes the last number of n = 932 --> n = 93
    }

    return digital_root(sum);
}

int main(){
    printf("Result: %d", digital_root(932)); // 5
    return 0;
}