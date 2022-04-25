import serial

import time

serialcomm = serial.Serial('COM4', 115200)
serialcomm.timeout = 1

while True:

    print(serialcomm.readline().decode('ascii'))
    i = input("4 bit girin: ").strip()

    if i == "Son":
        print('Bitti')
        break

    serialcomm.write(i.encode())
    time.sleep(0.5)
    print(serialcomm.readline().decode('ascii'))
serialcomm.close()

