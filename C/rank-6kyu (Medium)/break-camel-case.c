/*
Codewars Challenge: Break camelCase
Rank: 6 kyu
URL: https://www.codewars.com/kata/5208f99aee097e6552000148
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

//returned buffer should be dynamically allocated and will be freed by a caller
char* solution(const char *camelCase) {
    if (camelCase == NULL) return NULL;
    
    int len = strlen(camelCase);
    int upper_count = 0;
    
    for(int i = 0; i < len; i++){
        if(isupper(camelCase[i])){
            upper_count++;
        }
    }
    
    char *result = (char *)malloc(len + upper_count + 1);
    
    if(result == NULL) return NULL;
    
    int j = 0;
    for(int i = 0; i < len; i++){
        if(isupper(camelCase[i])){
            result[j++] = ' ';
        }
        result[j++] = camelCase[i];
    }
    result[j] = '\0';
    
    return result;
}

int main(){
    printf("%s\n", solution("camelCase")); // camel Case
    printf("%s\n", solution("giveMeAStar")); // give Me A Star
    return 0;
}

