#include <iostream>
using namespace std;
//Define la función que define a la ecuación diferencial.
float fun(float a);

//Main del archivo
int main(){
	float h=0.01;
	float xi=0.0;
	float xf=4.0;
	int n=((xf-xi)/h);
	float x[n];
	float y[n];

	for(int i=0;i<n;i++){
		if(i==0){
			x[i]=0.0;
			y[i]=1.0;
		}

		else{
			x[i]=x[i-1]+h;
			y[i]=y[i-1]+h*fun(y[i-1]);
		}
		cout << x[i] <<" "<< y[i] <<endl;
	}
	return 0;
}

//Función que define la ecuación diferencial.
float fun (float a){
	return a;
}


