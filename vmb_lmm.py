import pandas as pd
from scipy.stats import f_oneway
import statsmodels.api as sm
from statsmodels.formula.api import mixedlm
import matplotlib.pyplot as plt
#import seaborn as sns
from statsmodels.stats.multitest import multipletests

def create_group_data(meta_df, original_df):
    
    # Extract the list of substrings from the first column
    substrings = meta_df.iloc[:, 0].apply(lambda x: x[1:] if len(x) > 1 else '').tolist()

    # Filter columns based on the substrings
    # Iterate over each column in the original DataFrame
    # Initialize an empty list to store the filtered column names
    filtered_columns = ['PC']
    for col in original_df.columns:
        # Check if any of the substrings is present in the column name
        for substring in substrings:
            if col.startswith(substring + "_"):
                filtered_columns.append(col)
                break  # Break the inner loop to avoid adding the same column multiple times

    filtered_df = original_df[filtered_columns]
    return filtered_df

def get_gene_data_for_lmm(dfM, metaDf, gene_200):
    data = []
    for gene_name in gene_200['Gene']:
        # Extract the rows as arrays (excluding the gene name) for the specified gene
        countsM = dfM[dfM.iloc[:, 0] == gene_name].iloc[:, 1:].values.flatten()
      
        i=1
        for gene_count in countsM:
            data.append([gene_name, dfM.columns[i],'PTL_Early', gene_count])
            i=i+1
    
    # Create DataFrame
    df = pd.DataFrame(data, columns=['Gene', 'SampleId', 'Group', 'GeneCount'])

    # Convert categorical variables
    df['Gene'] = df['Gene'].astype('category')
    df['Group'] = df['Group'].astype('category')

    print(df)
    return df


# Load the Summary 200 DataFrame
original_file_path = "Summary.filtered_gene_200.csv"
original_df = pd.read_csv(original_file_path)

# Filter data set according to the 2 models
meta_df1 = pd.read_csv('.\\meta\\VMB_Model1_Meta.csv');
meta_df2 = pd.read_csv('.\\meta\\VMB_Model2_Meta.csv');
group_model1 = create_group_data(meta_df1, original_df)
group_model2 = create_group_data(meta_df2, original_df)

# Read the gene names
gene_200 = pd.read_csv('.\\meta\\Gene_200.csv')

df_for_lmm = get_gene_data_for_lmm(group_model1, meta_df1, gene_200)

# Define and Fit the Mixed Effects Model
# model = mixedlm("GeneCount ~ Group", df_for_lmm, groups=df_for_lmm["Gene"])
# result = model.fit()

# Print Model Summary
# print(result.summary())
