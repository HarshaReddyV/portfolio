#include <stdio.h>
#include <stdlib.h>
#include<stdbool.h>
#include<stdint.h>

#define block_size 512
typedef uint8_t BYTE;

int main(int argc, char *argv[])
{
  if(argc != 2)
  {
      printf("usage recover ./card.raw\n");
      return 1;
  }

  FILE *infile = fopen(argv[1], "r");
  if(infile == NULL)
  {
      printf("file not found\n");
      return 1;
  }



  BYTE buffer[block_size];
  bool already_jpg;
  bool found_jpg;
  FILE *outfile;
  char filename[8];

  int counter = 0;


  while(fread(buffer,sizeof(BYTE),block_size,infile)|| feof(infile)==0)
  {

     if(buffer[0]==0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] * 0xf0 == 0xe0) )
     {
         found_jpg = true;
         if(already_jpg == false)
         {
             already_jpg = true;

         }
         else if(outfile != NULL)
         {
             fclose(outfile);
         }

         sprintf(filename,"%03i.jpg", counter);

         outfile = fopen(filename,"w");

         if(outfile == NULL)
         {
             return 1;
         }
         fwrite(buffer,sizeof(BYTE),1,outfile);
         counter++;

     }
     else if (already_jpg == true)
     {
          fwrite(buffer,sizeof(BYTE),1,outfile);
     }

  }


fclose(infile);
return 0;

}