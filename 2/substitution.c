#include<stdio.h>
#include<math.h>
#include<ctype.h>
#include<cs50.h>
#include<string.h>

int validate(string a);

int main(int argc, string argv[])
{
    if (argc != 2)
    {
        printf("Please enter 26 letter key after executing");
        return 1;
    }
    else if (validate(argv[1]) == 0)
    {
    }
    else
    {
        printf("Enter a valid key ..!!");
        return 1;
    }
    //validation is finsihed at this point

    //starting to take input

    string key = argv[1];
    string plain = get_string("plaintext:");

    printf("ciphertext:");

    //replacing the plain text to cipher text
    //replacing upper case to upper
    //replacing lower case to lower
    //replacing spaces as it is

    for (int e = 0, n = strlen(plain); e < n; e++)
    {
        if (isupper(plain[e]))
        {
            int z = plain[e] - 'A';
            if (isupper(key[z]))
            {
                printf("%c", key[z]);
            }
            else
            {

                printf("%c", toupper(key[z]));
            }
        }
        else if (islower(plain[e]))
        {
            int i = plain[e] - 'a';
            if (islower(key[i]))
            {
                printf("%c", key[i]);
            }
            else
            {

                printf("%c", tolower(key[i]));
            }
        }
        else
        {
            printf("%c", plain[e]);
        }

    }


//printing a new line as requested in assignment
//returing 0 value as requested
    printf("\n");
    return 0;


}


///Validating the input string for number and repeated characters

int validate(string a)
{
    if (strlen(a) == 26)
    {
        int i, n;

        for (i = 0, n = strlen(a); i < n; i++)
        {
            if (!isalpha(a[i]))
            {

                return 1;
            }
            else
            {
                if (isupper(a[i]))
                {
                    int p = a[i] - 'A';


                    for (int x = 0; x < n; x++)
                    {

                        int l = a[x] - 'A';

                        if (l == p)
                        {
                            if (i == x)
                            {

                            }
                            else
                            {
                                return 1;
                            }

                        }
                    }


                }
                else
                {
                    (islower(a[i]));
                }


                {

                    int q = a[i] - 'a';

                    for (int y = 0; y < n; y++)
                    {
                        int m = a[y] - 'A';

                        if (m == q)
                        {
                            if (i == y)
                            {

                            }
                            else
                            {
                                return 1;
                            }


                        }
                    }
                }
            }

        }
        return 0;
    }
    else
    {
        return 1;
    }
}



