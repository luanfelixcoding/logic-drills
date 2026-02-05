/*
Codewars Challenge: Take a Ten Minutes Walk
Rank: 6 kyu
URL: https://www.codewars.com/kata/54da539698b8a2ad76000228
*/

#include <stdio.h>
#include <stdbool.h>
#include <string.h>

// input is a null-terminated string
bool isValidWalk(const char *walk) {
    if (strlen(walk) != 10) {
        return false;
    }
    
    int x = 0; // east and west
    int y = 0; // north and south
    
    for(int i = 0; walk[i] != '\0'; i++){
        if (walk[i] == 'n') y++;
        else if (walk[i] == 's') y--;
        else if (walk[i] == 'w') x++;
        else x--;
    }
    
    return (x == 0 && y == 0);
}

int main(){
    char input[11] = "nsnsnsnsns"; // true
    char input_2[11] = "nwewnnnsns"; // false
    printf("%d\n", isValidWalk(input));
    printf("%d\n", isValidWalk(input_2));
    return 0;
}