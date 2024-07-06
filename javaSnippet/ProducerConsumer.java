package proj;
import java.lang.Thread;

class Q {
    private int n;
    private boolean empty;
  
    public Q() {
        this.n = -1;
        this.empty = true;
    }
  
    public synchronized void put(int n) {
        while (!this.empty) {
            try {
                this.wait();
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
        this.n = n;
        this.empty = false;
        this.notify();
        System.out.println("Produced:" + n);
    }
  
    public synchronized int get() {
        while (this.empty) {
            try {
                this.wait();
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
        this.empty = true;
        this.notify();
        System.out.println("Consumed:" + this.n);
        return n;
    }
  }

class P implements Runnable {
    Q q;
    Thread t;
    public P(Q queue) {
        this.t = new Thread(this);
        this.q = queue;
    }

    public void run() {
        for (int i = 0; i < 10; i++) {
            q.put(i);
        }
    }
}

class C implements Runnable {
    Q q;
    Thread t;
    public C(Q queue) {
        this.t = new Thread(this);
        this.q = queue;
    }

    public void run() {
        for (int i = 0; i < 10; i++) {
            q.get();
        }
    }
}

public class ProducerConsumer {
    public static void main(String[] args) {
        Q q = new Q();
        P p = new P(q);
        C c = new C(q);
        p.t.start();
        c.t.start();
    }
}