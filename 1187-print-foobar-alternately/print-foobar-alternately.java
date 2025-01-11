class FooBar {
    private int n;
    Semaphore foo = new Semaphore(0);
    Semaphore bar = new Semaphore(1);

    public FooBar(int n) {
        this.n = n;
    }

    public void foo(Runnable printFoo) throws InterruptedException {
        
        for (int i = 0; i < n; i++) {
            bar.acquire();
        	// printFoo.run() outputs "foo". Do not change or remove this line.
        	printFoo.run();
            foo.release();
        }
    }

    public void bar(Runnable printBar) throws InterruptedException {
        
        for (int i = 0; i < n; i++) {
            foo.acquire();
            // printBar.run() outputs "bar". Do not change or remove this line.
        	printBar.run();
            bar.release();
        }
    }
}