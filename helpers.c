#include "helpers.h"
#include <math.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{

    for(int i=0;i< height;i++)
    {
        for(int j=0;j<width;j++)
        {
            float x = (image[i][j].rgbtBlue + image[i][j].rgbtRed + image[i][j].rgbtGreen)/ 3.00;

            int p = round(x);

            image[i][j].rgbtBlue = p;
            image[i][j].rgbtRed = p;
            image[i][j].rgbtGreen = p;

        }
    }


    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    return;
}
