#include <stdio.h>
#include <stdlib.h>
#include<stdint.h>
#include<cs50.h>
#include<stdbool.h>

#define FILE_NAME_SIZE 8



int main(int argc, char *argv[])
{

   if(argc != 2)
   {
       printf("usage: ./recover image.raw");
       return 1;
   }

    typedef uint8_t BYTE;
    const int block_size = 512;
    BYTE buffer[block_size];
    size_t bytes_read;
    bool is_first_jpg = false;
    FILE *current_file;
    char filename[100];
    int current_file_number = 0;
    bool found_jpg = false;

    FILE *infile = fopen(argv[1],"r");
    if (infile == NULL)
    {
        printf("Could not open file.\n");
        return 1;
    }

    //checking jpg type
    while(true)
    {
        bytes_read = fread(buffer,sizeof(BYTE),block_size,infile);

        if(bytes_read == 0)
        {
            break;
        }

         if(buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3]*0xf0) == 0xe0 )
         {
             found_jpg = true;
             if(!is_first_jpg)
             {
                 is_first_jpg = true;
             }
             else
             {
                 fclose(current_file);

             }
             sprintf(filename , "%03i",current_file_number);
             current_file = fopen(filename,"w");

               fwrite(buffer,sizeof(BYTE),block_size,current_file);
             current_file_number++;

         }
         else
         {
            if(found_jpg)
            {
                fwrite(buffer,sizeof(BYTE),block_size,current_file);
            }
         }


    }




fclose(infile);
fclose(current_file);
return 0;


}

