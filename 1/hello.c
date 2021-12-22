#include<stdio.h>
#include<cs50.h>

int main(void)
{
    //asking for name
    string Name = get_string(" What is your Name?\n");
    //displaying name
    printf("hello,%s\n", Name);
}