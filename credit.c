#include<stdio.h>
#include<cs50.h>

int main(void)
{
   long i,b;
   int y, x, z, l, a,d,c, sum1, sum2;
   sum2=0;
   sum1=0;

   do
   {
      i = get_long( "Enter Card Number:" );
   }
   while (i < 0);
   b=i;

   for(x=0;i!=0;x++)
   {
      y=i % 10;
      i=i/10;

      if(x%2==0)
      {
        sum1 = sum1 + y;


      }
      else
      {

        y = y * 2;
        if(y > 10)
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
    a = sum1+sum2;

        if(a%10==0)
        {

           for(d=0;b>=9;d++)
           {
             c = b%10;
             b =  b / 10;



           }
           {

              if(b==3)
              {
                 printf("AMEX\n");
              }
              else if(b==5)
              {
                printf("MASTERCARD\n");
              }
              else if(b==4)
              {
                printf("VISA\n");
              }
            }
         }
        else
        {

          printf("INVALID\n");
        }
}