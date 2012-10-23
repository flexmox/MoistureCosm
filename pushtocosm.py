import eeml
import serial

# parameters
FEED = 81860
API_KEY = '-nENmzLfiwCpeQGrI7LW5KsRS7aSAKxONjZpWVROVmVXVT0g'
API_URL = '/v2/feeds/{feednum}.xml' .format(feednum = FEED)
rawreading = 0.00

serial = serial.Serial('/dev/ttyACM0', 9600)
for x in range(10):
  rawreading += float(serial.readline().strip())

avgreading = rawreading/10.00

reading = round(float((float(avgreading)/1023.00)*100.00),2)

pac = eeml.Pachube(API_URL, API_KEY)
pac.update([eeml.Data('01', reading, unit=eeml.Moisture())])
pac.put()



