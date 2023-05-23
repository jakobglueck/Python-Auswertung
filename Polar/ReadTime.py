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


if __name__ == '__main__':

    #JSONSIZES
    dfBestAbsolute = pd.read_csv('/Users/jakobglueck/Desktop/Foldersize/Zeitmessungen/Bestcase/Polar/ZeitMessungen/PolarbeatsJsonRead.txt', delimiter=',',header=None, names=["JsonFile", "FileSize in bytes"], skiprows=1, dtype={"FileSize in bytes": int})
    dfBestDifferential = pd.read_csv('/Users/jakobglueck/Desktop/Foldersize/Zeitmessungen/Bestcase/Polar/ZeitMessungen/PolarbeatsDifferentialJsonRead.txt', delimiter=',', header=None, names=["JsonFile","FileSize in bytes"],skiprows=1, dtype={"FileSize in bytes": int})

    maskCoordinate = dfBestAbsolute['JsonFile'].str.contains('/30MinCoordinate/')
    dataBestAbsoluteCoordinate = dfBestAbsolute[maskCoordinate]
    maskNorm = dfBestAbsolute['JsonFile'].str.contains('/30MinNorm/')
    dataBestAbsoluteNorm = dfBestAbsolute[maskNorm]

    maskCoordinate = dfBestDifferential['JsonFile'].str.contains('/30MinCoordinate/')
    dataBestDifferentialCoordinate = dfBestDifferential[maskCoordinate]
    maskNorm = dfBestDifferential['JsonFile'].str.contains('/30MinNorm/')
    dataBestDifferentialNorm = dfBestDifferential[maskNorm]

    dataBestAbsoluteCoordinate['FileSize in bytes'] = calculateInKilobytes(dataBestAbsoluteCoordinate['FileSize in bytes'])
    dataBestAbsoluteNorm['FileSize in bytes'] = calculateInKilobytes(dataBestAbsoluteNorm['FileSize in bytes'])

    dataBestDifferentialCoordinate['FileSize in bytes'] = calculateInKilobytes(dataBestDifferentialCoordinate['FileSize in bytes'])
    dataBestDifferentialNorm['FileSize in bytes'] = calculateInKilobytes(dataBestDifferentialNorm['FileSize in bytes'])

    dataBestAbsoluteCoordinate['Jsonform'] = 'absoluteJson'
    dataBestAbsoluteCoordinate[""] = "Optimalfall"
    dataBestAbsoluteNorm['Jsonform'] = 'absoluteJson'
    dataBestAbsoluteNorm[""] = "Optimalfall"
    dataBestDifferentialCoordinate['Jsonform'] = 'differentialJson'
    dataBestDifferentialCoordinate[""] = "Optimalfall"
    dataBestDifferentialNorm['Jsonform'] = 'differentialJson'
    dataBestDifferentialNorm[""] = "Optimalfall"
    df_BestCoordinate = pd.concat([dataBestAbsoluteCoordinate, dataBestDifferentialCoordinate])
    df_BestNorm = pd.concat([ dataBestAbsoluteNorm, dataBestDifferentialNorm])





    dfNormalAbsolute = pd.read_csv('/Users/jakobglueck/Desktop/Foldersize/Zeitmessungen/normal/Polar/ZeitMessungen/PolarbeatsJsonRead.txt', delimiter =',', header=None, names=["JsonFile","FileSize in bytes"],skiprows=1, dtype={"FileSize in bytes": int})
    dfNormalDifferential = pd.read_csv('/Users/jakobglueck/Desktop/Foldersize/Zeitmessungen/normal/Polar/ZeitMessungen/PolarbeatsDifferentialJsonRead.txt', delimiter=',', header=None, names=["JsonFile","FileSize in bytes"],skiprows=1, dtype={"FileSize in bytes": int})

    maskCoordinate = dfNormalAbsolute['JsonFile'].str.contains('/30MinCoordinate/')
    dataNormalAbsoluteCoordinate = dfNormalAbsolute[maskCoordinate]
    maskNorm = dfNormalAbsolute['JsonFile'].str.contains('/5/')
    dataNormalAbsoluteNorm = dfNormalAbsolute[maskNorm]

    maskCoordinate = dfNormalDifferential['JsonFile'].str.contains('/30MinCoordinate/')
    dataNormalDifferentialCoordinate = dfNormalDifferential[maskCoordinate]
    maskNorm = dfNormalDifferential['JsonFile'].str.contains('/30MinNorm/')
    dataNormalDifferentialNorm = dfNormalDifferential[maskNorm]

    dataNormalAbsoluteCoordinate['FileSize in bytes'] = calculateInKilobytes(dataNormalAbsoluteCoordinate['FileSize in bytes'])
    dataNormalAbsoluteNorm['FileSize in bytes'] = calculateInKilobytes(dataNormalAbsoluteNorm['FileSize in bytes'])

    dataNormalDifferentialCoordinate['FileSize in bytes'] = calculateInKilobytes(dataNormalDifferentialCoordinate['FileSize in bytes'])
    dataNormalDifferentialNorm['FileSize in bytes'] = calculateInKilobytes(dataNormalDifferentialNorm['FileSize in bytes'])

    dataNormalAbsoluteCoordinate['Jsonform'] = 'absoluteJson'
    dataNormalAbsoluteCoordinate[""] = "Realfall"
    dataNormalAbsoluteNorm['Jsonform'] = 'absoluteJson'
    dataNormalAbsoluteNorm[""] = "Realfall"
    dataNormalDifferentialCoordinate['Jsonform'] = 'differentialJson'
    dataNormalDifferentialCoordinate[""] = "Realfall"
    dataNormalDifferentialNorm['Jsonform'] = 'differentialJson'
    dataNormalDifferentialNorm[""] = "Realfall"
    df_NormalCoordinate = pd.concat([dataNormalAbsoluteCoordinate, dataNormalDifferentialCoordinate])
    df_NormalNorm = pd.concat([dataNormalAbsoluteNorm, dataNormalDifferentialNorm])

    dfWorstAbsolute = pd.read_csv('/Users/jakobglueck/Desktop/Foldersize/Zeitmessungen/Worstcase/Polar/ZeitMessungen/PolarJsonRead.txt', delimiter=',', header=None, names=["JsonFile", "FileSize in bytes"], skiprows=1, dtype={"FileSize in bytes": int})
    dfWorstDifferential = pd.read_csv('/Users/jakobglueck/Desktop/Foldersize/Zeitmessungen/Worstcase/Polar/ZeitMessungen/PolarDifferentialJsonRead.txt',delimiter=',', header=None, names=["JsonFile", "FileSize in bytes"], skiprows=1,dtype={"FileSize in bytes": int})

    maskCoordinate = dfWorstAbsolute['JsonFile'].str.contains('/30MinCoordinate/')
    dataWorstAbsoluteCoordinate = dfWorstAbsolute[maskCoordinate]
    maskNorm = dfWorstAbsolute['JsonFile'].str.contains('/30MinNorm/')
    dataWorstAbsoluteNorm = dfWorstAbsolute[maskNorm]

    maskCoordinate = dfWorstDifferential['JsonFile'].str.contains('/30MinCoordinate/')
    dataWorstDifferentialCoordinate = dfWorstDifferential[maskCoordinate]
    maskNorm = dfWorstDifferential['JsonFile'].str.contains('/30MinNorm/')
    dataWorstDifferentialNorm = dfWorstDifferential[maskNorm]

    dataWorstAbsoluteCoordinate['FileSize in bytes'] = calculateInKilobytes(dataWorstAbsoluteCoordinate['FileSize in bytes'])
    dataWorstAbsoluteNorm['FileSize in bytes'] = calculateInKilobytes(dataWorstAbsoluteNorm['FileSize in bytes'])

    dataWorstDifferentialCoordinate['FileSize in bytes'] = calculateInKilobytes(dataWorstDifferentialCoordinate['FileSize in bytes'])
    dataWorstDifferentialNorm['FileSize in bytes'] = calculateInKilobytes(dataWorstDifferentialNorm['FileSize in bytes'])

    dataWorstAbsoluteCoordinate['Jsonform'] = 'absoluteJson'
    dataWorstAbsoluteCoordinate[""] = "Pessimalfall"
    dataWorstAbsoluteNorm['Jsonform'] = 'absoluteJson'
    dataWorstAbsoluteNorm[""] = "Pessimalfall"
    dataWorstDifferentialCoordinate['Jsonform'] = 'differentialJson'
    dataWorstDifferentialCoordinate[""] = "Pessimalfall"
    dataWorstDifferentialNorm['Jsonform'] = 'differentialJson'
    dataWorstDifferentialNorm[""] = "Pessimalfall"
    df_WorstCoordinate = pd.concat([dataWorstAbsoluteCoordinate, dataWorstDifferentialCoordinate])
    df_WorstNorm = pd.concat([dataWorstAbsoluteNorm, dataWorstDifferentialNorm])


    df_allJsonCoordinate = pd.concat([df_BestCoordinate, df_NormalCoordinate, df_WorstCoordinate])
    df_allJsonNorm = pd.concat([df_BestNorm, df_NormalNorm, df_WorstNorm])

    #PcoreSIZES

    dfBestPcore = pd.read_csv( '/Users/jakobglueck/Desktop/Foldersize/Zeitmessungen/Bestcase/Polar/ZeitMessungen/PolarbeatsPcoreRead.txt', delimiter=',',header=None, names=["JsonFile", "FileSize in bytes"], skiprows=1, dtype={"FileSize in bytes": int})

    maskBestPcoreCoordinate = dfBestPcore['JsonFile'].str.contains('/30MinCoordinate/')
    dataBestPcoreCoordinate = dfBestPcore[maskBestPcoreCoordinate]
    maskBestPcoreNorm = dfBestPcore['JsonFile'].str.contains('/30MinNorm/')
    dataBestPcoreNorm = dfBestPcore[maskBestPcoreNorm]

    dataBestPcoreCoordinate['FileSize in bytes'] = calculateInKilobytes(dataBestPcoreCoordinate['FileSize in bytes'])
    dataBestPcoreNorm['FileSize in bytes'] = calculateInKilobytes(dataBestPcoreNorm['FileSize in bytes'])

    dataBestPcoreCoordinate[""] = "Optimalfall"
    dataBestPcoreNorm[""] = "Optimalfall"

    dfNormalPcore = pd.read_csv( '/Users/jakobglueck/Desktop/Foldersize/Zeitmessungen/normal/Polar/ZeitMessungen/PolarbeatsPcoreRead.txt', delimiter=',',header=None, names=["JsonFile", "FileSize in bytes"], skiprows=1, dtype={"FileSize in bytes": int})

    maskNormalPcoreCoordinate = dfNormalPcore['JsonFile'].str.contains('/30MinCoordinate/')
    dataNormalPcoreCoordinate = dfNormalPcore[maskNormalPcoreCoordinate]
    maskNormalPcoreNorm = dfNormalPcore['JsonFile'].str.contains('/30MinNorm/')
    dataNormalPcoreNorm = dfNormalPcore[maskNormalPcoreNorm]

    dataNormalPcoreCoordinate['FileSize in bytes'] = calculateInKilobytes(dataNormalPcoreCoordinate['FileSize in bytes'])
    dataNormalPcoreNorm['FileSize in bytes'] = calculateInKilobytes(dataNormalPcoreNorm['FileSize in bytes'])

    dataNormalPcoreCoordinate[""] = "Realfall"
    dataNormalPcoreNorm[""] = "Realfall"


    dfWorstPcore = pd.read_csv( '/Users/jakobglueck/Desktop/Foldersize/Zeitmessungen/Worstcase/Polar/ZeitMessungen/PolarPcoreRead.txt', delimiter=',',header=None, names=["JsonFile", "FileSize in bytes"], skiprows=1, dtype={"FileSize in bytes": int})

    maskWorstPcoreCoordinate = dfWorstPcore['JsonFile'].str.contains('/30MinCoordinate/')
    dataWorstPcoreCoordinate = dfWorstPcore[maskWorstPcoreCoordinate]
    maskWorstPcoreNorm = dfWorstPcore['JsonFile'].str.contains('/30MinNorm/')
    dataWorstPcoreNorm = dfWorstPcore[maskWorstPcoreNorm]

    dataWorstPcoreCoordinate['FileSize in bytes'] = calculateInKilobytes(dataWorstPcoreCoordinate['FileSize in bytes'])
    dataWorstPcoreNorm['FileSize in bytes'] = calculateInKilobytes(dataWorstPcoreNorm['FileSize in bytes'])

    dataWorstPcoreCoordinate[""] = "Pessimalfall"
    dataWorstPcoreNorm[""] = "Pessimalfall"

    df_allPcoreCoordinate =pd.concat([dataBestPcoreCoordinate,dataNormalPcoreCoordinate,dataWorstPcoreCoordinate])
    df_allPcoreNorm = pd.concat([dataBestPcoreNorm, dataNormalPcoreNorm, dataWorstPcoreNorm])


    fig = plt.figure(figsize=(25,15))
    sb.set(style="darkgrid")
    ax = fig.add_subplot(221)
    ax = sb.violinplot(data=df_allJsonNorm, x='', y="FileSize in bytes", hue="Jsonform", linewidth=1, split=True,inner = "quartile", palette={ "absoluteJson": "b", "differentialJson": ".85"})
    ax.legend([],[], frameon=False)
    ax.set_ylabel("Zeit in s")
    ax.set_title('(a)', fontsize=10,loc="left")
    ax1 = fig.add_subplot(223)
    ax1 = sb.violinplot(data=df_allPcoreNorm, x='', y="FileSize in bytes",inner = "quartile", palette="Blues")
    ax1.set_ylabel("Zeit in s")
    ax1.set_title('(c)', fontsize=10,loc="left")
    sb.set(style="darkgrid")

    ax2 = fig.add_subplot(222)
    ax2 = sb.violinplot(data=df_allJsonCoordinate, x='', y="FileSize in bytes", hue="Jsonform", linewidth=1, split=True,inner = "quartile", palette={ "absoluteJson": "b", "differentialJson": ".85"})
    ax2.legend([], [], frameon=False)
    ax2.set_ylabel("Zeit in s")
    ax2.set_title('(b)', fontsize=10,loc="left")


    ax3 = fig.add_subplot(224)
    ax3 = sb.violinplot(data=df_allPcoreCoordinate, x='', y="FileSize in bytes",inner = "quartile", palette="Blues")
    ax3.set_ylabel("Zeit in s")
    ax3.set_title('(d)', fontsize=10,loc="left")
    sb.set(style="darkgrid")
    fig.tight_layout(pad=4.0)
    plt.show()

