#include<stdio.h>
#include<cs50.h>

int main(void)
{
    int i, a, p, j;
    do
    {
        i = get_int("Enter Height:");
    }
    while (i < 1 || i > 8);

    for (a = 0 ; a < i ; a++)
    {
        //inserting spaces to create space
        for (p = i - a ; p > 1 ; p--)
        {
            printf(" ");
        }
        {
            //insering hashes incrementally on vertical axis
            for (j = a; j >= 0; j--)
            {
                printf("#");

            }
            {
                printf("  ");
                for (j = a; j >= 0; j--)
            {
                printf("#");

            }
            {
                printf("\n");
            }
            }
        }
    }
    {}
}