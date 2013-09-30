class Predictor(object):
    "The predictor is fed DataSets and algorithm options"

    def __init__(self, dataSet):
        self.baseData = dataSet
        
    def makePrediction(self):
        return self.baseData.data
        
    