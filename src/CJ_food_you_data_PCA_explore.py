#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 14:56:50 2020

@author: charliejeynes@hotmail.com

This script is adapted from https://towardsdatascience.com/pca-using-python-scikit-learn-e653f8989e60

It essentailly performs PCA on the data from the FSA Food and You survey,
after some columns (variobales) are dropped that are not appropriate (e.g. serial number)
Then it plots PC1 against PC2 with the gender as the label.

"""

import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# import data
df = pd.read_csv('/Users/charliejeynes/Documents/Pivago local documents/data/food survey/Food+and+You+Waves+1-5+Data (3).csv')

# select wales only entries
df_wales = df.loc[df['region_dv'] == 10]

# get rid of all columns not wanted for the PCA transformation
df_wales_drop = df_wales.drop(['SerialNo', \
                               'RespSex', \
                               'psu_dv', 'stratum_all_dv', \
                               'combinedW1_5weight', \
                               'countryW1_5weight'], 1)
    
# Standardizing the features
df_wales_drop_st = StandardScaler().fit_transform(df_wales_drop)    

# running the PCA 
pca = PCA(n_components=2)
principalComponents = pca.fit_transform(df_wales_drop_st)
principalDf = pd.DataFrame(data = principalComponents
             , columns = ['principal component 1', 'principal component 2']) 

# create a labels columns (i.e. gender) for new PCA dataframe 
to_concate =  df_wales[['RespSex']]

# concatenate the 'target' column (i.e. gender) to the transformed data
finalDf = pd.concat([principalDf.reset_index(drop=True), to_concate.reset_index(drop=True)], axis = 1)
#[df1.reset_index(drop=True), df2.reset_index(drop=True)]


# replace 0,1 with male, female
finalDF_gender = finalDf.replace({'RespSex': {1: 'male', 2: 'female'}})


# plot principle component one against two
fig = plt.figure(figsize = (8,8))
ax = fig.add_subplot(1,1,1) 
ax.set_xlabel('Principal Component 1', fontsize = 15)
ax.set_ylabel('Principal Component 2', fontsize = 15)
ax.set_title('2 component PCA on all Food and You data', fontsize = 20)
targets = ['female', 'male']
colors = ['r', 'g']
for target, color in zip(targets,colors):
    indicesToKeep = finalDF_gender['RespSex'] == target
    ax.scatter(finalDF_gender.loc[indicesToKeep, 'principal component 1']
               , finalDF_gender.loc[indicesToKeep, 'principal component 2']
               , c = color
               , s = 50)
ax.legend(targets)
ax.grid()