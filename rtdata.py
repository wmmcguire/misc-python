import matplotlib.pyplot as plt 
from time import sleep
import numpy as np
from datetime import datetime


runTime = datetime.now()
delay = 1 #delay of 1 second

fig = plt.figure()
ax1=fig.add_subplot(1,1,1)
plt.title('Sin over Time')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.legend(['Amplitude = 1'])

def main():
	fig.show()

	x, y, t = [], [], []


	while True:
		currentTime = datetime.now()
		

		x.append(t)
		y.append(np.sin(np.pi*t))

		ax1.plot(x,y, 'r')

		fig.canvas.draw()

		ax1.set_xlim(left = t-5, right=t+5)

		sleep(0.1)
		t += 0.09
		

if __name__ == '__main__':
	main()