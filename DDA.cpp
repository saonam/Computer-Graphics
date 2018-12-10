/*
By: Pravesh Gaire

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
    if((dy/dx)>1){
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
