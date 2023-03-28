
import threading
import os
import time
import requests
import serial

def say():
    n = 100
    while (n>3):
        for i in range(n, 0, -1):
            print(i)
            time.sleep(1)
  
def datasend():
    x = requests.get('https://atlas.rvmtr.com/Services//Transaction/Event/ApiDbCreateData?apikeysecret=8bc695c4-8a1b-4e4c-bec2-bee821c3a07d&data=[{" \
    EventId":0,"NodeId":2,"EventDate":"2022-06-16T10:18:27","EventName":"Test Event","EventDescription":"API Test Event","TypeId":2,"PriorityId":4, \
    "ImpactId":3,"StatusId":3,"Source":"...","SourceId":2,"ClearStatus":1,"ClearDateTime":"2022-06-16T10:18:29","SessionId":22,"Gift":15.0, \
    "Comment1":"This record","Comment2":"Created by","Comment3":"Test Api Application"}]')
    print(str(x.status_code)+"veri gönderdim")

def motorrun():
    arduino = serial.Serial(port='COM5', baudrate=9600, timeout=.1)
    def write_read(x):
        arduino.write(bytes(x, 'utf-8'))
        time.sleep(0.05)
        data = arduino.readline()
        return data
    while True:
        num = input("Enter a number: ") # Taking input from user
        value = write_read(num)
        print(value) # printing the value
        datasend()
    
    
    
    
    
  
if __name__ == "__main__":

    # creating threads
    t1 = threading.Thread(target=say, name='t1')
    t2 = threading.Thread(target=datasend, name='t2')  
    t3 = threading.Thread(target=motorrun, name='t3')
    
    
    # starting threads
    t1.start()
    t2.start()
    t3.start()
    
    # wait until all threads finish
    t1.join()
    t2.join()
    t3.join()
    
    