from DataScientist import DataScientist

irisCSV = 'iris_species'
irisDS = DataScientist(irisCSV)
irisDS.printDataDescriptors()
"""
irisDS.printDataFrame()
print(irisDS.getColumnStat("sepal-length", "mean"))
print(irisDS.getDataSortedByColumn("sepal-length"))
print(irisDS.getQuery("`sepal-length`", ">", "5"))
print(irisDS.getDataAsNumpyArray())
print(irisDS.replaceIncompleteInstances("mean"))
"""

#irisDS.graphColumnHistogram("sepal-length")
irisDS.graphAllHistograms()
irisDS.graphTwoColumnsAsScatterPlot("sepal-width", "sepal-length")
irisDS.graphAllPairwiseScatterPlots()