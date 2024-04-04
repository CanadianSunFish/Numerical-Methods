#include <iostream>
#include <cmath>
#include <iomanip> //for setting precision
using namespace std;

// g++ jacobi_gauss-seidel.cpp  -lm -o  jacobi
// ./jacobi

// This will print out Laplace matrix and eigenfunction on its right side.
// On next line, it will print 


int main(){
    int n; //matrix size
    int xEigen;
    int yEigen;
    int iter;

    cout << "Enter the node count (which equals to n^2): " << endl;
    cin >> n;
    cout << "Enter x eigen value: " << endl;
    cin >> xEigen;
    cout << "Enter y eigen value: " << endl;
    cin >> yEigen;
    cout << "Enter iteration count: " << endl;
    cin >> iter;

    double arr[n][n];
    double f[n];
    double jacobiNewArr[n];
    double jacobiOldArr[n];
    double gaussSeidelArr[n];
    
    double h=M_PI/(sqrtN+1.0);
    double error = 100;

    int sqrtN=sqrt(n);
    

    /*
        Setting up Laplace with n^2 nodes.
        -4 across the diagonal and 1 at adjacent nodes.
    */ 
    for(int i=0; i<n; i++){
        jacobiNewArr[i]=0; 
        jacobiOldArr[i]=0; 
        gaussSeidelArr[i]=0; 

        for (int l=0;l<n;l++) {
 		    arr[i][l]=0.0; 
 		} 
        arr[i][i] = -4.0; 

        if(i-1>-1 && i%sqrtN!=0){
            arr[i][i-1]=1.0;
        }
        if(i+1<n && ((i+1)%sqrtN)!=0){
            arr[i][i+1]=1.0;
        }

        for(int j=0; j<n; j++){
            if(j-sqrt(n)==i){
                arr[i][j]=1.0;
            }
            else if(j+sqrt(n)==i){
                arr[i][j]=1.0;
            }

            // Setting f(x)=y vector
            if (i<sqrtN and j<sqrtN){
                int index = i*sqrtN +j;
                f[index]=sin(xEigen*(i+1)*h)*sin(yEigen*(j+1)*h); 
            }
        }
    }

    // Printing Laplace matrix and solution
    cout<<"Laplace matrix  |   y"<<"\n";
    for(int i=0; i<n; i++){
        for(int j=0; j<n; j++){
            cout << arr[i][j] << "  ";
        }
        cout << "\t" << setprecision(6)<<f[i] << "\n";
        cout << "\t" << "\n";
    }

    
    // Random
    for (int k=0; k<iter;k++){ //iteration
        //Jacobi
        for(int i=0; i<n; i++){
            double sum = 0;
            for(int j=0; j<n; j++){
                if(j != i){
                    sum += arr[i][j] * jacobiNewArr[j];
                }
            }
            jacobiNewArr[i] = (f[i] - sum)/arr[i][i];
            error = min(error, jacobiOldArr[i] - jacobiNewArr[i]);
            jacobiOldArr[i] = jacobiNewArr[i];
        }
        //Gauss Seidel
        for(int i=0; i<n; i++){
            double sum = 0;
            for(int j=0; j<n; j++){
                if(j != i){
                    sum += arr[i][j] * gaussSeidelArr[j];
                }
            }
            gaussSeidelArr[i] = (f[i] - sum)/arr[i][i];
        }
    }
    
    //print
    cout<<"jacobi      |   jacobi over eigenvector y    |   Gauss-Seidel    | Gauss Seidel over eiven vector y"<<"\n";
    for(int i=0; i<n; i++){
        cout<<jacobiNewArr[i]<<"\t"<<"\t"<<jacobiNewArr[i]/f[i]<<"\t"<<"\t"<<gaussSeidelArr[i]<<"\t"<<"\t"<<gaussSeidelArr[i]/f[i]<<"\n";
    }
    cout << "\n" << error << endl;

}
