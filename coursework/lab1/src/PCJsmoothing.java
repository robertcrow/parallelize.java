/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
import java.io.IOException;
import java.util.Random;
import org.pcj.NodesDescription;
import org.pcj.PCJ;
import org.pcj.RegisterStorage;
import org.pcj.StartPoint;
import org.pcj.Storage;

/**
 *
 * @author Robert Crow
 */
@RegisterStorage(PCJsmoothing.shared.class)
public class PCJsmoothing implements StartPoint {

    @Storage(PCJsmoothing.class)
    enum shared {
        x
    }
    double x[];

    public static void main(String args[]) throws IOException {
        PCJ.deploy(PCJsmoothing.class, new NodesDescription("nodes.txt"));
    }

    @Override
    public void main() throws Throwable {

        int nAll = 1024;
        int n = nAll / PCJ.threadCount();
        x = new double[nAll];
        double y[] = new double[nAll];

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

        double xl[] = new double[2];
        double xp]] = new double[2];

        if (PCJ.myId() < PCJ.threadCount()) {
            xp[0] = PCJ.get(PCJ.myId(), shared.x, 0);
            xp[1] = PCJ.get(PCJ.myId(), shared.x, 1);
        }
        if (PCJ.myId() < PCJ.threadCount()) {
            xl[0] = PCJ.get(PCJ.myId() -1, shared.x, n-2);
            xl[1] = PCJ.get(PCJ.myId() -1, shared.x, n-1);
        }

        for (int i = 2; i < n - 2; i++) {
            y[i] = anorm * (a[0] * x[i - 2] + a[1] * x[i - 1] + a[2] * x[i] + a[3] * x[i + 1] + a[4] * x[i + 2]);
        }
        //wypisanie wynikow 
        if (PCJ.myId() == 0) {
            y[0] = a[2] * x[0] + a[3] * x[1] + a[4] * x[2];
            y[0] = y[0] / (a[2] + a[3] + a[4]);
            
            y[1] = a[1] * x[1] + a[2] * x[2] + a[3] * x[3] + a[4] * x[4];
            y[1] = y[1] / (a[1] + a[2] + a[3] + a[4]);
        } else {
            y[0] = a[0] * x[0] + a[1] * x[1] + a[2] * x[2] + a[3] * x[3] + a[4] * x[4];
            y[0] = y[0] * anorm;
            
            y[0] = a[0] * x[0] + a[1] * x[1] + a[2] * x[2] + a[3] * x[3] + a[4] * x[4];
            y[1] = y[1] * anorm;
        }

        if (PCJ.myId() == PCJ.threadCount() - 1) {
            y[n - 1] = a[0] * x[n-3] + a[1] * x[n-2] + a[2] * x[n-1];
            y[n - 1] = y[n - 1] / (a[0] + a[1] + a[2]);
            
            y[n - 2] = a[0] * x[n-4] + a[1] * x[n-3] + a[2] * x[n-2] + a[3] * x[n-1];
            y[n - 2] = y[n - 2] / (a[0] + a[1] + a[2] + a[3]);
        } else {
            y[0] = a[2] * x[0] + a[3] * x[1] + a[4] * x[2];
            y[0] = y[0] * anorm;
            
            y[1] = a[0] * x[0] + a[1] * x[1] + a[2] * x[2] + a[4] * x[3];
            y[1] = y[1] * anorm;
            
        }

        for (int i = 0; i < n; i++) {
            System.out.println(i + " " + y[i]);
        }

    }

}
