/**
*   Non-equidistant Fourier Transform
*
*   Uso: Debe haber un archivo de datos con columnas x y y de la serie de tiempo a analizar.
*
*   comando:
*   $ ./NFT "datos.dat" f0 ff step
*
*   y también:
*
*   $ ./NFT "datos.dat" f0 ff step "ouput_name.dat"
*
*   "datos.dat":        string      Archivo a leer
*   f0:                 double      Inicio del espacio de frecuencias.
*   ff:                 double      Final del espacio de frecuencias.
*   step                double      Resolución del espacio de frecuencias.
*   "ouput_name.dat":   string      archivo a escribir los n datos de la transformada. Se escribirán en tres columnas, una frecuencia, otra parte real y otra parte imaginaria.
*
**/


#include <iostream>
#include <fstream>
#include <math.h>
#include <vector>
#include <cstdlib>
#include <complex>
#include <cmath>
#include <algorithm>
#include <string>
#include <sstream>

using namespace std;

typedef complex<double> Complex;


Complex I=1i;
Complex Pi=3.1415926535897+I*0.00000000000000;


/**
* Transformada de los datos para una frecuencia freq
**/
Complex FourierTransform(vector<double> tdata,vector<double> ydata, double freq)
{
    Complex s=0.;
    for(int i=0;i<tdata.size();i++)
    {
        s+=ydata[i]*exp(-2.0*Pi*I*freq*tdata[i]);
    }
    return s;
}


int countfind(string str,string query)
{
    int counter=0;
    for(int i=0;i<str.size();i++)
    {
        string comp;
        comp=str[i];
        if(comp==query)
        {
            counter++;
        }
    }
    return counter;
}


int main (int argc, char *argv[])
{
    // Leer los argumentos

    string filename = argv[1];
    double f0=atof(argv[2]);
    double ff=atof(argv[3]);
    double step=atof(argv[4]);
    string out_name = "fourier_output.dat";
    if(argc==6){out_name = argv[5];}

    //ver cuántas columnas tiene el archivo, y sólo agarrar las primeras 2. aceptados al parecer " " y "\t" como separadores.

    ifstream datos(filename);

    string line;
    getline(datos,line);
    int spaces = countfind(line," ");
    int tabs = countfind(line,"\t");


    // Leer los datos del archivo .dat y guardarlos en los vectores X y Y

    vector<double> X, Y, Z;
    double x, y, z;

    if(tabs>1 || spaces>1)
    {
        while(datos >> x >> y >> z)
        {
            X.push_back(x);
            Y.push_back(y);
            Z.push_back(z);
        }
    }else
    {
        while(datos >> x >> y)
        {
            X.push_back(x);
            Y.push_back(y);
        }
    }



    // Normalizar los datos

    double Yprom=0.000;
    double Ymax=0.0;

    for(int i=0;i<Y.size();i++)
    {
        Yprom+=Y[i];
        if(Y[i]>Ymax)
        {
            Ymax=Y[i];
        }
    }
    Yprom=Yprom/Y.size();



    vector<double> Y2;
    for(int i=0;i<Y.size();i++)
    {
        Y2.push_back((Y[i]-Yprom));
    }

    vector<double> X2;
    for(int i=0;i<X.size();i++)
    {
        X2.push_back(X[i]-X[0]);
    }

    // Calcular la transformada de los datos en el espacio de frecuencias indicado y guardarla en vectores.

    vector<double> FrequencySpace, RealPart, ImagPart;

    double f=f0;
    while(f<=ff)
    {
        FrequencySpace.push_back(f);
        Complex transf=FourierTransform(X,Y2,f);
        //cout << transf << endl;
        RealPart.push_back(real(transf));
        //cout << real(transf) << endl;
        ImagPart.push_back(imag(transf));
        f+=step;
    }

    // Escribir el archivo con la transformada de los datos


    ofstream result(out_name);
    for(int i=0; i < FrequencySpace.size(); i++)
    {
        result << FrequencySpace[i] << "\t" << sqrt(pow(RealPart[i],2)+pow(ImagPart[i],2)) << endl;
    }
    result.close();
    return 0;
}
