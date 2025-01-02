import RPi.GPIO as GPIO
import time
import multiprocessing

print("0: Car has entered the sensor range, 1: Car has left the sensor range")

def read_gpio(pin1, pin2):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pin1, GPIO.IN)
    GPIO.setup(pin2, GPIO.IN)
    
 
    prev_val1 = GPIO.input(pin1)
    prev_val2 = GPIO.input(pin2)
    
    while True:
        val1 = GPIO.input(pin1)
        val2 = GPIO.input(pin2)
        
     
        if val1 != prev_val1 or val2 != prev_val2:
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
            print("[{}]        Parking Sensor 1:{}             Parking Sensor 2:{}".format(timestamp, val1, val2)) 
            prev_val1 = val1
            prev_val2 = val2
            
        time.sleep(1) 

if __name__ == '__main__':
   
    pin1 = 3
    pin2 = 5

    
    process1 = multiprocessing.Process(target=read_gpio, args=(pin1, pin2))

    process1.start()

    try:
      
        timeout = 60 
        process1.join(timeout)
    except KeyboardInterrupt:
    
        process1.terminate()

    GPIO.cleanup()
