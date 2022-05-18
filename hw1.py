import pandas as pd
import pandasql as ps
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

crash = pd.read_csv("car_crashes2.csv")
print(f"Type of crash:{type(crash)}")
print(type(crash))
# print(crash.shape[0])  # shape returns a tuple of the dimensions
# print(crash.head())

print(crash.isnull().any() or crash.isna().any())


crash