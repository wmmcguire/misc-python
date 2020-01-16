from sense_hat import SenseHat
from datetime import datetime
import csv

hat = SenseHat()

timestamp = datetime.now()
delay = 30

with open('data.csv', 'w', newline='') as f:
	data_writer = csv.writer(f)


def get_snsData():
	snsData = []
	snsData.append(hat.get_temperature())
	snsData.append(hat.get_pressure())
	snsData.append(hat.get_humidity())

	mag = hat.get_compass_raw()
	snsData.append(mag['x'])
	snsData.append(mag['y'])
	snsData.append(mag['z'])

	acc = hat.get_accelerometer_raw()
	snsData.append(acc['x'])
	snsData.append(acc['y'])
	snsData.append(acc['z'])

	gyro = sense.get_gyroscope_raw()
	snsData.append(gyro['x'])
	snsData.append(gyro['y'])
	snsData.append(gyro['z'])

	snsData.append(datetime.now())
	

	

data_writer.writerow(
	['temp', 'pres', 'hum',
	'yaw', 'pitch', 'roll,'
	'mag_x', 'mag_y', 'mag_z',
	'gyro_x', 'gyro_y', 'gyro_z'
	'datetime'

	])
 
isFivemins = False


while isFivemins == False:
	data = get_snsData()

	dt = data[-1] - timestamp #last index of data will always be a datetime

	if dt.seconds > delay:
		data_writer = writerow(data)
		timestamp = datetime.now()

	if dt.minutes = 5:
		isFivemins = True



	
