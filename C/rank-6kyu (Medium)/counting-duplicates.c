/*
Codewars Challenge: Counting Duplicates
Rank: 6 kyu
URL: https://www.codewars.com/kata/54bf1c2cd5b56cc47f0007a1
*/

#include <stdio.h>
#include <string.h>
#include <ctype.h>

int count_duplicates(const char* text){
    int counts[128] = {0}; // all 128 ASCII characters, that's why 128
    int duplicates = 0;
    
    for(int i = 0; text[i] != '\0'; i++){
        char c = tolower((unsigned char)text[i]);
        counts[(int)c]++;
    }
    
    for(int i = 0; i < 128; i++){
        //printf("%d", counts[i]); // it'll show each character counting
        if(counts[i] > 1){
            duplicates++;
        }
    }
    return duplicates;
}

int main()
{
    printf("%d", count_duplicates("aabBcde")); // 2, letters 'a' and 'b' ('B' and 'b')

    return 0;
}