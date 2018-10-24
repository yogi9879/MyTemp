import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def Model(dataset):

	del dataset["Alley"]
	del dataset["PoolQC"]
	del dataset["Fence"]
	del dataset["MiscFeature"]
	del dataset["FireplaceQu"]

	dataset["LotFrontage"].fillna(dataset["LotFrontage"].mode()[0],inplace=True)
	dataset["MasVnrType"].fillna(dataset["MasVnrType"].mode()[0],inplace=True)
	dataset["MasVnrArea"].fillna(dataset["MasVnrArea"].mean(),inplace=True)
	dataset["BsmtQual"].fillna(dataset["BsmtQual"].mode()[0],inplace=True)
	dataset["BsmtCond"].fillna(dataset["BsmtCond"].mode()[0],inplace=True)

	for i in range(0,76):
		if dataset.iloc[:,i].dtype==object:
			dataset.iloc[:,i] = dataset.iloc[:,i].astype('category')
			dataset.iloc[:,i]=dataset.iloc[:,i].cat.codes

	dataset=dataset.dropna()
	train_y=dataset.iloc[:,-1]
	# Feature Scaling
	from sklearn.preprocessing import StandardScaler
	sc_X = StandardScaler()
	sc_y = StandardScaler()
	#test = sc_X.fit_transform(test)
	dataset = sc_y.fit_transform(dataset)


	dataset=pd.DataFrame(dataset)
	correlation=dataset.corr(method="pearson")
	correlation.iloc[:,1]
	train_x=dataset.iloc[:,0:75] 




	from sklearn.svm import SVR
	svr_reg=SVR(kernel = 'rbf')
	svr_reg.fit(train_x,train_y)

	from sklearn.cross_validation import cross_val_score
	accuracies_train = cross_val_score(estimator =svr_reg , X = train_x, y = train_y, cv = 10)

	#y_lpredict=svr_reg.predict(test)
	
	return accuracies_train
