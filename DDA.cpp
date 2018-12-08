/*
By: Pravesh Gaire

Title:
Digital Differential Analyzer (DDA) - Line Generation Algorithm

Theory:
In any 2-Dimensional plane if we connect two points (x0, y0) and (x1, y1), we get a line segment. But in the case of computer graphics we can not directly join any two coordinate points, for that we should calculate intermediate point’s coordinate and put a pixel for each intermediate point, of the desired color with help of functions like putpixel(x, y, K) in C, where (x,y) is our co-ordinate and K denotes some color.
Examples:
Input: For line segment between (2, 2) and (6, 6) :
we need (3, 3) (4, 4) and (5, 5) as our intermediate
points.
Input: For line segment between (0, 2) and (0, 6) :
we need (0, 3) (0, 4) and (0, 5) as our intermediate
points.

Algorithm:
step 1: Get one point as (X0, Y0) and second point of line as (X1, Y1) 
step 2: Calculate difference between two end points
dx = X1 - X0
dy = Y1 - Y0
step 3: calculate the number of steps to put pixel
steps = abs(dx) > abs(dy) ? abs(dx) : abs(dy)
step 4: calculate the increment in x and y axis
Xinc = dx / steps
Yinc = dy / steps
step 5: put the pixel in each coordinates
X, Y = X0, Y0
for (i=0; i<=steps; i++)
{
    putpixel(X,Y, white)
    X += Xinc
    Y += Yinc
}
*/

#include<iostream>
#include<cmath>

void DDA(int X0, int Y0, int X1, int Y1){
    int dx = X1 - X0;
    int dy = Y1 - Y0;
    
    int steps = abs(dx) > abs(dy) ? abs(dx) : abs(dy);
    float Xinc = dx / (float) steps;
    float Yinc = dy / (float) steps;

    float X = X0;
    float Y = Y0;
    if((dy/dx)<1){
    for (int i=0; i<=steps; i++){
        //putpixel(X,Y,WHITE);
        std::cout<< "(" << X << "," << Y << ")\n";
        X+= Xinc;
        Y+= Yinc;
    }}
    else{
    for(int i=steps; i>=0; i--){
    	std::cout<<"("<<X<<","<<Y<<")\n";
	x-=Xinc;
	y-=Yinc;
    }}
}

int main(int argc, char *argv[]){
    int xa=atoi(argv[1]), xb=atoi(argv[3]), ya=atoi(argv[2]), yb=atoi(argv[4]);
    DDA(xa,ya,xb,yb);
    return 0;
}
