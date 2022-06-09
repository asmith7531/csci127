import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from numpy import ndarray
from pandas import DataFrame


class DataScientist:

    def __init__(self, dataSetName: str):
        self.dataSetName = dataSetName
        self.dataFrame = pd.read_csv('datasets/' + self.dataSetName + ".csv")

    def printDataFrame(self) -> None:
        print(self.dataFrame)

    def getDataAsNumpyArray(self) -> ndarray:
        return self.dataFrame.values

    def printDataDescriptors(self) -> None:
        print(self.dataFrame.describe())

    def getColumnStat(self, column: str, statistic: str) -> DataFrame:
        descriptiveStats = self.dataFrame.describe()
        thisColumnsStat = descriptiveStats.at[statistic, column]
        return thisColumnsStat

    def getDataSortedByColumn(self, column: str) -> DataFrame:
        descriptiveStats = self.dataFrame.filter(regex=column)
        return descriptiveStats

    def getQuery(self, column: str, boolOperator: str, value: str) -> DataFrame:
        query = column + boolOperator + value
        print(query)
        return self.dataFrame.query(query)

    def removeColumn(self, column: str | list) -> DataFrame:
        return self.DataFrame.drop(columns=[column])

    def removeIncompleteMissing(self) -> DataFrame:
        return self.dataFrame.dropna()

    def replaceIncompleteInstances(self, stat: str) -> DataFrame:
        replacedDataFrame = self.dataFrame.copy()
        for column in self.dataFrame.columns:
            thisColumnStat = self.getColumnStat(column, stat)
            replacedDataFrame.fillna(thisColumnStat, inplace=True)
        return replacedDataFrame

    def graphColumnHistogram(self, column: str, bins=12) -> None:
        self.dataFrame.plot.hist(column=column, by="label", bins=bins, figsize=(15, 15))
        plt.savefig("figs/" + self.dataSetName + "_hist_" + column + ".png")
        return

    def graphAllHistograms(self) -> None:
        for column in self.dataFrame:
            if column != 'label':
                self.graphColumnHistogram(column)
        return

    def graphTwoColumnsAsScatterPlot(self, xAxisColumn: str, yAxisColumn: str) -> None:
        self.dataFrame.plot.scatter(x=xAxisColumn, y=yAxisColumn, c="label", cmap="viridis")
        plt.savefig("figs/" + self.dataSetName + "_scatter_" + xAxisColumn + "_" + yAxisColumn + ".png")
        return

    def graphAllPairwiseScatterPlots(self) -> None:
        lastX = []
        for xcolumn in self.dataFrame:
            lastX.append(xcolumn)
            for ycolumn in self.dataFrame:
                if (xcolumn != ycolumn) and (ycolumn not in lastX) and (ycolumn != 'label') and (xcolumn != 'label'):
                    self.graphTwoColumnsAsScatterPlot(xcolumn, ycolumn)
            print(lastX)
        return