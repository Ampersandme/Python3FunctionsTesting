def scaleList(strOriginal, multiplier):

    import numpy as np

    exportString =  strOriginal.split(",")
    exportList = []

    for i in exportString:
        #print(type(i))
        numb = float(i)
        rounded = str(int(numb * multiplier))
        exportList.append(rounded)
        #print(rounded)

    output = ", ".join(exportList)
    print(output)

    return output
