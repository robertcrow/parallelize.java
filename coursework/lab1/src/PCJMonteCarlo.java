
import java.io.IOException;
import java.util.Random;
import org.pcj.NodesDescription;
import org.pcj.PCJ;
import org.pcj.RegisterStorage;
import org.pcj.StartPoint;
import org.pcj.Storage;

// import everything from a library by: import org.pcj.PCJ.*;
/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
/**
 *
 * @author Robert Crow
 */
@RegisterStorage(PCJMonteCarlo.shared.class)

public class PCJMonteCarlo implements StartPoint {

    @Storage(PCJMonteCarlo.class)
    enum shared {
        cL
    }
    long cL[];

    public static void main(String args[]) throws IOException {
        PCJ.deploy(PCJMonteCarlo.class, new NodesDescription("nodes.txt"));
    }

    @Override
    public void main() throws Throwable {

        cL = new long[PCJ.threadCount()];
        Random r = new Random();
        long nAll = 1_000_000;
        long n = nAll / PCJ.threadCount(); // rozdzielenie pracy
        long c = 0;

        for (int i = 1; i <= n; i++) {
            double x = 2.0 * r.nextDouble() - 1.0;
            double y = 2.0 * r.nextDouble() - 1.0;

            if ((x * x + y * y) < 1) {
                c++;
            }
        }
        System.out.println("c from " + PCJ.myId() + " = " + c);
        PCJ.put(c, 0, shared.cL, PCJ.myId());
        if (PCJ.myId() == 0) {
            
            PCJ.waitFor(shared.cL, PCJ.threadCount());

            long s = 0;

            for (int i = 0; i < PCJ.threadCount(); i++) { // sumowanie

                s = s + cL[i];
                System.out.println("cL" + i + " = " + cL[i]);
            }

            System.out.println(4.0 * (double) s / (double) nAll);
        }
    }

}
