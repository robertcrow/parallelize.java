import java.io.IOException;
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
@RegisterStorage(PCJHelloWorld.shared.class)

public class PCJHelloWorld implements StartPoint{
    
    @Storage(PCJHelloWorld.class)
    enum shared{a}
    int a;
    
    public static void main(String args[]) throws IOException{
        PCJ.deploy(PCJHelloWorld.class, new NodesDescription("nodes.txt"));
    }
    
    
    @Override
    public void main() throws Throwable{
        
        System.out.println("Hello from  " +  PCJ.myId() + " out of " + PCJ.threadCount() );
        
        PCJ.barrier(); // hold-up dla wszystkich watkow
        a = PCJ.myId();
        
        System.out.println("Hello from  " +  PCJ.myId() + " a = " + a);
        
        PCJ.broadcast(-1, shared.a); // 
        if (PCJ.myId() == 0 ) PCJ.asyncBroadcast(-1, shared.a);
        PCJ.waitFor(shared.a); // czekam na zmiane zmiennej wynikajacej z komunikacji
        System.out.println("Hello from  " +  PCJ.myId() + " a (po broadcast) = " + a);
        
        if (PCJ.myId() == 1){
            a = -10;
            PCJ.put(a, 0, shared.a);
            
        }
        
        if (PCJ.myId() == 0){
            PCJ.waitFor(shared.a);
        }
        System.out.println("Hello from " + PCJ.myId() + " a (po PCJ.put)  " + a);
        
    }

}