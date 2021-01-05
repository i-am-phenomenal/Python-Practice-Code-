#include<stdio.h> 

int main()
{
    char *string = "this is a string";
    char input[1024] = { 0 };
    printf("%s", string);
    printf("\033[D");
    printf("\033[D");
    printf("\033[D");
    printf("\033[D");
    printf("\033[D");
    fgets(input, 1024, stdin);
    return 0;
}