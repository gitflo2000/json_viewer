import pandas as pd
import matplotlib.pyplot as pyplot

df = pd.read_json('data.json')

df['Timestamp'] = df['Timestamp'].apply(lambda s:s.strip())
df['Timestamp'] = pd.to_datetime(df['Timestamp'], format='%Y-%m-%d_%H-%M-%S')

#Line Chart
fig = pyplot.figure()
ax1 = fig.add_subplot(1,1,1)
ax1.set_xlabel('Time')
ax1.set_ylabel('Temperature')
pyplot.plot(df['Timestamp'],df['T1'])
pyplot.plot(df['Timestamp'],df['T2'])
pyplot.plot(df['Timestamp'],df['T3'])

pyplot.show()
