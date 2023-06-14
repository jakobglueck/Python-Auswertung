import matplotlib.pyplot as plt
import seaborn as sb
import pandas as pd

def createPlotValues(path):
    with open(path, 'r') as data:
        lines = data.readlines()[1:]
        values = [int(line.strip().split(",")[1]) for line in lines]
    return values


def splitDirectoryFiles(data, directory):
    valueArray = []
    for line in data:
        if directory in line:
            valueArray.append(line)
    return valueArray


def calculateInKilobytes(dataValues):
    dataInKb = []
    for value in dataValues:
        dataInKb.append(value / 1000000000)
    return dataInKb

def calculateInMs(dataValues):
    dataInKb = []
    for value in dataValues:
        dataInKb.append(value / 1000000)
    return dataInKb

if __name__ == '__main__':

    #JSONSIZES
    dfBestAbsolute = pd.read_csv('/Users/jakobglueck/Desktop/Foldersize/Zeitmessungen/Bestcase/Heartbeats/ZeitMessungen/HeartbeatsToJson.txt', delimiter=',',header=None, names=["JsonFile", "FileSize in bytes"], skiprows=1, dtype={"FileSize in bytes": int})
    dfBestDifferential = pd.read_csv('/Users/jakobglueck/Desktop/Foldersize/Zeitmessungen/Bestcase/Heartbeats/ZeitMessungen/HeartbeatsToDifferentialJson.txt', delimiter=',', header=None, names=["JsonFile","FileSize in bytes"],skiprows=1, dtype={"FileSize in bytes": int})

    mask1min = dfBestAbsolute['JsonFile'].str.contains('/1/')
    dataBestAbsolute1min = dfBestAbsolute[mask1min]
    mask5min = dfBestAbsolute['JsonFile'].str.contains('/5/')
    dataBestAbsolute5min = dfBestAbsolute[mask5min]

    mask1min = dfBestDifferential['JsonFile'].str.contains('/1/')
    dataBestDifferential1min = dfBestDifferential[mask1min]
    mask5min = dfBestDifferential['JsonFile'].str.contains('/5/')
    dataBestDifferential5min = dfBestDifferential[mask5min]

    dataBestAbsolute1min['FileSize in bytes'] = calculateInKilobytes(dataBestAbsolute1min['FileSize in bytes'])
    dataBestAbsolute5min['FileSize in bytes'] = calculateInKilobytes(dataBestAbsolute5min['FileSize in bytes'])

    dataBestDifferential1min['FileSize in bytes'] = calculateInKilobytes(dataBestDifferential1min['FileSize in bytes'])
    dataBestDifferential5min['FileSize in bytes'] = calculateInKilobytes(dataBestDifferential5min['FileSize in bytes'])

    dataBestAbsolute1min['Jsonform'] = 'absoluteJson'
    dataBestAbsolute1min[""] = "Optimalfall"
    dataBestAbsolute5min['Jsonform'] = 'absoluteJson'
    dataBestAbsolute5min[""] = "Optimalfall"
    dataBestDifferential1min['Jsonform'] = 'differentialJson'
    dataBestDifferential1min[""] = "Optimalfall"
    dataBestDifferential5min['Jsonform'] = 'differentialJson'
    dataBestDifferential5min[""] = "Optimalfall"
    df_Best1min = pd.concat([dataBestAbsolute1min, dataBestDifferential1min])
    df_Best5min = pd.concat([ dataBestAbsolute5min, dataBestDifferential5min])





    dfNormalAbsolute = pd.read_csv('/Users/jakobglueck/Desktop/Foldersize/Zeitmessungen/normal/Heartbeats/ZeitMessungen/HeartbeatsToJson.txt', delimiter =',', header=None, names=["JsonFile","FileSize in bytes"],skiprows=1, dtype={"FileSize in bytes": int})
    dfNormalDifferential = pd.read_csv('/Users/jakobglueck/Desktop/Foldersize/Zeitmessungen/normal/Heartbeats/ZeitMessungen/HeartbeatsToDifferentialJson.txt', delimiter=',', header=None, names=["JsonFile","FileSize in bytes"],skiprows=1, dtype={"FileSize in bytes": int})

    mask1min = dfNormalAbsolute['JsonFile'].str.contains('/1/')
    dataNormalAbsolute1min = dfNormalAbsolute[mask1min]
    mask5min = dfNormalAbsolute['JsonFile'].str.contains('/5/')
    dataNormalAbsolute5min = dfNormalAbsolute[mask5min]

    mask1min = dfNormalDifferential['JsonFile'].str.contains('/1/')
    dataNormalDifferential1min = dfNormalDifferential[mask1min]
    mask5min = dfNormalDifferential['JsonFile'].str.contains('/5/')
    dataNormalDifferential5min = dfNormalDifferential[mask5min]

    dataNormalAbsolute1min['FileSize in bytes'] = calculateInKilobytes(dataNormalAbsolute1min['FileSize in bytes'])
    dataNormalAbsolute5min['FileSize in bytes'] = calculateInKilobytes(dataNormalAbsolute5min['FileSize in bytes'])

    dataNormalDifferential1min['FileSize in bytes'] = calculateInKilobytes(dataNormalDifferential1min['FileSize in bytes'])
    dataNormalDifferential5min['FileSize in bytes'] = calculateInKilobytes(dataNormalDifferential5min['FileSize in bytes'])

    dataNormalAbsolute1min['Jsonform'] = 'absoluteJson'
    dataNormalAbsolute1min[""] = "Realfall"
    dataNormalAbsolute5min['Jsonform'] = 'absoluteJson'
    dataNormalAbsolute5min[""] = "Realfall"
    dataNormalDifferential1min['Jsonform'] = 'differentialJson'
    dataNormalDifferential1min[""] = "Realfall"
    dataNormalDifferential5min['Jsonform'] = 'differentialJson'
    dataNormalDifferential5min[""] = "Realfall"
    df_Normal1min = pd.concat([dataNormalAbsolute1min, dataNormalDifferential1min])
    df_Normal5min = pd.concat([dataNormalAbsolute5min, dataNormalDifferential5min])

    dfWorstAbsolute = pd.read_csv('/Users/jakobglueck/Desktop/Foldersize/Zeitmessungen/Worstcase/Heartbeats/ZeitMessungen/HeartbeatsToJson.txt', delimiter=',', header=None, names=["JsonFile", "FileSize in bytes"], skiprows=1, dtype={"FileSize in bytes": int})
    dfWorstDifferential = pd.read_csv('/Users/jakobglueck/Desktop/Foldersize/Zeitmessungen/Worstcase/Heartbeats/ZeitMessungen/HeartbeatsToDifferentialJson.txt',delimiter=',', header=None, names=["JsonFile", "FileSize in bytes"], skiprows=1,dtype={"FileSize in bytes": int})

    mask1min = dfWorstAbsolute['JsonFile'].str.contains('/1/')
    dataWorstAbsolute1min = dfWorstAbsolute[mask1min]
    mask5min = dfWorstAbsolute['JsonFile'].str.contains('/5/')
    dataWorstAbsolute5min = dfWorstAbsolute[mask5min]

    mask1min = dfWorstDifferential['JsonFile'].str.contains('/1/')
    dataWorstDifferential1min = dfWorstDifferential[mask1min]
    mask5min = dfWorstDifferential['JsonFile'].str.contains('/5/')
    dataWorstDifferential5min = dfWorstDifferential[mask5min]

    dataWorstAbsolute1min['FileSize in bytes'] = calculateInKilobytes(dataWorstAbsolute1min['FileSize in bytes'])
    dataWorstAbsolute5min['FileSize in bytes'] = calculateInKilobytes(dataWorstAbsolute5min['FileSize in bytes'])

    dataWorstDifferential1min['FileSize in bytes'] = calculateInKilobytes(dataWorstDifferential1min['FileSize in bytes'])
    dataWorstDifferential5min['FileSize in bytes'] = calculateInKilobytes(dataWorstDifferential5min['FileSize in bytes'])

    dataWorstAbsolute1min['Jsonform'] = 'absoluteJson'
    dataWorstAbsolute1min[""] = "Pessimalfall"
    dataWorstAbsolute5min['Jsonform'] = 'absoluteJson'
    dataWorstAbsolute5min[""] = "Pessimalfall"
    dataWorstDifferential1min['Jsonform'] = 'differentialJson'
    dataWorstDifferential1min[""] = "Pessimalfall"
    dataWorstDifferential5min['Jsonform'] = 'differentialJson'
    dataWorstDifferential5min[""] = "Pessimalfall"
    df_Worst1min = pd.concat([dataWorstAbsolute1min, dataWorstDifferential1min])
    df_Worst5min = pd.concat([dataWorstAbsolute5min, dataWorstDifferential5min])


    df_allJson1min = pd.concat([df_Best1min, df_Normal1min, df_Worst1min])
    df_allJson5min = pd.concat([df_Best5min, df_Normal5min, df_Worst5min])

    #PcoreSIZES

    dfBestPcore = pd.read_csv( '/Users/jakobglueck/Desktop/Foldersize/Zeitmessungen/Bestcase/Heartbeats/ZeitMessungen/HeartbeatsSerialize.txt', delimiter=',',header=None, names=["JsonFile", "FileSize in bytes"], skiprows=1, dtype={"FileSize in bytes": int})

    maskBestPcore1min = dfBestPcore['JsonFile'].str.contains('/1/')
    dataBestPcore1min = dfBestPcore[maskBestPcore1min]
    maskBestPcore5min = dfBestPcore['JsonFile'].str.contains('/5/')
    dataBestPcore5min = dfBestPcore[maskBestPcore5min]

    dataBestPcore1min['FileSize in bytes'] = calculateInKilobytes(dataBestPcore1min['FileSize in bytes'])
    dataBestPcore5min['FileSize in bytes'] = calculateInKilobytes(dataBestPcore5min['FileSize in bytes'])

    dataBestPcore1min[""] = "Optimalfall"
    dataBestPcore5min[""] = "Optimalfall"

    dfNormalPcore = pd.read_csv( '/Users/jakobglueck/Desktop/Foldersize/Zeitmessungen/normal/Heartbeats/ZeitMessungen/HeartbeatsSerialize.txt', delimiter=',',header=None, names=["JsonFile", "FileSize in bytes"], skiprows=1, dtype={"FileSize in bytes": int})

    maskNormalPcore1min = dfNormalPcore['JsonFile'].str.contains('/1/')
    dataNormalPcore1min = dfNormalPcore[maskNormalPcore1min]
    maskNormalPcore5min = dfNormalPcore['JsonFile'].str.contains('/5/')
    dataNormalPcore5min = dfNormalPcore[maskNormalPcore5min]
    dataNormalPcore1min['FileSize in bytes'] = calculateInKilobytes(dataNormalPcore1min['FileSize in bytes'])
    dataNormalPcore5min['FileSize in bytes'] = calculateInKilobytes(dataNormalPcore5min['FileSize in bytes'])

    dataNormalPcore1min[""] = "Realfall"
    dataNormalPcore5min[""] = "Realfall"


    dfWorstPcore = pd.read_csv( '/Users/jakobglueck/Desktop/Foldersize/Zeitmessungen/Worstcase/Heartbeats/ZeitMessungen/HeartbeatsSerialize.txt', delimiter=',',header=None, names=["JsonFile", "FileSize in bytes"], skiprows=1, dtype={"FileSize in bytes": int})

    maskWorstPcore1min = dfWorstPcore['JsonFile'].str.contains('/1/')
    dataWorstPcore1min = dfWorstPcore[maskWorstPcore1min]
    maskWorstPcore5min = dfWorstPcore['JsonFile'].str.contains('/5/')
    dataWorstPcore5min = dfWorstPcore[maskWorstPcore5min]

    dataWorstPcore1min['FileSize in bytes'] = calculateInKilobytes(dataWorstPcore1min['FileSize in bytes'])
    dataWorstPcore5min['FileSize in bytes'] = calculateInKilobytes(dataWorstPcore5min['FileSize in bytes'])

    dataWorstPcore1min[""] = "Pessimalfall"
    dataWorstPcore5min[""] = "Pessimalfall"

    df_allPcore1min =pd.concat([dataBestPcore1min,dataNormalPcore1min,dataWorstPcore1min])
    df_allPcore5min = pd.concat([dataBestPcore5min, dataNormalPcore5min, dataWorstPcore5min])


