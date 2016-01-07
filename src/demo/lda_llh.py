import matplotlib.pyplot as plt

data = open('../../data/llh_data.txt').readlines()
x = []
y = []
for line in data:
    line = line.split()
    if line == []: continue
    x.append(int(line[0]))
    y.append(int(line[1]))
plt.plot(x[:20], y[:20])
plt.xlabel('iter')
plt.ylabel('log-likelihood')
plt.show()