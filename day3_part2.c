#include <stdio.h>
#include <string.h>

int main(int argc, char** argv) {
    FILE *fin = fopen("day3_in.txt","r");
    int pos1 = 0, pos2 = 0, pos3 = 0, pos4 = 0, pos5 = 0;
    long cnt1 = 0, cnt2 = 0, cnt3 = 0, cnt4 = 0, cnt5 = 0;
    char currLine[32], *n;
    int lineCnt = 1;
    
    fgets(currLine, 32, fin);
    fgetc(fin);
    while ((n = fgets(currLine, 32, fin)) != NULL) {
        pos1 = (pos1+1) % 31;
        pos2 = (pos2+3) % 31;
        pos3 = (pos3+5) % 31;
        pos4 = (pos4+7) % 31;
        if (lineCnt % 2 == 0) pos5 = (pos5+1) % 31;
        if (currLine[pos1] == '#') cnt1++;
        if (currLine[pos2] == '#') cnt2++;
        if (currLine[pos3] == '#') cnt3++;
        if (currLine[pos4] == '#') cnt4++;
        if (lineCnt % 2 == 0 && currLine[pos5] == '#') cnt5++;
        fgetc(fin);
        lineCnt++;
    }
    fclose(fin);
    printf("cnt: %lu, %lu, %lu, %lu, %lu => %lu\n", cnt1, cnt2, cnt3, cnt4, cnt5, (cnt1*cnt2*cnt3*cnt4*cnt5));
}
