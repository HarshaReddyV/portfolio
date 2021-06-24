#include<stdio.h>
#include<cs50.h>

int main(void)
{
    long i, b;
    int y, x, z, l, a,d,c, sum1, sum2;
    sum2 = 0;
    sum1 = 0;

    do
    {
      i = get_long("Enter Card Number:");
    }
    while (i < 0);
    b = i;

    for ( x = 0; i != 0; x++)
   {
        y = i % 10;
        i = i/10;


        if (x % 2 == 0)
        {
            sum1 = sum1 + y;



        }
        else
        {

            y = y * 2;
            if(y >= 10)
            {
               for(z = 0; y > 0; z++)
               {
                   l = y % 10;
                   y = y / 10;
                   sum2 = sum2 + l;
               }
               {


               }
           }

           else
           {
               sum2 = sum2 + y;
           }

        }

   }
   {
    a = sum1 + sum2;




        if ( a % 10 == 0)
        {

           for( d = 1; b > 99; d++)
           {
             c = b % 10;
             b =  b / 10;



           }
           {


              if(b == 34 || b == 37)
              {
                 if(d == 14)
                 {
                     printf("AMEX\n");
                 }
                 else
                 {
                    printf("INVALID\n");
                 }

              }
              else if(b >= 51 && b <= 55)
              {
                  if(d == 15)
                  {
                     printf("MASTERCARD\n");
                  }
                  else
                  {
                     printf("INVALID\n");
                  }

              }
              else if(b >= 40 && b <= 49)
              {
                if(d == 12 || d == 15)
                {
                    printf("VISA\n");
                }
                else
                {
                   printf("INVALID\n");
                }

              }
              else
              {
                 printf("INVALID\n");
              }
            }
         }
        else
        {

          printf("INVALID\n");
        }
   }
}