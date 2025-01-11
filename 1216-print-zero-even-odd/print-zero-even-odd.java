class ZeroEvenOdd {
    private int n;
    Semaphore zero, odd, even;
    public ZeroEvenOdd(int n) {
        this.n = n;
        this.zero = new Semaphore(1);
        this.odd = new Semaphore(0);
        this.even = new Semaphore(0);
    }

    // printNumber.accept(x) outputs "x", where x is an integer.
    public void zero(IntConsumer printNumber) throws InterruptedException {
        for (int i=0; i<n; i++){
            zero.acquire();
            printNumber.accept(0);
            if (i %2 ==0){
                odd.release();
            }
            else{
                even.release();
            }
        }
    }

    public void even(IntConsumer printNumber) throws InterruptedException {
        for (int i=2; i<=n; i+=2){
            even.acquire();
            printNumber.accept(i);
            zero.release();
        }
        
    }

    public void odd(IntConsumer printNumber) throws InterruptedException {
        for (int i=1; i<=n; i+=2){
            odd.acquire();
            printNumber.accept(i);
            zero.release();
        }
    }
}