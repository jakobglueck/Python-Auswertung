import matplotlib.pyplot as plt
import seaborn as sb
import pandas as pd


def calculateInKilobytes(dataValues):
    dataInKb = []
    for value in dataValues:
        dataInKb.append(value / 1000000000)
    return dataInKb


if __name__ == '__main__':

    #JSONSIZES
    dfBestAbsolute = pd.read_csv('/Users/jakobglueck/Desktop/Foldersize/Zeitmessungen/Bestcase/Corsano/ZeitMessungen/CorsanoJsonRead.txt', delimiter=',',header=None, names=["JsonFile", "FileSize in bytes"], skiprows=1, dtype={"FileSize in bytes": int})
    dfBestDifferential = pd.read_csv('/Users/jakobglueck/Desktop/Foldersize/Zeitmessungen/Bestcase/Corsano/ZeitMessungen/CorsanoDifferentialJsonRead.txt', delimiter=',', header=None, names=["JsonFile","FileSize in bytes"],skiprows=1, dtype={"FileSize in bytes": int})

    dfBestAbsolute['FileSize in bytes'] = calculateInKilobytes(dfBestAbsolute['FileSize in bytes'])
    dfBestDifferential['FileSize in bytes'] = calculateInKilobytes(dfBestDifferential['FileSize in bytes'])

    dfBestAbsolute['Jsonform'] = 'absoluteJson'
    dfBestAbsolute[""] = "Optimalfall"

    dfBestDifferential['Jsonform'] = 'differentialJson'
    dfBestDifferential[""] = "Optimalfall"

    df_Best= pd.concat([dfBestAbsolute,dfBestDifferential])


    dfNormalAbsolute = pd.read_csv('/Users/jakobglueck/Desktop/Foldersize/Zeitmessungen/normal/Corsano/ZeitMessungen/CorsanoJsonRead.txt', delimiter =',', header=None, names=["JsonFile","FileSize in bytes"],skiprows=1, dtype={"FileSize in bytes": int})
    dfNormalDifferential = pd.read_csv('/Users/jakobglueck/Desktop/Foldersize/Zeitmessungen/normal/Corsano/ZeitMessungen/CorsanoDifferentialJsonRead.txt', delimiter=',', header=None, names=["JsonFile","FileSize in bytes"],skiprows=1, dtype={"FileSize in bytes": int})

    dfNormalAbsolute['FileSize in bytes'] = calculateInKilobytes(dfNormalAbsolute['FileSize in bytes'])
    dfNormalDifferential['FileSize in bytes'] = calculateInKilobytes(dfNormalDifferential['FileSize in bytes'])

    dfNormalAbsolute['Jsonform'] = 'absoluteJson'
    dfNormalAbsolute[""] = "Realfall"

    dfNormalDifferential['Jsonform'] = 'differentialJson'
    dfNormalDifferential[""] = "Realfall"

    df_Normal= pd.concat([dfNormalAbsolute,dfNormalDifferential])


    dfWorstAbsolute = pd.read_csv('/Users/jakobglueck/Desktop/Foldersize/Zeitmessungen/Worstcase/Corsano/ZeitMessungen/CorsanoJsonRead.txt', delimiter=',', header=None, names=["JsonFile", "FileSize in bytes"], skiprows=1, dtype={"FileSize in bytes": int})
    dfWorstDifferential = pd.read_csv('/Users/jakobglueck/Desktop/Foldersize/Zeitmessungen/Worstcase/Corsano/ZeitMessungen/CorsanoDifferentialJsonRead.txt',delimiter=',', header=None, names=["JsonFile", "FileSize in bytes"], skiprows=1,dtype={"FileSize in bytes": int})

    dfWorstAbsolute['FileSize in bytes'] = calculateInKilobytes(dfWorstAbsolute['FileSize in bytes'])
    dfWorstDifferential['FileSize in bytes'] = calculateInKilobytes(dfWorstDifferential['FileSize in bytes'])

    dfWorstAbsolute['Jsonform'] = 'absoluteJson'
    dfWorstAbsolute[""] = "Pessimalfall"

    dfWorstDifferential['Jsonform'] = 'differentialJson'
    dfWorstDifferential[""] = "Pessimalfall"

    df_Worst= pd.concat([dfWorstAbsolute,dfWorstDifferential])

    #PcoreSIZES

    dfBestPcore = pd.read_csv( '/Users/jakobglueck/Desktop/Foldersize/Zeitmessungen/Bestcase/Corsano/ZeitMessungen/CorsanoPcoreRead.txt', delimiter=',',header=None, names=["JsonFile", "FileSize in bytes"], skiprows=1, dtype={"FileSize in bytes": int})


    dfBestPcore['FileSize in bytes'] = calculateInKilobytes(dfBestPcore['FileSize in bytes'])

    dfBestPcore[""] = "Optimalfall"

    dfNormalPcore = pd.read_csv( '/Users/jakobglueck/Desktop/Foldersize/Zeitmessungen/normal/Corsano/ZeitMessungen/CorsanoPcoreRead.txt', delimiter=',',header=None, names=["JsonFile", "FileSize in bytes"], skiprows=1, dtype={"FileSize in bytes": int})

    dfNormalPcore['FileSize in bytes'] = calculateInKilobytes(dfNormalPcore['FileSize in bytes'])

    dfNormalPcore[""] = "Realfall"

    dfWorstPcore = pd.read_csv( '/Users/jakobglueck/Desktop/Foldersize/Zeitmessungen/Worstcase/Corsano/ZeitMessungen/CorsanoPcoreRead.txt', delimiter=',',header=None, names=["JsonFile", "FileSize in bytes"], skiprows=1, dtype={"FileSize in bytes": int})

    dfWorstPcore['FileSize in bytes'] = calculateInKilobytes(dfWorstPcore['FileSize in bytes'])

    dfWorstPcore[""] = "Pessimalfall"


    df_allPcore =pd.concat([dfBestPcore,dfNormalPcore,dfWorstPcore])

    df_allabsoluteJon = pd.concat([df_Best, df_Normal, df_Worst])

    fig = plt.figure(figsize=(25, 15))
    sb.set(style="darkgrid")
    ax = fig.add_subplot(221)
    ax = sb.violinplot(data=df_allabsoluteJon, x='', y="FileSize in bytes", hue="Jsonform", linewidth=1, split=True,
                       inner="quartile", palette={"absoluteJson": "b", "differentialJson": ".85"})
    ax.legend([], [], frameon=False)
    ax.set_ylabel("Zeit in s")
    ax.set_title('(a)', fontsize=10, loc="left")

    ax2 = fig.add_subplot(222)
    sb.violinplot(data=df_allPcore, x='', y="FileSize in bytes", inner="quartile", palette="Blues")
    ax2.set_ylabel("Zeit in s")
    ax2.set_title('(b)', fontsize=10, loc="left")
    sb.set(style="darkgrid")

    fig.tight_layout(pad=4.0)
    plt.show()