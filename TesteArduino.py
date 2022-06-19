from pyfirmata import Arduino, OUTPUT

PORTA = 'COM3'

arduino = Arduino(PORTA)

arduino.digital[12].mode = OUTPUT

while True:
    arduino.digital[12].write(1)
    arduino.pass_time(2)
    arduino.digital[12].write(0)
    arduino.pass_time(2)
