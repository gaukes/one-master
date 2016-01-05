import serial
import time

# specify Arduino being used
serial_port_name = '/dev/cu.usbmodem1d1141' # for Mac 
ser = serial.Serial(serial_port_name, 115200, timeout=1)

delay = 1*10 # Delay in seconds

# Run once at the start
def setup():
    try:
        print "Setup"
    except:
        print "Setup Error"

# Run continuously forever
def loop():
# Check if something is in serial buffer 
    if ser.inWaiting() > 0:
        try:
        # Read entire line (until '\n')
            x = ser.readline() 
            # split data between readings
            print "Arduino said", x
        except:
            print "Error with reporting readings"

    # Send to server

    # Read processed information from server, which should come from ListenAndProcess.py

    # 100 ms delay
    time.sleep(0.1) 
    return

# Run continuously forever
# with a delay between calls
def delayed_loop():
    print "Delayed Loop"

# Run once at the end
# Run once at the end
def close(): 
    try:
        print "Close Serial Port"
        ser.close() 
    except:
        print "Close Error"
    
# Program Structure    
def main():
    # Call setup function
    setup()
    # Set start time
    nextLoop = time.time()
    while(True):
        # Try loop() and delayed_loop()
        try:
            loop()
            if time.time() > nextLoop:
                # If next loop time has passed...
                nextLoop = time.time() + delay
                # delayed_loop()
        except KeyboardInterrupt:
            # If user enters "Ctrl + C", break while loop
            break
        except:
            # Catch all errors
            print "Unexpected error."
    # Call close function
    close()

# Run the program
main()
