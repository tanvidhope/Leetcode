class TrafficLight {
    AtomicBoolean greenOnRoadA;
    ReentrantReadWriteLock greenSignalLock;

    public TrafficLight() {
        this.greenOnRoadA = new AtomicBoolean(true);
        // readlock is used to cross road
        // write lock to change signal
        this.greenSignalLock = new ReentrantReadWriteLock(true);
    }
    
    public void carArrived(
        int carId,           // ID of the car
        int roadId,          // ID of the road the car travels on. Can be 1 (road A) or 2 (road B)
        int direction,       // Direction of the car
        Runnable turnGreen,  // Use turnGreen.run() to turn light to green on current road
        Runnable crossCar    // Use crossCar.run() to make car cross the intersection 
    ) {
        greenSignalLock.readLock().lock();
        if (!isGreen(roadId)){
            // change signal. Release readlock and acquire writelock
            greenSignalLock.readLock().unlock();
            greenSignalLock.writeLock().lock();
            // check again if signal is changed
            if (!isGreen(roadId)){
                toggleGreen();
                turnGreen.run();
            }

            // downgrade to read lock
            greenSignalLock.readLock().lock();
            greenSignalLock.writeLock().unlock();
        }

        // cross the car
        crossCar.run();
        greenSignalLock.readLock().unlock();
    }

    private boolean isGreen(int roadId){
        if (roadId == 1){
            return greenOnRoadA.get();
        }
        else{
            return !greenOnRoadA.get();
        }
    }

    private void toggleGreen(){
        this.greenOnRoadA.set(!greenOnRoadA.get());
    }
}