
/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */


import java.util.Random;

/**
 *
 * @author Robert Crow
 */
public class Smoothing {

    static double x[] = new double[1024];
    static double y[] = new double[1024];

    public static void main(String args[]) {

        int n = 1024;
        double a[] = new double[5];

        a[0] = -3.0;
        a[1] = -12.0;
        a[2] = 17.0;
        a[3] = 12.0;
        a[4] = -3.0;

        Random r = new Random();

        for (int i = 0; i < n; i++) {
            x[i] = r.nextDouble();
        }

        double anorm = 1.0 / (a[0] + a[1] + a[2] + a[3] + a[4]);
        y[0] = a[2] * x[0] + a[3] * x[1] + a[4] * x[2];
        y[0] = y[0] / (a[2] + a[3] + a[4]);
        y[1] = a[1] * x[1] + a[2] * x[2] + a[3] * x[3]; 
        y[1] = y[1] / (a[1] + a[2] + a[3] + a[4]);
                
        y[n-1] = a[2] * x[0] + a[3] * x[1] + a[4] * x[2];
        y[n-1] = y[n-1] / (a[0] + a[1] + a[2]);
        y[n-2] = a[1] * x[1] + a[2] * x[2] + a[3] * x[3]; 
        y[n-2] = y[n-2] / (a[0] + a[1] + a[2] + a[3]);
        
        
        
        for (int i = 2; i < n-2; i++) {
            y[i] = anorm * (a[0] * x[i - 2] + a[1] * x[i - 1] + a[2] * x[i] + a[3] * x[i + 1] + a[4] * x[i + 2]);
        }
        //wypisanie wynikow 

        for (int i = 0; i < n; i++) {
            System.out.println(i + " " + y[i]);
        }

    }

}
