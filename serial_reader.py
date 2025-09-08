import serial
import time

# Replace 'COM3' with your actual port.
ser = serial.Serial('COM10', 115200, timeout=1)

# Wait for the ESP32 to reset and open the serial connection.
time.sleep(2)

print("Listening to ESP32...")

try:
    while True:
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').strip()
            print("Received:", line)

except KeyboardInterrupt:
    print("Exiting...")
    ser.close()
