#!/usr/bin/python3
import serial
import time

ser = serial.Serial('/dev/serial/by-path/platform-fd500000.pcie-pci-0000:01:00.0-usb-0:1.1:1.0-port0', 9600, timeout=5)

# read from Arduino
input_str = ser.readline()
print ("Read input " + input_str.decode("utf-8").strip() + " from Arduino")

while 1:
        # write status back
        ser.write(b'status\n')
        input_str = ser.readline().decode("utf-8").strip()
        if (input_str ==""):
                print(".")
        else:
                # read response back from Arduino
                print ("Read input back: " + input_str)

        time.sleep(5)

        # Write Command Back - ON
        ser.write(b'set on\n')
        input_str = ser.readline().decode("utf-8").strip()
        if (input_str ==""):
                print(".")
        else:
                # read response back from Arduino
                print ("Read input back: " + input_str)

        time.sleep(5)

        # Write Command Back - OFF
        ser.write(b'set off\n')
        input_str = ser.readline().decode("utf-8").strip()
        if (input_str ==""):
                print(".")
        else:
                # read response back from Arduino
                print ("Read input back: " + input_str)

        time.sleep(5)

        # # Write Command Back - nothing
        # ser.write(b'nothing\n')
        # input_str = ser.readline().decode("utf-8").strip()
        # if (input_str ==""):
        #         print(".")
        # else:
        #         # read response back from Arduino
        #         print ("Read input back: " + input_str)

        # time.sleep(5)

