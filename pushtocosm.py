import eeml
import serial

# parameters
FEED = 81860
API_KEY = '-nENmzLfiwCpeQGrI7LW5KsRS7aSAKxONjZpWVROVmVXVT0g'
API_URL = '/v2/feeds/{feednum}.xml' .format(feednum = FEED)


serial = serial.Serial('/dev/ttyACM0', 9600)
rawreading = serial.readline().strip()
reading = round(float((float(rawreading)/1023)*100),2)
pac = eeml.Pachube(API_URL, API_KEY)
pac.update([eeml.Data('01', reading, unit=eeml.Moisture())])
pac.put()



