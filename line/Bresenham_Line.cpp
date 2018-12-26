/*
 * Pravesh Gaire
 *
 * Breseham's Line Algorithm
*/

#include<iostream>
#include<cmath>

using namespace std;

void bresenham(int xa, int xb, int ya, int yb){
    int dx = abs(xb-xa);
    int dy = abs(yb-ya);
    int lx, ly;
    int p0;
    int x, y, p;

    if (xb > xa) lx=1;
    else lx=-1;
    if (yb > ya) ly=1;
    else ly=-1;
    
//    cout<<"("<<xa<<","<<ya<<")"<<endl;

    if (dx > dy){
    	p0 = 2 * dy - dx;
	for(int i=0; i<=dx; i++){
	    cout<<"("<<xa<<","<<ya<<")"<<endl;
	    if (p0 < 0){
	    	x = xa + lx;
		y = ya;
		p = p0 + 2 * dy;
	    }
	    else {
	    	x = xa + lx;
		y = ya + ly;
		p = p0 + 2 * dy - 2* dx;
	    }
	    xa = x;
	    ya = y;
	    p0 = p;
	}
    }
    else{
        p0 = 2 * dx - dy;
	for(int i=0; i<=dy; i++){
	    cout<<"("<<xa<<","<<ya<<")"<<endl;
	    if(p0 < 0){
	    	x = xa;
		y = ya + ly;
		p = p0 + 2 * dx;
	    }
	    else{
	    	x = xa + lx;
		y = ya + ly;
		p = p0 + 2 * dx - 2 * dy;
	    }
	    xa = x;
	    ya = y;
	    p0 = p;
	}
    }
}

int main(int argc, char *argv[]){
    //int xa=12, xb=24, ya=6, yb=16;
    int xa = atoi(argv[1]), xb = atoi(argv[3]), ya = atoi(argv[2]), yb = atoi(argv[4]);
    bresenham(xa, xb, ya, yb);
    return 0;
}
