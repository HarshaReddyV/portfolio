#include<stdio.h>
#include<cs50.h>

int main(void)
{
    int i,a,p,j;
    do
    {
         i = get_int("Enter Height:");
    }
    while(i < 1);

     for(a=0;a<i;a++)
     {
        for(p=i-a; p>=0;p--)
        {
           printf(" ");


        }
        {
            for(j=a;j>=0;j--)
            {
               printf("#");

            }
            {
                printf("\n");
            }
        }

     }
}