fig = plt.figure(figsize=(25,15))
sb.set(style="darkgrid")
ax = fig.add_subplot(221)
ax = sb.violinplot(data=df_allJson1min, x='', y="FileSize in bytes", hue="Jsonform", linewidth=1, split=True,inner = "quartile", palette={ "absoluteJson": "b", "differentialJson": ".85"})
ax.legend([],[], frameon=False)
ax.set_ylabel("Zeit in s")
ax.set_title('(a)', fontsize=10,loc="left")
sb.set(style="darkgrid")
ax1 = fig.add_subplot(223)
ax1 = sb.violinplot(data=df_allPcore1min, x='', y="FileSize in bytes",inner = "quartile", palette="Blues")
ax1.set_ylabel("Zeit in s")
ax1.set_title('(c)', fontsize=10,loc="left")
sb.set(style="darkgrid")

ax2 = fig.add_subplot(222)
ax2 = sb.violinplot(data=df_allJson5min, x='', y="FileSize in bytes", hue="Jsonform", linewidth=1, split=True,inner = "quartile", palette={ "absoluteJson": "b", "differentialJson": ".85"})
ax2.legend([], [], frameon=False)
ax2.set_ylabel("Zeit in s")
ax2.set_title('(b)', fontsize=10,loc="left")
sb.set(style="darkgrid")

ax3 = fig.add_subplot(224)
ax3 = sb.violinplot(data=df_allPcore5min, x='', y="FileSize in bytes",inner = "quartile", palette="Blues")
ax3.set_ylabel("Zeit in s")
ax3.set_title('(d)', fontsize=10,loc="left")
sb.set(style="darkgrid")
fig.tight_layout(pad=4.0)
plt.show()

