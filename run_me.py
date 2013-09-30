from Predictors import Predictor
from DataSets import DataSet
import Visualizers as visualisers
       
if __name__ == "__main__":
    dataSet = DataSet()
    predictor = Predictor(dataSet)
    visualisers.visualize(predictor.makePrediction())