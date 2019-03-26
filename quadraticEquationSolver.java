
import java.util.Scanner;

/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author Robert Crow
 */
public class quadraticEquationSolver {
    
    public static void main(String args[]){
        
        double a,b,c;
        
        Scanner sc = new Scanner(System.in);
        a = sc.nextDouble();
        b = sc.nextDouble();
        c = sc.nextDouble();
        
        double d = delta(a,b,c);
        
        if(d < 0){
            System.out.println("no real solutions");
        }
        if(0 == d){
            double x;
            x = -b/(2*a);
            
            System.out.println("one real solution:  " + x);
        }
        if(d > 0){
            double x1, x2;
            x1 = (-b - Math.sqrt(d)) / (2 * a);
            x2 = (-b + Math.sqrt(d)) / (2 * a);
            
            System.out.println("two real solutions real:  " + x1 + " " + x2);
        }
    }
    
    static double delta(double a, double b, double c){
        double delta = b*b - 4 * a * c;
        return delta;
    }
}
