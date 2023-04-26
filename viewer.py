import pandas as pd
import matplotlib.pyplot as pyplot

df = pd.read_json('data.json')

#Line Chart
fig = pyplot.figure()
ax1 = fig.add_subplot(1,1,1)
ax1.set_xlabel('Time')
ax1.set_ylabel('Temperature')
df['T1'].plot(kind='line')
df['T2'].plot(kind='line')
df['T3'].plot(kind='line')

pyplot.show()
