package proj;
import java.lang.Thread;

class Call {
    synchronized void call(String name) {
        try {
            for (int i = 1; i <= 3; i++) {
                System.out.println(name + ": " + String.valueOf(i));
                Thread.sleep(1000);
            }   
            System.out.println(name + " DONE");
        } catch (InterruptedException e) {
            System.out.println(e.getMessage());
        }
    }
}
class newThread implements Runnable {
    Thread t;
    Call callObj;

    public newThread(String name, Call obj) {
        t = new Thread(this, name);
        callObj = obj;
    }

    public void run() {
        callObj.call(t.getName());
    }
}

public class concurrency {
    public static void main(String[] args) {
        Call callObj = new Call();
        newThread n1 = new newThread("n1", callObj);
        newThread n2 = new newThread("n2", callObj);
        newThread n3 = new newThread("n3", callObj);
        n1.t.start();
        n2.t.start();
        n3.t.start();
        try {
            n1.t.join();
            n2.t.join();
            n3.t.join();
        } catch (InterruptedException e) {
            System.out.println(e.getMessage());
        }
        System.out.println("DONE");
    }
}