import numpy as np

exportString = np.arange(0, -1000, -1)
exportList = []

for i in exportString:
    #print(type(i))
    rounded = str(round(i, 2))
    exportList.append(rounded)
    #print(rounded)

output = ", ".join(exportList)
print(output)