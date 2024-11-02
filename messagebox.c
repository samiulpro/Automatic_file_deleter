#include <stdio.h>
#include <windows.h>

int messagebox(char *file){
    int r;
    r = MessageBoxA(NULL,file,"BOOK handler",MB_OKCANCEL);
    return r;
}