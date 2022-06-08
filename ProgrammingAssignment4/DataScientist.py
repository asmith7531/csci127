import pandas as pd
import numpy as np
from numpy import ndarray
from pandas import DataFrame


class DataScientist:

    def __init__(self, dataSetName: str):
        self.dataSetName = dataSetName
        self.dataFrame = pd.read_csv(self.dataSetName)

    def printDataFrame(self) -> None:
        print(self.dataFrame)

    def getDataAsNumpyArray(self) -> ndarray:
        return self.dataFrame.values

    def printDataDescriptors(self) -> None:
        print(self.dataFrame.describe())

    def getColumnStat(self) -> DataFrame:
        pass