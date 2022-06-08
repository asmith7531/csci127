from DataScientist import DataScientist

irisCSV = 'iris_species.csv'
irisDS = DataScientist('datasets/' + irisCSV)
irisDS.printDataFrame()
irisDS.printDataDescriptors()

