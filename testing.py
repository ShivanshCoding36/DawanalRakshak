import serial

# Open serial connection to Arduino
ser = serial.Serial('COM6', 9600, timeout=1)

while True:
    a = input('What to do: ')
    if a == 'a':
        # Send 'F' to Arduino
        ser.write(b'F')
        print("Sent 'F' to Arduino")
    elif a == 'q':
        break