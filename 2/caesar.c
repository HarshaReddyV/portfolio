#include<cs50.h>
#include<stdlib.h>
#include<stdio.h>
#include<math.h>
#include<string.h>
#include<ctype.h>

int main(int k, string argv[ ])
{
    //validate the nummber of arguments given
    if ((k != 2) || !isdigit(*argv[1]))
    {
        printf("Usakjbxge:./caesar key");
        return 1;
    }

    int   key = atoi(argv[1]);
    float b = atof(argv[1]);

    //checking if the argument is a number and if not output
    if (key != b)
    {
        printf("Usage:./caesar key");
        return 1;
    }

    //getting input text
    string text = get_string("plaintext:");

    //printing cipher text
    printf("ciphertext:");
    for (int i = 0, n = strlen(text); i < n; i++)
    {

        if (isupper(text[i]))
        {
            int x = ((text[i] - 'A') + key) % 26 ;

            char p = 'A' + x;

            printf("%c", p);
        }
        else if (islower(text[i]))
        {
            int y = ((text[i] - 'a') + key) % 26;

            char q = 'a' + y;

            printf("%c", q);
        }
        else
        {
            printf("%c", text[i]);
        }
    }

    //printing new line at the end
    printf("\n");
    return 0;
}