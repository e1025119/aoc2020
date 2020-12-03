#include <stdio.h>
#include <string.h>

int main(int argc, char** argv) {
    FILE *fin = fopen("day3_in.txt","r");
    int pos = 0, cnt = 0;
    char currLine[32], *n;
    fgets(currLine, 32, fin);
    fgetc(fin);
    while ((n = fgets(currLine, 32, fin)) != NULL) {
        pos = (pos+3) % 31;
        if (currLine[pos] == '#') cnt++;
        //printf("currLine: %s, pos: %c\n", currLine, currLine[pos]);
        fgetc(fin);
    }
    printf("cnt: %d\n", cnt);
    fclose(fin);
}
