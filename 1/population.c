#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // TODO: Prompt for start size

    int llamas, target, p, a;
    do
    {
        llamas = get_int("Enter number of llams:");
    }
    while (llamas < 9);
    // TODO: Prompt for end size

    do
    {
        target = get_int("Enter target count:");

    }
    while (target < llamas);
    // TODO: Calculate number of years until we reach threshold


    for (a = 0; llamas < target; a++)
    {
        llamas = llamas + (llamas / 3) - (llamas / 4);
    }




    // TODO: Print number of years
    {
        printf(" Years: %i\n", a);
    }

}