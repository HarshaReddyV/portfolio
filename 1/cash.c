#include<stdio.h>
#include<math.h>
#include<cs50.h>

int main(void)
{
    float i;
    int a, x, p, y, z, s;
    do
    {
        i = get_float("Enter Amount-$:");
    }
    while (i < 0);
    //rounding to cents

    a = round(i * 100);

    //counting the no. of coins

    for (x = 0; 25 <= a; x++)
    {
        //counting 25 cents

        a = a - 25;

    }
    {
        //counting 10 cents

        for (y = 0; 10 <= a; y++)
        {
            a = a - 10;


        }
        {
            //counting 5 cents

            for (z = 0; 5 <= a; z++)
            {
                a = a - 5;

            }

            {
                //counting 1 cents

                for (p = 0; 1 <= a; p++)
                {
                    a = a - 1;


                }

                {
                    //adding all coins

                    s = x + y + z + p;

                    //printing the no. of coins

                    printf("%i\n", s);

                }

            }


        }

    }

}
