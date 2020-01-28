#include "stdafx.h"
#include "conio.h"
#include "math.h"
#include <iostream>
using namespace std;
double func (double x, double y)
{
        return(x-2sqrt(y));
}
int main()
{
        double a=1, b=2;
        double h=(b-a)/10;
        double n=(b-a)/h; //кол-во точек на вычисляемом отрезке функции
        double X[(int)n]; // массивы значений
        double Y[(int)n];
        X[0]=1; Y[1]=0; //начальные условия
        cout<<"\n metod Eilera \n";
        cout<<"h= "<<h;
        cout<<"\n n= "<<n;
        for(int i=1;i<=n;i++)
        {
                X[i]=a+i*h;
                cout<<"X["<<i<<"]= "<<X[i]<<"\n";
                Y[i]=Y[i-1]+h*func(X[i-1],Y[i-1]);
                cout<<"Y["<<i<<"]= "<<Y[i]<<"\n";

        };
        cout<<endl;
        return 0;
}
