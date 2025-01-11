class BoundedBlockingQueue {
    private int capacity;
    Queue<Integer> queue;
    public BoundedBlockingQueue(int capacity) {
        this.capacity = capacity;
        this.queue = new LinkedList<Integer>();
    }
    
    public void enqueue(int element) throws InterruptedException {
        synchronized(this.queue){
            while (this.queue.size() == this.capacity){
                this.queue.wait();
            }
            this.queue.add(element);
            this.queue.notifyAll();
        }
    }
    
    public int dequeue() throws InterruptedException {
        synchronized(this.queue){
            while (this.queue.size() == 0){
                this.queue.wait();
            }
            int val = this.queue.remove();
            this.queue.notifyAll();
            return val;
        }
    }
    
    public int size() {
        synchronized(this.queue){
            return this.queue.size();
        }
    }
}