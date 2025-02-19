import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans

# Load the Metadata CSV file
file_path = '.\\meta\\VMB_META3.csv'
df = pd.read_csv(file_path)

# Filter rows for model 1
# Model 1 sample metadata

# Filter rows where GA < 37 months
filtered_model1 = df[df['Sample_GA'] < 37]

# Pick the row closest to 37 for each Subject ID that occurs multiple times
filtered_model1 = filtered_model1.loc[filtered_model1.groupby("Subject_ID")["Sample_GA"].idxmax()]

# Save the filtered rows to a new CSV file
filtered_model1.to_csv('.\\meta\\VMB_Model1_Meta.csv', index=False)

# Filter rows for model 2
# Model 2 sample metadata

filtered_model2 = df[((df['Sample_GA'] < 34) & ((df['Group2'] == 'PTL') | (df['Group2'] == 'PPROM')))
                     | (df['Group2'] == 'Control')]
filtered_model2 = filtered_model2.loc[filtered_model2.groupby("Subject_ID")["Sample_GA"].idxmax()]
filtered_model2.to_csv('.\\meta\\VMB_Model2_Meta.csv', index=False)