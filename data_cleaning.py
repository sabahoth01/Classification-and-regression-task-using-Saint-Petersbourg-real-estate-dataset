import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.impute import KNNImputer
import seaborn as sns
from tabulate import tabulate

data = pd.read_csv(r"D:\University\Sem1\Machine-learning\dataset\spb_real_estate_data.csv")
print(data)