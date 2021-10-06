import os
import pandas as pd

# you have NOT uploaded data.zip (check where it is expected)
def test_if_reduced_data_folder():
    assert not os.path.exists("./session_1/reduced_data")

# you have NOT uploaded model.h5 file (check where it is expected)
def test_if_model_does_not_exist():
    assert not os.path.exists("./session_1/model_pytorch.h5")

# your accuracy of the model is more than 70% (read from metrics)
def test_model_accuracy():
    data = pd.read_csv("./session_1/metrics.csv")
    assert data.iloc[-1]["Accuracy"] > 0.7

# the accuracy of your model for cat and dog is independently more than 70% 
# (read from metrics.csv file)
def test_model_accuracy_cat():
    data = pd.read_csv("./session_1/metrics.csv")
    assert data.iloc[-1]["CAT_Accuracy"] > 0.7

def test_model_accuracy_dog():
    data = pd.read_csv("./session_1/metrics.csv")
    assert data.iloc[-1]["DOG_Accuracy"] > 0.7
