/*
Codewars Challenge: Break camelCase
Rank: 5 kyu
URL: https://www.codewars.com/kata/52597aa56021e91c93000cb0
*/

#include <stdio.h>
#include <stddef.h>

void move_zeros(size_t len, int arr[len])
{
    size_t idx = 0;
    
    // mutate arr in place
    for (size_t i = 0; i < len; i++) {
        if (arr[i] != 0) {
            arr[idx] = arr[i];
            idx++;
        }
    }
    
    for (size_t i = idx; i < len; i++) {
        arr[i] = 0;
    }
}

int main(){

}