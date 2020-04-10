from sklearn import svm
from sklearn.preprocessing import MinMaxScaler
from parse_data import parse_data
from calc_error_pct import *
#import tkMessageBox
import time


class SVMHandler:
    """ In this class you will implement the classifier and it's methods. """
    def __init__(self):
        self.x_train, self.y_train = parse_data("data\\adult.data")
        self.x_test, self.y_test = parse_data("data\\adult.test")
        self.svclassifier = svm.LinearSVC()
        scaling_x_train = MinMaxScaler(feature_range=(-1,1)).fit(self.x_train)
        self.x_train = scaling_x_train.transform(self.x_train)
        self.x_test = scaling_x_train.transform(self.x_test)

    def _train(self):
        self.svclassifier.fit(self.x_train, self.y_train)

    def _predict(self):
        #call the library's predict method
        self.y_pred = self.svclassifier.predict(self.x_test)
        #normalize the prediction in order to fit to the y_train
        for i in range(0,len(self.y_pred)):
            if self.y_pred[i]>0:
                self.y_pred[i]=1
            else:
                self.y_pred[i]=0

    def _measure_accuracy(self):
        return calculate_error_percentage(self.y_test,self.y_pred)

    def run(self):
        self._train()
        self._predict()
        return self._measure_accuracy()


start_time = time.time()
handler = SVMHandler()
result = handler.run()
print(result)
print("--- %s seconds ---" % (time.time() - start_time))

