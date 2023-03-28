import psycopg2
import serial

con = psycopg2.connect(
                        host = "localhost",
                        database = "my_database",
                        user = "postgres",
                        password = "1234")
cur = con.cursor()


ser1 = serial.Serial(port='COM4', baudrate=9600, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS, timeout=0)
ser2 = serial.Serial(port='COM12', baudrate=9600, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS, timeout=0)
ser3 = serial.Serial(port='COM13', baudrate=9600, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS, timeout=0)
ser4 = serial.Serial(port='COM14', baudrate=9600, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS, timeout=0)

while True:
    if ser1.in_waiting:
        data1 = ser1.readline()
        a1 = data1.decode('utf')
        cur.execute("select * from rvmtr where kod ="+str(a1))
        row1 = cur.fetchall()
        print(row1)
        
    if ser2.in_waiting:
        data2 = ser2.readline()
        a2 = data2.decode('utf')
        cur.execute("select * from rvmtr where kod ="+str(a2))
        row2 = cur.fetchall()
        print(row2)
        
    if ser3.in_waiting:
        data3 = ser3.readline()
        a3 = data3.decode('utf')
        cur.execute("select * from rvmtr where kod ="+str(a3))
        row3 = cur.fetchall()
        print(row3)
        
    if ser4.in_waiting:
        data4 = ser4.readline()
        a4 = data4.decode('utf')
        cur.execute("select * from rvmtr where kod ="+str(a4))
        row4 = cur.fetchall()
        print(row4)
