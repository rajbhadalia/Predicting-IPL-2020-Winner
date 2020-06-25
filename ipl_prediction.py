#Name: Maharshi reddy Baddam
#NetID: MXB180036
 
#Name: Kalyankumar kancharla
#NetID: KXK190004

import pandas as pd
import numpy as np
from sklearn import preprocessing
from sklearn.linear_model import SGDRegressor
from sklearn.metrics import mean_squared_error
from sklearn.neighbors import KNeighborsRegressor
from collections import Counter 
import itertools
import statistics
from prettytable import PrettyTable
import matplotlib.pyplot as plt
import math
from sklearn.model_selection import train_test_split
import scipy.stats as st
from sklearn.utils import resample


#Exploratory Data Analysis

#Batting Data

Batsmen_data=pd.read_csv("Batsmen_Data.csv")
Batsmen_data.shape

#Drop the Matches_Bat feature as it is not an important feature

Batsmen_data.drop(['Matches_Bat'],axis=1,inplace=True)
Batsmen_data.head()

#Get the unique values of Double_Centuries_Bat

Batsmen_data['Double_Centuries_Bat'].unique()


#We have only 0 values in Double Centuries column. So, it is not a valid feature. We can drop this feature

Batsmen_data.drop(['Double_Centuries_Bat'],axis=1,inplace=True)
Batsmen_data.head()

Batsmen_data['Centuries_Bat'].value_counts()

#We can see that almost 81% of the players didn't score a century. So we can drop this feature as it does not provide any value

Batsmen_data.drop(['Centuries_Bat'],axis=1,inplace=True)
Batsmen_data

#Bowling Data

Bowler_data=pd.read_csv("Bowling_Data.csv")
Bowler_data.head()

#Drop the Matches_Bowl feature as it is not an important feature

Bowler_data.drop(['Matches_Bowl'],axis=1,inplace=True)
Bowler_data.head()


#Get the unique values of TenWickets_Bowl

Bowler_data['TenWickets_Bowl'].unique()


#We have only 0's in TenWickets_Bowl. So, it is not a valid feature. We can drop this feature

Bowler_data.drop(['TenWickets_Bowl'],axis=1,inplace=True)
Bowler_data.head()

Bowler_data['FiveWickets_Bowl'].value_counts()

Bowler_data.drop(['FiveWickets_Bowl'],axis=1,inplace=True)
Bowler_data.head()

#AllRounder Data

AllRounder_data=pd.read_csv("Allrounder_Data.csv")
AllRounder_data

#Drop the Matches_As_Bat_AllRounder feature as it is not an important feature

AllRounder_data.drop(['Matches_As_Bat_AllRounder'],axis=1,inplace=True)
AllRounder_data.head()


#Get the unique values of Double_Centuries_AllRounder

AllRounder_data['Double_Centuries_AllRounder'].unique()

#We have only 0's in Double_Centuries_AllRounder. So, it is not a valid feature. We can drop this feature


AllRounder_data.drop(['Double_Centuries_AllRounder'],axis=1,inplace=True)
AllRounder_data.head()
AllRounder_data['Centuries_AllRounder'].value_counts()


#We can see that almost 87% of the players didn't score a century. So we can drop this feature as it does not provide any value

AllRounder_data.drop(['Centuries_AllRounder'],axis=1,inplace=True)
AllRounder_data.head()


#Get the unique values of TenWickets_AllRounder

AllRounder_data['TenWickets_AllRounder'].unique()


#We have only 0's in TenWickets_AllRounder. So, it is not a valid feature. We can drop this feature

AllRounder_data.drop(['TenWickets_AllRounder'],axis=1,inplace=True)
AllRounder_data.head()


#Get the unique values of FiveWickets_AllRounder

AllRounder_data['FiveWickets_AllRounder'].unique()
AllRounder_data['FiveWickets_AllRounder'].value_counts()


#We can see that almost 91% of the players didn't score a Half Century. So we can drop this feature as it does not provide any value

AllRounder_data.drop(['FiveWickets_AllRounder'],axis=1,inplace=True)
AllRounder_data


#Delete the rows which have 0 values

Batsmen_data=Batsmen_data[Batsmen_data['Fifties_Bat'] !=0]
Batsmen_data

AllRounder_data=AllRounder_data[AllRounder_data['Fifties_AllRounder'] !=0]
AllRounder_data=AllRounder_data[AllRounder_data['Fours_AllRounder'] !=0]


#Visualize the Data

plt.hist(Batsmen_data['Batting_Average_Bat'],density=False, bins=30, label="Data")
plt.xlabel("Batting_Average_Batsmen")
plt.title("Histogram of Batting Averages for Batsmen")
plt.ylabel("Counts")
plt.show()

plt.hist(AllRounder_data['Batting_Average_AllRounder'],density=False, bins=30, label="Data")
plt.xlabel("Batting_Average_AllRounder")
plt.ylabel("Counts")
plt.title("Histogram of Batting Averages for All Rounders")
plt.show()


# Observation: Batting Averages for Batsmen and AllRounders are Right Skewed

plt.hist(Batsmen_data['Runs_Scored_Bat'],density=False, bins=30, label="Data")
plt.xlabel("Runs_Scored_Bat")
plt.ylabel("Counts")
plt.title("Histogram of Runs Scored for Batsmen")
plt.show()

plt.hist(AllRounder_data['Runs_Scored_AllRounder'],density=False, bins=40, label="Data")
plt.xlabel("Runs_Scored_AllRounder")
plt.ylabel("Counts")
plt.title("Histogram of Runs Scored for AllRounder")
plt.show()


# Observation: Runs Scored for Batsmen and AllRounders are Right Skewed

plt.hist(Batsmen_data['Batting_Strike_Rate_Bat'],density=False, bins=40, label="Data")
plt.xlabel("Batting_Strike_Rate_Bat")
plt.ylabel("Counts")
plt.title("Histogram of Batting Strike Rate for Batsmen")
plt.show()

plt.hist(AllRounder_data['Batting_Strike_Rate_AllRounder'],density=False, bins=40, label="Data")
plt.xlabel("Batting_Strike_Rate_AllRounder")
plt.ylabel("Counts")
plt.title("Histogram of Batting Strike Rate for AllRounder")
plt.show()


# Observation: Batting Strike rate for Batsmen and AllRounders are approximately normally distributed

plt.hist(Batsmen_data['Fifties_Bat'],density=False, bins=40, label="Data")
plt.xlabel("Fifties_Bat")
plt.ylabel("Counts")
plt.title("Histogram of Number of Fifties Scored by Batsmen")
plt.show()

plt.hist(AllRounder_data['Fifties_AllRounder'],density=False, bins=40, label="Data")
plt.xlabel("Fifties_AllRounder")
plt.ylabel("Counts")
plt.title("Histogram of Number of Fifties Scored by AllRounder")
plt.show()


# Observation: Number of Fifties Scored by Batsmen and AllRounders are Right Skewed

plt.hist(Batsmen_data['Fours_Bat'],density=False, bins=40, label="Data")
plt.xlabel("Fours_Bat")
plt.ylabel("Counts")
plt.title("Histogram of Number of Fours Scored by Batsmen")
plt.show()

plt.hist(AllRounder_data['Fours_AllRounder'],density=False, bins=40, label="Data")
plt.xlabel("Fours_AllRounder")
plt.ylabel("Counts")
plt.title("Histogram of Number of Fours Scored by AllRounder")
plt.show()


# Observation: Number of Fours Scored by Batsmen and AllRounders are Right Skewed


plt.hist(Batsmen_data['Sixes_Bat'],density=False, bins=40, label="Data")
plt.xlabel("Sixes_Bat")
plt.ylabel("Counts")
plt.title("Histogram of Number of Sixes Scored by Batsmen")
plt.show()

plt.hist(AllRounder_data['Sixes_AllRounder'],density=False, bins=40, label="Data")
plt.xlabel("Sixes_AllRounder")
plt.ylabel("Counts")
plt.title("Histogram of Number of Sixes Scored by AllRounder")
plt.show()


# Observation: Number of Sixes Scored by Batsmen and AllRounders are Right Skewed

plt.hist(Bowler_data['Wickets_Bowl'],density=False, bins=40, label="Data")
plt.xlabel("Wickets_Bowl")
plt.ylabel("Counts")
plt.title("Histogram of Wickets Taken by Bowlers")
plt.show()

plt.hist(AllRounder_data['Wickets_AllRounder'],density=False, bins=40, label="Data")
plt.xlabel("Wickets_AllRounder")
plt.ylabel("Counts")
plt.title("Histogram of Wickets Taken by AllRounders")
plt.show()


# Observation: Number of Wickets Taken by Bowlers and AllRounders are Right Skewed

plt.hist(Bowler_data['Economy_Bowl'],density=False, bins=40, label="Data")
plt.xlabel("Economy_Bowl")
plt.ylabel("Counts")
plt.title("Histogram of Economy of Bowlers")
plt.show()

plt.hist(AllRounder_data['Economy_AllRounder'],density=False, bins=40, label="Data")
plt.xlabel("Economy_AllRounder")
plt.ylabel("Counts")
plt.title("Histogram of Economy of AllRounders")
plt.show()


# Observation: Economy of Bowlers and AllRounders are approximately normally distributed


plt.hist(Bowler_data['Bowling_Average_Bowl'],density=False, bins=40, label="Data")
plt.xlabel("Bowling_Average_Bowl")
plt.ylabel("Counts")
plt.title("Histogram of Bowling Average of Bowlers")
plt.show()

plt.hist(AllRounder_data['Bowling_Average_AllRounder'],density=False, bins=40, label="Data")
plt.xlabel("Bowling_Average_AllRounder")
plt.ylabel("Counts")
plt.title("Histogram of Bowling Average of AllRounders")
plt.show()


# Observation: Bowling Average of Bowlers is approximately normally distributed whereas the Bowling Average of AllRounders is Right Skewed

plt.hist(Bowler_data['Bowling_Strike_Rate_Bowl'],density=False, bins=40, label="Data")
plt.xlabel("Bowling_Strike_Rate_Bowl")
plt.ylabel("Counts")
plt.title("Histogram of Bowling Strike Rate of Bowlers")
plt.show()

plt.hist(AllRounder_data['Bowling_Strike_Rate_AllRounder'],density=False, bins=40, label="Data")
plt.xlabel("Bowling_Strike_Rate_AllRounder")
plt.ylabel("Counts")
plt.title("Histogram of Bowling Strike Rate of AllRounders")
plt.show()


#Observation: Bowling Strike Rate of Bowlers is approximately normally distributed whereas the Bowling Average of AllRounders is Right Skewed

#We have skewness in the data and the models are not working properly. So, lets apply log transformation

#Using Log Transformation

x = Batsmen_data.values
x_log = np.log(x)
df_log = pd.DataFrame(x_log)
df_log.columns=["a","b","c","d","e","f","g","h"]

plt.hist(df_log["d"],density=False, bins=30, label="Data")
plt.xlabel("Batting_Average_Batsmen_Log")
plt.title("Histogram of Batting Averages for Batsmen")
plt.ylabel("Counts")
plt.show()

bat_avg_Batsmen=Batsmen_data['Batting_Average_Bat']
print("Skewness with Original Data:",bat_avg_Batsmen.skew())
bat_avg_Batsmen_log=df_log['d']
print("Skewness with LogTransformed Data:",bat_avg_Batsmen_log.skew())


#Skewness was greately reduced using Log Transformation. So apply Log Transformtaion to our data before building the models


Batsmen_data.to_csv("Batsmen_Data_After_Processing.csv",index = False)
Bowler_data.to_csv("Bowler_Data_After_Processing.csv",index=False)
AllRounder_data.to_csv("AllRounder_Data_After_Processing.csv",index=False)


#Models:


def sklearnSGDRegressor(Xtrn,ytrn,Xcv,ycv,epochs):
    iters=epochs
    rmse_train_SGD=[]
    rmse_cv_SGD=[]

    SGDReg_sklearn_train_table=PrettyTable()
    SGDReg_sklearn_train_table.field_names = ["Epochs","Train Error"]
    SGDReg_sklearn_cv_table=PrettyTable()
    SGDReg_sklearn_cv_table.field_names = ["Epochs","CV Error"]

    best_epoch_train_SGD_sklearn=0
    best_rmse_train_SGD_sklearn=float('inf')

    best_epoch_cv_SGD_sklearn=0
    best_rmse_cv_SGD_sklearn=float('inf')

    for i in iters:
        sgd_reg_train = SGDRegressor(shuffle = False,max_iter = i)
        sgd_reg_train.fit(Xtrn, ytrn)
        y_pred_trn_sgd_sklearn = sgd_reg_train.predict(Xtrn)
        y_pred_cv_sgd_sklearn = sgd_reg_train.predict(Xcv)
        rmse_train_SGD.append(math.sqrt(mean_squared_error(ytrn,y_pred_trn_sgd_sklearn)))
        rmse_cv_SGD.append(math.sqrt(mean_squared_error(ycv,y_pred_cv_sgd_sklearn)))
        SGDReg_sklearn_train_table.add_row([i,math.sqrt(mean_squared_error(ytrn,y_pred_trn_sgd_sklearn))])
        SGDReg_sklearn_cv_table.add_row([i,math.sqrt(mean_squared_error(ycv,y_pred_cv_sgd_sklearn))])
        if(math.sqrt(mean_squared_error(ytrn,y_pred_trn_sgd_sklearn))<best_rmse_train_SGD_sklearn):
            best_epoch_train_SGD_sklearn=i
            best_rmse_train_SGD_sklearn=math.sqrt(mean_squared_error(ytrn,y_pred_trn_sgd_sklearn))
        if(math.sqrt(mean_squared_error(ycv,y_pred_cv_sgd_sklearn))<best_rmse_cv_SGD_sklearn):
            best_epoch_cv_SGD_sklearn=i
            best_rmse_cv_SGD_sklearn=math.sqrt(mean_squared_error(ycv,y_pred_cv_sgd_sklearn))
        
    plt.plot(iters,rmse_train_SGD,label="Train RMSE")
    plt.plot(iters,rmse_cv_SGD,label="CV RMSE")
    plt.title("RMSE with epochs")
    plt.xlabel("epochs: Hyperparameter")
    plt.ylabel("RMSE")
    plt.legend()
    plt.show()

    print(SGDReg_sklearn_train_table)
    print(SGDReg_sklearn_cv_table)
    print("Best No.of Epochs is:",best_epoch_cv_SGD_sklearn)
    return best_epoch_cv_SGD_sklearn


def SGDRegressionOwn(train_data,learning_rate,total_iter,k):
    num_iter=1
    weights=np.zeros(shape=(1,train_data.shape[1]-1))
    intercept=0
    while(num_iter<=total_iter):
        sample_data=train_data.sample(k,replace=True)
        y=np.array(sample_data['regresult'])
        x=np.array(sample_data.drop('regresult',axis=1))
        w_gradient=np.zeros(shape=(1,train_data.shape[1]-1))
        b_gradient=0
        for i in range(k):
            error=y[i]-np.dot(weights,x[i])-intercept
            w_gradient=w_gradient+(-2)*x[i]*error
            b_gradient=b_gradient+(-2)*(error)
        weights=weights-learning_rate*(w_gradient/k)
        intercept=intercept-learning_rate*(b_gradient/k)
        num_iter+=1
    
    return weights,intercept


def predictSGDOwn(x,w,b):
    y_pred=[]
    for i in range(len(x)):
        y=np.asscalar(np.dot(w,x[i])+b)
        y_pred.append(y)
    return np.array(y_pred)


def SGDRegressionOwnTraining(Xtrn,ytrn,Xcv,ycv,epochs):
    iters=[10,100,200,400,800,1600,2000]
    rmse_train_SGD_Own=[]
    rmse_cv_SGD_Own=[]
    
    train_data=pd.DataFrame(Xtrn)
    train_data['regresult']=ytrn
    
    SGDReg_own_train_table=PrettyTable()
    SGDReg_own_train_table.field_names = ["Epochs","Train Error"]
    
    SGDReg_own_cv_table=PrettyTable()
    SGDReg_own_cv_table.field_names = ["Epochs","CV Error"]

    best_epoch_train_SGD_Own=0
    best_rmse_train_SGD_Own=float('inf')

    best_epoch_cv_SGD_Own=0
    best_rmse_cv_SGD_Own=float('inf')

    for i in iters:
        w,b = SGDRegressionOwn(train_data,learning_rate=0.01,total_iter=i,k=10)
        y_pred_trn_sgd_own = predictSGDOwn(Xtrn,w,b)
        y_pred_cv_sgd_own = predictSGDOwn(Xcv,w,b)
        rmse_train_SGD_Own.append(math.sqrt(mean_squared_error(ytrn,y_pred_trn_sgd_own)))
        rmse_cv_SGD_Own.append(math.sqrt(mean_squared_error(ycv,y_pred_cv_sgd_own)))
        SGDReg_own_train_table.add_row([i,math.sqrt(mean_squared_error(ytrn,y_pred_trn_sgd_own))])
        SGDReg_own_cv_table.add_row([i,math.sqrt(mean_squared_error(ycv,y_pred_cv_sgd_own))])
        if(math.sqrt(mean_squared_error(ytrn,y_pred_trn_sgd_own))<best_rmse_train_SGD_Own):
            best_epoch_train_SGD_Own=i
            best_rmse_train_SGD_Own=math.sqrt(mean_squared_error(ytrn,y_pred_trn_sgd_own))
        if(math.sqrt(mean_squared_error(ycv,y_pred_cv_sgd_own))<best_rmse_cv_SGD_Own):
            best_epoch_cv_SGD_Own=i
            best_rmse_cv_SGD_Own=math.sqrt(mean_squared_error(ycv,y_pred_cv_sgd_own))
    plt.plot(epochs,rmse_train_SGD_Own,label="Train RMSE")
    plt.plot(epochs,rmse_cv_SGD_Own,label="CV RMSE")
    plt.title("RMSE with epochs")
    plt.xlabel("epochs: Hyperparameter")
    plt.ylabel("RMSE")
    plt.legend()
    plt.show()
    print(SGDReg_own_train_table)
    print(SGDReg_own_cv_table)

    print("Best No.of Epochs is:",best_epoch_cv_SGD_Own)
    return best_epoch_cv_SGD_Own


def LinearRegressionLSM(Xtrn,ytrn,shape):
    Xtrn=np.concatenate([np.ones((Xtrn.shape[0],1),dtype=Xtrn.dtype),Xtrn], axis=1)
    transpose=Xtrn.transpose()
    prod=np.matmul(transpose,Xtrn)
    prod = prod+0.00001*np.random.rand(shape, shape)
    inverse = np.linalg.inv(prod)
    ytrn=ytrn.reshape(-1,1)
    we=np.matmul(inverse,transpose)
    we=we.dot(ytrn)
    return we


def predict_LSM(x,we):
    x=np.concatenate([np.ones((x.shape[0],1),dtype=x.dtype),x], axis=1)
    yhat=x.dot(we)
    return yhat


def sklearnKNNRegressor(Xtrn,ytrn,Xcv,ycv,neighbors):
    no_of_neighbors=neighbors
    rmse_train_KNN=[]
    rmse_cv_KNN=[]

    KNNReg_sklearn_train_table=PrettyTable()
    KNNReg_sklearn_train_table.field_names = ["Neighbors","Train Error"]

    KNNReg_sklearn_cv_table=PrettyTable()
    KNNReg_sklearn_cv_table.field_names = ["Neighbors","CV Error"]

    best_neighbors_train_KNN_sklearn=0
    best_rmse_train_KNN_sklearn=float('inf')

    best_neighbors_cv_KNN_sklearn=0
    best_rmse_cv_KNN_sklearn=float('inf')

    for i in no_of_neighbors:
        knn_reg_train = KNeighborsRegressor(n_neighbors=i)
        knn_reg_train.fit(Xtrn, ytrn)
        y_pred_trn_KNN_sklearn = knn_reg_train.predict(Xtrn)
        y_pred_cv_KNN_sklearn = knn_reg_train.predict(Xcv)
        rmse_train_KNN.append(math.sqrt(mean_squared_error(ytrn,y_pred_trn_KNN_sklearn)))
        rmse_cv_KNN.append(math.sqrt(mean_squared_error(ycv,y_pred_cv_KNN_sklearn)))
        KNNReg_sklearn_train_table.add_row([i,math.sqrt(mean_squared_error(ytrn,y_pred_trn_KNN_sklearn))])
        KNNReg_sklearn_cv_table.add_row([i,math.sqrt(mean_squared_error(ycv,y_pred_cv_KNN_sklearn))])
        if(math.sqrt(mean_squared_error(ytrn,y_pred_trn_KNN_sklearn))<best_rmse_train_KNN_sklearn):
            best_neighbors_train_KNN_sklearn=i
            best_rmse_train_KNN_sklearn=math.sqrt(mean_squared_error(ytrn,y_pred_trn_KNN_sklearn))
        if(math.sqrt(mean_squared_error(ycv,y_pred_cv_KNN_sklearn))<best_rmse_cv_KNN_sklearn):
            best_neighbors_cv_KNN_sklearn=i
            best_rmse_cv_KNN_sklearn=math.sqrt(mean_squared_error(ycv,y_pred_cv_KNN_sklearn))
    plt.plot(no_of_neighbors,rmse_train_KNN,label="Train RMSE")
    plt.plot(no_of_neighbors,rmse_cv_KNN,label="CV RMSE")
    plt.title("RMSE with Neighbors")
    plt.xlabel("Neighbors: Hyperparameter")
    plt.ylabel("RMSE")
    plt.legend()
    plt.show()
    print(KNNReg_sklearn_train_table)
    print(KNNReg_sklearn_cv_table)
    print("Best No.of Neighbors is:",best_neighbors_cv_KNN_sklearn)
    return best_neighbors_cv_KNN_sklearn


def euclidean_dist(x,xq):
    sum_dist=0
    dist=0
    for i in range(len(x)):
        sum_dist+=pow((x[i]-xq[i]),2)
        dist=math.sqrt(sum_dist)
    return dist


def KNNRegressionOwn(Xtrn,ytrn,n_neighbors,xq):
    nearest_points_indeces=[]
    distances={}
    sorted_distances={}
    Yhat=[]
    Ytrue=[]
    n=0
    for i in range(xq.shape[0]):
        for j in range(Xtrn.shape[0]):
            distances[j]=euclidean_dist(xq[i],Xtrn[j])
        sorted_distances=sorted(distances.items(), key=lambda x: x[1])
        near_points = dict(itertools.islice(dict(sorted_distances).items(), n_neighbors)) 
        for k in near_points:
            nearest_points_indeces.append(k)
        for p in range(len(nearest_points_indeces)):
            Ytrue.append(ytrn[nearest_points_indeces[p]])
        Yhat.append(sum(Ytrue)/len(Ytrue))
        nearest_points_indeces=[]
        distances={}
        Ytrue=[]
    return Yhat


def KNNRegressorOwnTraining(Xtrn,ytrn,Xcv,ycv,neighbors):
    no_of_neighbors=neighbors
    rmse_train_KNN_Own=[]
    rmse_cv_KNN_Own=[]

    KNNReg_own_train_table=PrettyTable()
    KNNReg_own_train_table.field_names = ["Neighbors","Train Error"]

    KNNReg_own_cv_table=PrettyTable()
    KNNReg_own_cv_table.field_names = ["Neighbors","CV Error"]

    best_neighbors_train_KNN_own=0
    best_rmse_train_KNN_own=float('inf')

    best_neighbors_cv_KNN_own=0
    best_rmse_cv_KNN_own=float('inf')

    for i in neighbors:
        y_pred_trn_knn_own = KNNRegressionOwn(Xtrn,ytrn,i,Xtrn)
        y_pred_cv_knn_own = KNNRegressionOwn(Xtrn,ytrn,i,Xcv)
 
        rmse_train_KNN_Own.append(math.sqrt(mean_squared_error(ytrn,y_pred_trn_knn_own)))
        rmse_cv_KNN_Own.append(math.sqrt(mean_squared_error(ycv,y_pred_cv_knn_own)))

        KNNReg_own_train_table.add_row([i,math.sqrt(mean_squared_error(ytrn,y_pred_trn_knn_own))])
        KNNReg_own_cv_table.add_row([i,math.sqrt(mean_squared_error(ycv,y_pred_cv_knn_own))])
    
        if(math.sqrt(mean_squared_error(ytrn,y_pred_trn_knn_own))<best_rmse_train_KNN_own):
            best_neighbors_train_KNN_own=i
            best_rmse_train_KNN_own=math.sqrt(mean_squared_error(ytrn,y_pred_trn_knn_own))
        if(math.sqrt(mean_squared_error(ycv,y_pred_cv_knn_own))<best_rmse_cv_KNN_own):
            best_neighbors_cv_KNN_own=i
            best_rmse_cv_KNN_own=math.sqrt(mean_squared_error(ycv,y_pred_cv_knn_own))
    plt.plot(neighbors,rmse_train_KNN_Own,label="Train RMSE")
    plt.plot(neighbors,rmse_cv_KNN_Own,label="CV RMSE")
    plt.title("RMSE with Neighbors")
    plt.xlabel("Neighbors: Hyperparameter")
    plt.ylabel("RMSE")
    plt.legend()
    plt.show()
    print(KNNReg_own_train_table)
    print(KNNReg_own_cv_table)
    print("Best No.of Neighbors is:",best_neighbors_cv_KNN_own)
    return best_neighbors_cv_KNN_own


def KNNRegressionOwnWeighted(Xtrn,ytrn,n_neighbors,xq):
    nearest_points_indeces=[]
    distances={}
    sorted_distances={}
    Yhat=[]
    Ytrue=[]
    weights=[]
    sum_weights=0
    pred=0
    n=0
    for i in range(xq.shape[0]):
        for j in range(Xtrn.shape[0]):
            distances[j]=euclidean_dist(xq[i],Xtrn[j])
        sorted_distances=sorted(distances.items(), key=lambda x: x[1])
        near_points = dict(itertools.islice(dict(sorted_distances).items(), n_neighbors)) 
        for k,v in near_points.items():
            nearest_points_indeces.append(k)
            weights.append(1/((v*v)+0.0001))
        for p in range(len(nearest_points_indeces)):
            Ytrue.append(ytrn[nearest_points_indeces[p]])
        for s in range(len(Ytrue)):
            pred+=Ytrue[s]*weights[s]
        sum_weights=sum(weights)    
        Yhat.append(pred/sum_weights)
        nearest_points_indeces=[]
        distances={}
        Ytrue=[]
        weights=[]
        sum_weights=0
        pred=0
    return Yhat


def KNNRegressionOwnWeightedTraining(Xtrn,ytrn,Xcv,ycv,neighbors):
    no_of_neighbors=neighbors
    rmse_train_KNN_Weighted_Own=[]
    rmse_cv_KNN_Weighted_Own=[]

    KNN_Weighted_own_train_table=PrettyTable()
    KNN_Weighted_own_train_table.field_names = ["Neighbors","Train Error"]

    KNN_Weighted_own_cv_table=PrettyTable()
    KNN_Weighted_own_cv_table.field_names = ["Neighbors","CV Error"]

    best_neighbors_train_KNN_Weighted_own=0
    best_neighbors_cv_KNN_Weighted_own=0

    best_rmse_train_KNN_Weighted_own=float('inf')
    best_rmse_cv_KNN_Weighted_own=float('inf')

    for i in no_of_neighbors:
        y_pred_trn_knn_weighted_own = KNNRegressionOwnWeighted(Xtrn,ytrn,i,Xtrn)
        y_pred_cv_knn_weighted_own = KNNRegressionOwnWeighted(Xtrn,ytrn,i,Xcv)
 
        rmse_train_KNN_Weighted_Own.append(math.sqrt(mean_squared_error(ytrn,y_pred_trn_knn_weighted_own)))
        rmse_cv_KNN_Weighted_Own.append(math.sqrt(mean_squared_error(ycv,y_pred_cv_knn_weighted_own)))
    
        KNN_Weighted_own_train_table.add_row([i,math.sqrt(mean_squared_error(ytrn,y_pred_trn_knn_weighted_own))])
        KNN_Weighted_own_cv_table.add_row([i,math.sqrt(mean_squared_error(ycv,y_pred_cv_knn_weighted_own))])
    
        if(math.sqrt(mean_squared_error(ytrn,y_pred_trn_knn_weighted_own))<best_rmse_train_KNN_Weighted_own):
            best_neighbors_train_KNN_Weighted_own=i
            best_rmse_train_KNN_Weighted_own=math.sqrt(mean_squared_error(ytrn,y_pred_trn_knn_weighted_own))
        if(math.sqrt(mean_squared_error(ycv,y_pred_cv_knn_weighted_own))<best_rmse_cv_KNN_Weighted_own):
            best_neighbors_cv_KNN_Weighted_own=i
            best_rmse_cv_KNN_Weighted_own=math.sqrt(mean_squared_error(ycv,y_pred_cv_knn_weighted_own))

    plt.plot(neighbors,rmse_train_KNN_Weighted_Own,label="Train RMSE")
    plt.plot(neighbors,rmse_cv_KNN_Weighted_Own,label="CV RMSE")
    plt.title("RMSE with Neighbors")
    plt.xlabel("Neighbors: Hyperparameter")
    plt.ylabel("RMSE")
    plt.legend()
    plt.show()
    print(KNN_Weighted_own_train_table)
    print(KNN_Weighted_own_cv_table)
    print("Best No.of Neighbors is:",best_neighbors_cv_KNN_Weighted_own)
    return best_neighbors_cv_KNN_Weighted_own


#Executing the above defined models by passing data to them

#Batsmen Data

M_trn = np.genfromtxt('./Batsmen_Data_After_Processing.csv', missing_values=0, skip_header=1, delimiter=',', dtype=float)

ytrn_Bat = M_trn[:, 0]
Xtrn_Bat = M_trn[:, 1:8]

Xtrn_Bat, Xtst_Bat, ytrn_Bat, ytst_Bat = train_test_split(Xtrn_Bat, ytrn_Bat, test_size=0.1)
Xtrn_Bat, Xcv_Bat, ytrn_Bat, ycv_Bat = train_test_split(Xtrn_Bat, ytrn_Bat, test_size=0.1) 
 

print("Shape of Xtrn_Bat is",Xtrn_Bat.shape)
print("Shape of ytrn_Bat is",ytrn_Bat.shape)
print("Shape of Xcv_Bat is",Xcv_Bat.shape)
print("Shape of ycv_Bat is",ycv_Bat.shape)
print("Shape of Xtst_Bat is",Xtst_Bat.shape)
print("Shape of ytst_Bat is",ytst_Bat.shape)

#Using the Data without sampling for KNN as KNN is sensitive to duplicates

Xtrn_Bat_KNN=Xtrn_Bat
Xcv_Bat_KNN=Xcv_Bat
Xtst_Bat_KNN=Xtst_Bat
ytrn_Bat_KNN=ytrn_Bat
ycv_Bat_KNN=ycv_Bat
ytst_Bat_KNN=ytst_Bat


#Sampling the Train Data separately to make sure that there is no data leake to the Test set with Replacement to generate samples as the datasize is small.

Xtrndf=pd.DataFrame(Xtrn_Bat)
ytrndf=pd.DataFrame(ytrn_Bat)
Train_Data = pd.concat([ytrndf,Xtrndf], axis=1)
Train_Data_upsampled = resample(Train_Data,replace=True,n_samples=50)
Xtrn_Bat_upsampled=Train_Data_upsampled.iloc[:,1:8].values
Ytrn_Bat_upsampled=Train_Data_upsampled.iloc[:,0].values
Xtrnfinal=np.concatenate((Xtrn_Bat, Xtrn_Bat_upsampled), axis=0)
ytrnfinal=np.concatenate((ytrn_Bat, Ytrn_Bat_upsampled), axis=0)


#Sampling the CV Data

Xcvdf=pd.DataFrame(Xcv_Bat)
ycvdf=pd.DataFrame(ycv_Bat)
CV_Data = pd.concat([ycvdf,Xcvdf], axis=1)
CV_Data_upsampled = resample(CV_Data,replace=True,n_samples=30)
Xcv_Bat_upsampled=CV_Data_upsampled.iloc[:,1:8].values
Ycv_Bat_upsampled=CV_Data_upsampled.iloc[:,0].values
Xcvfinal=np.concatenate((Xcv_Bat, Xcv_Bat_upsampled), axis=0)
ycvfinal=np.concatenate((ycv_Bat, Ycv_Bat_upsampled), axis=0)


#Sampling the Test Data


Xtestdf=pd.DataFrame(Xtst_Bat)
ytestdf=pd.DataFrame(ytst_Bat)
Test_Data = pd.concat([ytestdf,Xtestdf], axis=1)
Test_Data_upsampled = resample(Test_Data,replace=True,n_samples=15)
Xtest_Bat_upsampled=Test_Data_upsampled.iloc[:,1:8].values
Ytest_Bat_upsampled=Test_Data_upsampled.iloc[:,0].values
Xtestfinal=np.concatenate((Xtst_Bat, Xtest_Bat_upsampled), axis=0)
ytestfinal=np.concatenate((ytst_Bat, Ytest_Bat_upsampled), axis=0)


#Applying the Log to the Data to make it as normal distribution and then standardizing it

Xtrn_Bat=Xtrnfinal
Xcv_Bat=Xcvfinal
Xtst_Bat=Xtestfinal
ytrn_Bat=ytrnfinal
ycv_Bat=ycvfinal
ytst_Bat=ytestfinal

print("Shape of Xtrn_Bat after upsampling is",Xtrn_Bat.shape)
print("Shape of ytrn_Bat after upsampling is",ytrn_Bat.shape)
print("Shape of Xcv_Bat after upsampling is",Xcv_Bat.shape)
print("Shape of ycv_Bat after upsampling is",ycv_Bat.shape)
print("Shape of Xtst_Bat after upsampling is",Xtst_Bat.shape)
print("Shape of ytst_Bat after upsampling is",ytst_Bat.shape)


Xtrn_Bat = np.log(Xtrn_Bat)
Xcv_Bat = np.log(Xcv_Bat)
Xtst_Bat = np.log(Xtst_Bat)

Stdscaler_Bat = preprocessing.StandardScaler().fit(Xtrn_Bat)
Xtrn_Bat = Stdscaler_Bat.transform(Xtrn_Bat)
Xcv_Bat = Stdscaler_Bat.transform(Xcv_Bat)
Xtst_Bat = Stdscaler_Bat.transform(Xtst_Bat)


#SGD SKlearn

epochs=[10,100,200,400,800,1600,2000]
best_epoch_cv_SGD_sklearn_Bat=sklearnSGDRegressor(Xtrn_Bat,ytrn_Bat,Xcv_Bat,ycv_Bat,epochs)

rmse_test_SGD_Bat=[]
SGDReg_sklearn_test_table_Bat=PrettyTable()
SGDReg_sklearn_test_table_Bat.field_names = ["Epochs","Test Error"]

sgd_reg_test_Bat = SGDRegressor(shuffle = False,max_iter = best_epoch_cv_SGD_sklearn_Bat)
sgd_reg_test_Bat.fit(Xtrn_Bat, ytrn_Bat)
y_pred_tst_sgd_sklearn_Bat = sgd_reg_test_Bat.predict(Xtst_Bat)
rmse_test_SGD_Bat.append(math.sqrt(mean_squared_error(ytst_Bat,y_pred_tst_sgd_sklearn_Bat)))
SGDReg_sklearn_test_table_Bat.add_row([best_epoch_cv_SGD_sklearn_Bat,math.sqrt(mean_squared_error(ytst_Bat,y_pred_tst_sgd_sklearn_Bat))])
print(SGDReg_sklearn_test_table_Bat)

plt.scatter(ytst_Bat,y_pred_tst_sgd_sklearn_Bat)
plt.grid()
plt.xlabel('Actual y')
plt.ylabel('Predicted y')
plt.title('Actual Value and Predicted Value using Sklearn SGD on Batsmen Data')
plt.show()


#SGD Own

train_data_Bat=pd.DataFrame(Xtrn_Bat)
train_data_Bat['regresult']=ytrn_Bat
epochs=[10,100,200,400,800,1600,2000]

rmse_test_SGD_Own_Bat=[]
SGDReg_own_test_table_Bat=PrettyTable()
SGDReg_own_test_table_Bat.field_names = ["Epochs","Test Error"]

best_epoch_cv_SGD_Own_Bat=SGDRegressionOwnTraining(Xtrn_Bat,ytrn_Bat,Xcv_Bat,ycv_Bat,epochs)

w_Bat,b_Bat = SGDRegressionOwn(train_data_Bat,learning_rate=0.01,total_iter=best_epoch_cv_SGD_Own_Bat,k=10)
y_pred_tst_sgd_own_Bat = predictSGDOwn(Xtst_Bat,w_Bat,b_Bat)
rmse_test_SGD_Own_Bat.append(math.sqrt(mean_squared_error(ytst_Bat,y_pred_tst_sgd_own_Bat)))
SGDReg_own_test_table_Bat.add_row([best_epoch_cv_SGD_Own_Bat,math.sqrt(mean_squared_error(ytst_Bat,y_pred_tst_sgd_own_Bat))])
print(SGDReg_own_test_table_Bat)

plt.scatter(ytst_Bat,y_pred_tst_sgd_own_Bat)
plt.grid()
plt.xlabel('Actual y')
plt.ylabel('Predicted y')
plt.title('Actual Value and Predicted Value using Own SGD on Batsmen Data')
plt.show()


#LSE Own

shape=Xtrn_Bat.shape[1]+1
we_Bat=LinearRegressionLSM(Xtrn_Bat,ytrn_Bat,shape)
y_pred_lse_own_Bat=predict_LSM(Xtst_Bat,we_Bat)
rmse_train_LSE_Own_Bat=math.sqrt(mean_squared_error(ytst_Bat,y_pred_lse_own_Bat))
print("RMSE using Least Squares Estimates is",rmse_train_LSE_Own_Bat)


plt.scatter(ytst_Bat,y_pred_lse_own_Bat)
plt.grid()
plt.xlabel('Actual y')
plt.ylabel('Predicted y')
plt.title('Actual Value and Predicted Value using Own LSE on Batsmen Data')
plt.show()


#KNN Sklearn


rmse_test_KNN_Bat=[]
KNNReg_sklearn_test_table_Bat=PrettyTable()
KNNReg_sklearn_test_table_Bat.field_names = ["Neighbors","Test Error"]
neighbors=[1,2,3,4,5,6,7,8,9]
best_neighbors_cv_KNN_sklearn_Bat=sklearnKNNRegressor(Xtrn_Bat_KNN,ytrn_Bat_KNN,Xcv_Bat_KNN,ycv_Bat_KNN,neighbors)

knn_reg_test_Bat = KNeighborsRegressor(n_neighbors=best_neighbors_cv_KNN_sklearn_Bat)
knn_reg_test_Bat.fit(Xtrn_Bat_KNN, ytrn_Bat_KNN)
y_pred_tst_knn_sklearn_Bat = knn_reg_test_Bat.predict(Xtst_Bat_KNN)
rmse_test_KNN_Bat.append(math.sqrt(mean_squared_error(ytst_Bat_KNN,y_pred_tst_knn_sklearn_Bat)))
KNNReg_sklearn_test_table_Bat.add_row([best_neighbors_cv_KNN_sklearn_Bat,math.sqrt(mean_squared_error(ytst_Bat_KNN,y_pred_tst_knn_sklearn_Bat))])
print(KNNReg_sklearn_test_table_Bat)
plt.scatter(ytst_Bat_KNN,y_pred_tst_knn_sklearn_Bat)
plt.grid()
plt.xlabel('Actual y')
plt.ylabel('Predicted y')
plt.title('Actual Value and Predicted Value using Sklearn KNN on Batsmen Data')
plt.show()


#KNN Own

neighbors=[1,2,3,4,5,6,7,8,9]
KNNReg_own_test_table_Bat=PrettyTable()
KNNReg_own_test_table_Bat.field_names = ["Neighbors","Test Error"]

best_neighbors_cv_KNN_own_Bat=KNNRegressorOwnTraining(Xtrn_Bat_KNN,ytrn_Bat_KNN,Xcv_Bat_KNN,ycv_Bat_KNN,neighbors)

y_pred_knn_own_Bat=KNNRegressionOwn(Xtrn_Bat_KNN,ytrn_Bat_KNN,best_neighbors_cv_KNN_own_Bat,Xtst_Bat_KNN)
KNNReg_own_test_table_Bat.add_row([best_neighbors_cv_KNN_own_Bat,math.sqrt(mean_squared_error(ytst_Bat_KNN,y_pred_knn_own_Bat))])
print(KNNReg_own_test_table_Bat)

plt.scatter(ytst_Bat_KNN,y_pred_knn_own_Bat)
plt.grid()
plt.xlabel('Actual y')
plt.ylabel('Predicted y')
plt.title('Actual Value and Predicted Value using Own KNN on Batsmen Data')
plt.show()


#Weighted KNN Own

neighbors=[1,2,3,4,5,6,7,8,9]
KNNReg_own_weighted_test_table_Bat=PrettyTable()
KNNReg_own_weighted_test_table_Bat.field_names = ["Neighbors","Test Error"]

best_neighbors_cv_KNN_Weighted_own_Bat=KNNRegressionOwnWeightedTraining(Xtrn_Bat_KNN,ytrn_Bat_KNN,Xcv_Bat_KNN,ycv_Bat_KNN,neighbors)

y_pred_knn_own_weighted_Bat=KNNRegressionOwnWeighted(Xtrn_Bat_KNN,ytrn_Bat_KNN,best_neighbors_cv_KNN_Weighted_own_Bat,Xtst_Bat_KNN)
KNNReg_own_weighted_test_table_Bat.add_row([best_neighbors_cv_KNN_Weighted_own_Bat,math.sqrt(mean_squared_error(ytst_Bat_KNN,y_pred_knn_own_weighted_Bat))])
print(KNNReg_own_test_table_Bat)

plt.scatter(ytst_Bat_KNN,y_pred_knn_own_weighted_Bat)
plt.grid()
plt.xlabel('Actual y')
plt.ylabel('Predicted y')
plt.title('Actual Value and Predicted Value using Own Weighted KNN on Batsmen Data')
plt.show()


#Bowler Data

M_trn = np.genfromtxt('./Bowler_Data_After_Processing.csv', missing_values=0, skip_header=1, delimiter=',', dtype=float)
ytrn_Bowl = M_trn[:, 0]
Xtrn_Bowl = M_trn[:, 1:6]

Xtrn_Bowl, Xtst_Bowl, ytrn_Bowl, ytst_Bowl = train_test_split(Xtrn_Bowl, ytrn_Bowl, test_size=0.2)
Xtrn_Bowl, Xcv_Bowl, ytrn_Bowl, ycv_Bowl = train_test_split(Xtrn_Bowl, ytrn_Bowl, test_size=0.1) 

print("Shape of Xtrn_Bowl is",Xtrn_Bowl.shape)
print("Shape of ytrn_Bowl is",ytrn_Bowl.shape)
print("Shape of Xcv_Bowl is",Xcv_Bowl.shape)
print("Shape of ycv_Bowl is",ycv_Bowl.shape)
print("Shape of Xtst_Bowl is",Xtst_Bowl.shape)
print("Shape of ytst_Bowl is",ytst_Bowl.shape)

#Using the Data without sampling for KNN as KNN is sensitive to duplicates

Xtrn_Bowl_KNN=Xtrn_Bowl
Xcv_Bowl_KNN=Xcv_Bowl
Xtst_Bowl_KNN=Xtst_Bowl
ytrn_Bowl_KNN=ytrn_Bowl
ycv_Bowl_KNN=ycv_Bowl
ytst_Bowl_KNN=ytst_Bowl


#Sampling the Train Data separately to make sure that there is no data leake to the Test set with Replacement to generate samples as the datasize is small.

Xtrndf=pd.DataFrame(Xtrn_Bowl)
ytrndf=pd.DataFrame(ytrn_Bowl)
Train_Data = pd.concat([ytrndf,Xtrndf], axis=1)
Train_Data_upsampled = resample(Train_Data,replace=True,n_samples=70)
Xtrn_Bowl_upsampled=Train_Data_upsampled.iloc[:,1:6].values
Ytrn_Bowl_upsampled=Train_Data_upsampled.iloc[:,0].values
Xtrnfinal=np.concatenate((Xtrn_Bowl, Xtrn_Bowl_upsampled), axis=0)
ytrnfinal=np.concatenate((ytrn_Bowl, Ytrn_Bowl_upsampled), axis=0)


#Sampling the CV Data


Xcvdf=pd.DataFrame(Xcv_Bowl)
ycvdf=pd.DataFrame(ycv_Bowl)
CV_Data = pd.concat([ycvdf,Xcvdf], axis=1)
CV_Data_upsampled = resample(CV_Data,replace=True,n_samples=50)
Xcv_Bowl_upsampled=CV_Data_upsampled.iloc[:,1:6].values
Ycv_Bowl_upsampled=CV_Data_upsampled.iloc[:,0].values
Xcvfinal=np.concatenate((Xcv_Bowl, Xcv_Bowl_upsampled), axis=0)
ycvfinal=np.concatenate((ycv_Bowl, Ycv_Bowl_upsampled), axis=0)


#Sampling the Test Data

Xtestdf=pd.DataFrame(Xtst_Bowl)
ytestdf=pd.DataFrame(ytst_Bowl)
Test_Data = pd.concat([ytestdf,Xtestdf], axis=1)
Test_Data_upsampled = resample(Test_Data,replace=True,n_samples=35)
Xtest_Bowl_upsampled=Test_Data_upsampled.iloc[:,1:6].values
Ytest_Bowl_upsampled=Test_Data_upsampled.iloc[:,0].values
Xtestfinal=np.concatenate((Xtst_Bowl, Xtest_Bowl_upsampled), axis=0)
ytestfinal=np.concatenate((ytst_Bowl, Ytest_Bowl_upsampled), axis=0)


#Applying the Log to the Data to make it as normal distribution and then standardizing it

Xtrn_Bowl=Xtrnfinal
Xcv_Bowl=Xcvfinal
Xtst_Bowl=Xtestfinal
ytrn_Bowl=ytrnfinal
ycv_Bowl=ycvfinal
ytst_Bowl=ytestfinal

print("Shape of Xtrn_Bowl after upsampling is",Xtrn_Bowl.shape)
print("Shape of ytrn_Bowl after upsampling is",ytrn_Bowl.shape)
print("Shape of Xcv_Bowl after upsampling is",Xcv_Bowl.shape)
print("Shape of ycv_Bowl after upsampling is",ycv_Bowl.shape)
print("Shape of Xtst_Bowl after upsampling is",Xtst_Bowl.shape)
print("Shape of ytst_Bowl after upsampling is",ytst_Bowl.shape)

Xtrn_Bowl = np.log(Xtrn_Bowl)
Xcv_Bowl = np.log(Xcv_Bowl)
Xtst_Bowl = np.log(Xtst_Bowl)

Stdscaler_Bowl = preprocessing.StandardScaler().fit(Xtrn_Bowl)
Xtrn_Bowl = Stdscaler_Bowl.transform(Xtrn_Bowl)
Xcv_Bowl = Stdscaler_Bowl.transform(Xcv_Bowl)
Xtst_Bowl = Stdscaler_Bowl.transform(Xtst_Bowl)


#SGD SKlearn

epochs=[10,100,200,400,800,1600,2000]
best_epoch_cv_SGD_sklearn_Bowl=sklearnSGDRegressor(Xtrn_Bowl,ytrn_Bowl,Xcv_Bowl,ycv_Bowl,epochs)

rmse_test_SGD_Bowl=[]
SGDReg_sklearn_test_table_Bowl=PrettyTable()
SGDReg_sklearn_test_table_Bowl.field_names = ["Epochs","Test Error"]

sgd_reg_test_Bowl = SGDRegressor(shuffle = False,max_iter = best_epoch_cv_SGD_sklearn_Bowl)
sgd_reg_test_Bowl.fit(Xtrn_Bowl, ytrn_Bowl)
y_pred_tst_sgd_sklearn_Bowl = sgd_reg_test_Bowl.predict(Xtst_Bowl)
rmse_test_SGD_Bowl.append(math.sqrt(mean_squared_error(ytst_Bowl,y_pred_tst_sgd_sklearn_Bowl)))
SGDReg_sklearn_test_table_Bowl.add_row([best_epoch_cv_SGD_sklearn_Bowl,math.sqrt(mean_squared_error(ytst_Bowl,y_pred_tst_sgd_sklearn_Bowl))])
print(SGDReg_sklearn_test_table_Bowl)

plt.scatter(ytst_Bowl,y_pred_tst_sgd_sklearn_Bowl)
plt.grid()
plt.xlabel('Actual y')
plt.ylabel('Predicted y')
plt.title('Actual Value and Predicted Value using Sklearn SGD on Bowlers Data')
plt.show()

#SGD Own

train_data_Bowl=pd.DataFrame(Xtrn_Bowl)
train_data_Bowl['regresult']=ytrn_Bowl
epochs=[10,100,200,400,800,1600,2000]

rmse_test_SGD_Own_Bowl=[]
SGDReg_own_test_table_Bowl=PrettyTable()
SGDReg_own_test_table_Bowl.field_names = ["Epochs","Test Error"]

best_epoch_cv_SGD_Own_Bowl=SGDRegressionOwnTraining(Xtrn_Bowl,ytrn_Bowl,Xcv_Bowl,ycv_Bowl,epochs)

w_Bowl,b_Bowl = SGDRegressionOwn(train_data_Bowl,learning_rate=0.01,total_iter=best_epoch_cv_SGD_Own_Bowl,k=10)
y_pred_tst_sgd_own_Bowl = predictSGDOwn(Xtst_Bowl,w_Bowl,b_Bowl)
rmse_test_SGD_Own_Bowl.append(math.sqrt(mean_squared_error(ytst_Bowl,y_pred_tst_sgd_own_Bowl)))
SGDReg_own_test_table_Bowl.add_row([best_epoch_cv_SGD_Own_Bowl,math.sqrt(mean_squared_error(ytst_Bowl,y_pred_tst_sgd_own_Bowl))])
print(SGDReg_own_test_table_Bowl)

plt.scatter(ytst_Bowl,y_pred_tst_sgd_own_Bowl)
plt.grid()
plt.xlabel('Actual y')
plt.ylabel('Predicted y')
plt.title('Actual Value and Predicted Value using Own SGD on Bowlers Data')
plt.show()

#LSE Own

shape=Xtrn_Bowl.shape[1]+1
we_Bowl=LinearRegressionLSM(Xtrn_Bowl,ytrn_Bowl,shape)
y_pred_lse_own_Bowl=predict_LSM(Xtst_Bowl,we_Bowl)
rmse_train_LSE_Own_Bowl=math.sqrt(mean_squared_error(ytst_Bowl,y_pred_lse_own_Bowl))
print("RMSE using Least Squares Estimates is",rmse_train_LSE_Own_Bowl)

plt.scatter(ytst_Bowl,y_pred_lse_own_Bowl)
plt.grid()
plt.xlabel('Actual y')
plt.ylabel('Predicted y')
plt.title('Actual Value and Predicted Value using Own LSE on Bowlers Data')
plt.show()


#KNN Sklearn

rmse_test_KNN_Bowl=[]
KNNReg_sklearn_test_table_Bowl=PrettyTable()
KNNReg_sklearn_test_table_Bowl.field_names = ["Neighbors","Test Error"]
neighbors=[1,2,3,4,5,6,7,8,9]
best_neighbors_cv_KNN_sklearn_Bowl=sklearnKNNRegressor(Xtrn_Bowl_KNN,ytrn_Bowl_KNN,Xcv_Bowl_KNN,ycv_Bowl_KNN,neighbors)

knn_reg_test_Bowl = KNeighborsRegressor(n_neighbors=best_neighbors_cv_KNN_sklearn_Bowl)
knn_reg_test_Bowl.fit(Xtrn_Bowl_KNN, ytrn_Bowl_KNN)
y_pred_tst_knn_sklearn_Bowl = knn_reg_test_Bowl.predict(Xtst_Bowl_KNN)
rmse_test_KNN_Bowl.append(math.sqrt(mean_squared_error(ytst_Bowl_KNN,y_pred_tst_knn_sklearn_Bowl)))
KNNReg_sklearn_test_table_Bowl.add_row([best_neighbors_cv_KNN_sklearn_Bowl,math.sqrt(mean_squared_error(ytst_Bowl_KNN,y_pred_tst_knn_sklearn_Bowl))])
print(KNNReg_sklearn_test_table_Bowl)

plt.scatter(ytst_Bowl_KNN,y_pred_tst_knn_sklearn_Bowl)
plt.grid()
plt.xlabel('Actual y')
plt.ylabel('Predicted y')
plt.title('Actual Value and Predicted Value using Sklearn KNN on Bowlers Data')
plt.show()

#KNN Own

neighbors=[1,2,3,4,5,6,7,8,9]
best_neighbors_cv_KNN_own_Bowl=KNNRegressorOwnTraining(Xtrn_Bowl_KNN,ytrn_Bowl_KNN,Xcv_Bowl_KNN,ycv_Bowl_KNN,neighbors)

y_pred_knn_own_Bowl=KNNRegressionOwn(Xtrn_Bowl_KNN,ytrn_Bowl_KNN,best_neighbors_cv_KNN_own_Bowl,Xtst_Bowl_KNN)
KNNReg_own_test_table_Bowl=PrettyTable()
KNNReg_own_test_table_Bowl.field_names = ["Neighbors","Test Error"]
KNNReg_own_test_table_Bowl.add_row([best_neighbors_cv_KNN_own_Bowl,math.sqrt(mean_squared_error(ytst_Bowl_KNN,y_pred_knn_own_Bowl))])
print(KNNReg_own_test_table_Bowl)
plt.scatter(ytst_Bowl_KNN,y_pred_knn_own_Bowl)
plt.grid()
plt.xlabel('Actual y')
plt.ylabel('Predicted y')
plt.title('Actual Value and Predicted Value using Own KNN on Bowlers Data')
plt.show()


#Weighted KNN Own

neighbors=[1,2,3,4,5,6,7,8,9]
KNNReg_own_weighted_test_table_Bowl=PrettyTable()
KNNReg_own_weighted_test_table_Bowl.field_names = ["Neighbors","Test Error"]

best_neighbors_cv_KNN_Weighted_own_Bowl=KNNRegressionOwnWeightedTraining(Xtrn_Bowl_KNN,ytrn_Bowl_KNN,Xcv_Bowl_KNN,ycv_Bowl_KNN,neighbors)

y_pred_knn_own_weighted_Bowl=KNNRegressionOwnWeighted(Xtrn_Bowl_KNN,ytrn_Bowl_KNN,best_neighbors_cv_KNN_Weighted_own_Bowl,Xtst_Bowl_KNN)
KNNReg_own_weighted_test_table_Bowl.add_row([best_neighbors_cv_KNN_Weighted_own_Bowl,math.sqrt(mean_squared_error(ytst_Bowl_KNN,y_pred_knn_own_weighted_Bowl))])
print(KNNReg_own_weighted_test_table_Bowl)

plt.scatter(ytst_Bowl_KNN,y_pred_knn_own_weighted_Bowl)
plt.grid()
plt.xlabel('Actual y')
plt.ylabel('Predicted y')
plt.title('Actual Value and Predicted Value using Own Weighted KNN on Bowlers Data')
plt.show()


#AllRounder Data

M_trn = np.genfromtxt('./AllRounder_Data_After_Processing.csv', missing_values=0, skip_header=1, delimiter=',', dtype=float)
ytrn_All = M_trn[:, 0]
Xtrn_All = M_trn[:, 1:13]

Xtrn_All, Xtst_All, ytrn_All, ytst_All = train_test_split(Xtrn_All, ytrn_All, test_size=0.2)
Xtrn_All, Xcv_All, ytrn_All, ycv_All = train_test_split(Xtrn_All, ytrn_All, test_size=0.1) 

print("Shape of Xtrn_All is",Xtrn_All.shape)
print("Shape of ytrn_All is",ytrn_All.shape)
print("Shape of Xcv_All is",Xcv_All.shape)
print("Shape of ycv_All is",ycv_All.shape)
print("Shape of Xtst_All is",Xtst_All.shape)
print("Shape of ytst_All is",ytst_All.shape)

#Using the Data without sampling for KNN as KNN is sensitive to duplicates

Xtrn_All_KNN=Xtrn_All
Xcv_All_KNN=Xcv_All
Xtst_All_KNN=Xtst_All
ytrn_All_KNN=ytrn_All
ycv_All_KNN=ycv_All
ytst_All_KNN=ytst_All


#Sampling the Train Data separately to make sure that there is no data leake to the Test set with Replacement to generate samples as the datasize is small.

Xtrndf=pd.DataFrame(Xtrn_All)
ytrndf=pd.DataFrame(ytrn_All)
Train_Data = pd.concat([ytrndf,Xtrndf], axis=1)
Train_Data_upsampled = resample(Train_Data,replace=True,n_samples=50)
Xtrn_All_upsampled=Train_Data_upsampled.iloc[:,1:13].values
Ytrn_All_upsampled=Train_Data_upsampled.iloc[:,0].values
Xtrnfinal=np.concatenate((Xtrn_All, Xtrn_All_upsampled), axis=0)
ytrnfinal=np.concatenate((ytrn_All, Ytrn_All_upsampled), axis=0)


#Sampling the CV Data

Xcvdf=pd.DataFrame(Xcv_All)
ycvdf=pd.DataFrame(ycv_All)
CV_Data = pd.concat([ycvdf,Xcvdf], axis=1)
CV_Data_upsampled = resample(CV_Data,replace=True,n_samples=30)
Xcv_All_upsampled=CV_Data_upsampled.iloc[:,1:13].values
Ycv_All_upsampled=CV_Data_upsampled.iloc[:,0].values
Xcvfinal=np.concatenate((Xcv_All, Xcv_All_upsampled), axis=0)
ycvfinal=np.concatenate((ycv_All, Ycv_All_upsampled), axis=0)


#Sampling the Test Data

Xtestdf=pd.DataFrame(Xtst_All)
ytestdf=pd.DataFrame(ytst_All)
Test_Data = pd.concat([ytestdf,Xtestdf], axis=1)
Test_Data_upsampled = resample(Test_Data,replace=True,n_samples=15)
Xtest_All_upsampled=Test_Data_upsampled.iloc[:,1:13].values
Ytest_All_upsampled=Test_Data_upsampled.iloc[:,0].values
Xtestfinal=np.concatenate((Xtst_All, Xtest_All_upsampled), axis=0)
ytestfinal=np.concatenate((ytst_All, Ytest_All_upsampled), axis=0)


#Applying the Log to the Data to make it as normal distribution and then standardizing it

Xtrn_All=Xtrnfinal
Xcv_All=Xcvfinal
Xtst_All=Xtestfinal
ytrn_All=ytrnfinal
ycv_All=ycvfinal
ytst_All=ytestfinal

print("Shape of Xtrn_All after upsampling is",Xtrn_All.shape)
print("Shape of ytrn_All after upsampling is",ytrn_All.shape)
print("Shape of Xcv_All after upsampling is",Xcv_All.shape)
print("Shape of ycv_All after upsampling is",ycv_All.shape)
print("Shape of Xtst_All after upsampling is",Xtst_All.shape)
print("Shape of ytst_All after upsampling is",ytst_All.shape)


Xtrn_All = np.log(Xtrn_All)
Xcv_All = np.log(Xcv_All)
Xtst_All = np.log(Xtst_All)

Stdscaler_All = preprocessing.StandardScaler().fit(Xtrn_All)
Xtrn_All = Stdscaler_All.transform(Xtrn_All)
Xcv_All = Stdscaler_All.transform(Xcv_All)
Xtst_All = Stdscaler_All.transform(Xtst_All)


#SGD SKlearn

epochs=[10,100,200,400,800,1600,2000]
best_epoch_cv_SGD_sklearn_All=sklearnSGDRegressor(Xtrn_All,ytrn_All,Xcv_All,ycv_All,epochs)

rmse_test_SGD_All=[]
SGDReg_sklearn_test_table_All=PrettyTable()
SGDReg_sklearn_test_table_All.field_names = ["Epochs","Test Error"]

sgd_reg_test_All = SGDRegressor(shuffle = False,max_iter = best_epoch_cv_SGD_sklearn_Bowl)
sgd_reg_test_All.fit(Xtrn_All, ytrn_All)
y_pred_tst_sgd_sklearn_All = sgd_reg_test_All.predict(Xtst_All)
rmse_test_SGD_All.append(math.sqrt(mean_squared_error(ytst_All,y_pred_tst_sgd_sklearn_All)))
SGDReg_sklearn_test_table_All.add_row([best_epoch_cv_SGD_sklearn_All,math.sqrt(mean_squared_error(ytst_All,y_pred_tst_sgd_sklearn_All))])
print(SGDReg_sklearn_test_table_All)

plt.scatter(ytst_All,y_pred_tst_sgd_sklearn_All)
plt.grid()
plt.xlabel('Actual y')
plt.ylabel('Predicted y')
plt.title('Actual Value and Predicted Value using Sklearn SGD on AllRounders Data')
plt.show()


#SGD Own

train_data_All=pd.DataFrame(Xtrn_All)
train_data_All['regresult']=ytrn_All
epochs=[10,100,200,400,800,1600,2000]

rmse_test_SGD_Own_All=[]
SGDReg_own_test_table_All=PrettyTable()
SGDReg_own_test_table_All.field_names = ["Epochs","Test Error"]

best_epoch_cv_SGD_Own_All=SGDRegressionOwnTraining(Xtrn_All,ytrn_All,Xcv_All,ycv_All,epochs)

w_All,b_All = SGDRegressionOwn(train_data_All,learning_rate=0.01,total_iter=best_epoch_cv_SGD_Own_All,k=10)
y_pred_tst_sgd_own_All = predictSGDOwn(Xtst_All,w_All,b_All)
rmse_test_SGD_Own_All.append(math.sqrt(mean_squared_error(ytst_All,y_pred_tst_sgd_own_All)))
SGDReg_own_test_table_All.add_row([best_epoch_cv_SGD_Own_All,math.sqrt(mean_squared_error(ytst_All,y_pred_tst_sgd_own_All))])
print(SGDReg_own_test_table_All)

plt.scatter(ytst_All,y_pred_tst_sgd_own_All)
plt.grid()
plt.xlabel('Actual y')
plt.ylabel('Predicted y')
plt.title('Actual Value and Predicted Value using Own SGD on AllRounders Data')
plt.show()


#LSE Own

shape=Xtrn_All.shape[1]+1
we_All=LinearRegressionLSM(Xtrn_All,ytrn_All,shape)
y_pred_lse_own_All=predict_LSM(Xtst_All,we_All)
rmse_train_LSE_Own_All=math.sqrt(mean_squared_error(ytst_All,y_pred_lse_own_All))
print("RMSE using Least Squares Estimates is",rmse_train_LSE_Own_All)

plt.scatter(ytst_All,y_pred_lse_own_All)
plt.grid()
plt.xlabel('Actual y')
plt.ylabel('Predicted y')
plt.title('Actual Value and Predicted Value using Own LSE on AllRounders Data')
plt.show()


#KNN Sklearn

rmse_test_KNN_All=[]
KNNReg_sklearn_test_table_All=PrettyTable()
KNNReg_sklearn_test_table_All.field_names = ["Neighbors","Test Error"]
neighbors=[1,2,3,4,5,6,7,8,9]
best_neighbors_cv_KNN_sklearn_All=sklearnKNNRegressor(Xtrn_All_KNN,ytrn_All_KNN,Xcv_All_KNN,ycv_All_KNN,neighbors)

knn_reg_test_All = KNeighborsRegressor(n_neighbors=best_neighbors_cv_KNN_sklearn_All)
knn_reg_test_All.fit(Xtrn_All_KNN, ytrn_All_KNN)
y_pred_tst_knn_sklearn_All = knn_reg_test_All.predict(Xtst_All_KNN)
rmse_test_KNN_All.append(math.sqrt(mean_squared_error(ytst_All_KNN,y_pred_tst_knn_sklearn_All)))
KNNReg_sklearn_test_table_All.add_row([best_neighbors_cv_KNN_sklearn_All,math.sqrt(mean_squared_error(ytst_All_KNN,y_pred_tst_knn_sklearn_All))])
print(KNNReg_sklearn_test_table_All)

plt.scatter(ytst_All_KNN,y_pred_tst_knn_sklearn_All)
plt.grid()
plt.xlabel('Actual y')
plt.ylabel('Predicted y')
plt.title('Actual Value and Predicted Value using sklearn KNN on AllRounders Data')
plt.show()


#KNN Own

neighbors=[1,2,3,4,5,6,7,8,9]
best_neighbors_cv_KNN_own_All=KNNRegressorOwnTraining(Xtrn_All_KNN,ytrn_All_KNN,Xcv_All_KNN,ycv_All_KNN,neighbors)

y_pred_knn_own_All=KNNRegressionOwn(Xtrn_All_KNN,ytrn_All_KNN,best_neighbors_cv_KNN_own_All,Xtst_All_KNN)
KNNReg_own_test_table_All=PrettyTable()
KNNReg_own_test_table_All.field_names = ["Neighbors","Test Error"]
KNNReg_own_test_table_All.add_row([best_neighbors_cv_KNN_own_All,math.sqrt(mean_squared_error(ytst_All_KNN,y_pred_knn_own_All))])

print(KNNReg_own_test_table_All)

plt.scatter(ytst_All_KNN,y_pred_knn_own_All)
plt.grid()
plt.xlabel('Actual y')
plt.ylabel('Predicted y')
plt.title('Actual Value and Predicted Value using Own KNN on AllRounders Data')
plt.show()


#Weighted KNN Own

neighbors=[1,2,3,4,5,6,7,8,9]
KNNReg_own_weighted_test_table_All=PrettyTable()
best_neighbors_cv_KNN_Weighted_own_All=KNNRegressionOwnWeightedTraining(Xtrn_All_KNN,ytrn_All_KNN,Xcv_All_KNN,ycv_All_KNN,neighbors)

y_pred_knn_own_weighted_All=KNNRegressionOwnWeighted(Xtrn_All_KNN,ytrn_All_KNN,best_neighbors_cv_KNN_Weighted_own_All,Xtst_All_KNN)

KNNReg_own_weighted_test_table_All.field_names = ["Neighbors","Test Error"]
KNNReg_own_weighted_test_table_All.add_row([best_neighbors_cv_KNN_own_All,math.sqrt(mean_squared_error(ytst_All_KNN,y_pred_knn_own_weighted_All))])
print(KNNReg_own_weighted_test_table_All)

plt.scatter(ytst_All_KNN,y_pred_knn_own_weighted_All)
plt.grid()
plt.xlabel('Actual y')
plt.ylabel('Predicted y')
plt.title('Actual Value and Predicted Value using Weighted KNN on AllRounders Data')
plt.show()


#Algorithm for predicting IPL Winner

from array import array

def logScale(x,Stdscaler):
    x_log=np.log(x)
    x_log_std=Stdscaler.transform(x_log)
    return x_log_std


def getOutput(player,cate,model):
    print(player)
    if cate == 'allrounder':
        allRound_stats=player[0:4]+player[6:14]
        allRound_stats_Arr=np.asarray(allRound_stats,dtype=float)
        allRound_stats_Arr=logScale(allRound_stats_Arr.reshape(1,-1),Stdscaler_All)
        #print("Stats is",allRound_stats_Arr)
        #print("Predicted value is",sgd_reg_test_All.predict(allRound_stats_Arr.reshape(1,-1)))
        return model.predict(allRound_stats_Arr)
    elif cate == 'bowler':
        bowler_stats=player[0:5]
        bowler_stats_Arr=np.asarray(bowler_stats,dtype=float)
        bowler_stats_Arr=logScale(bowler_stats_Arr.reshape(1,-1),Stdscaler_Bowl)
        return model.predict(bowler_stats_Arr)
    else:
        batsmen_stats=player[0:4]+player[6:9]
        batsmen_stats_Arr=np.asarray(batsmen_stats,dtype=float)
        batsmen_stats_Arr=logScale(batsmen_stats_Arr.reshape(1,-1),Stdscaler_Bat)
        return model.predict(batsmen_stats_Arr)

def appendOutput(output,team,cate,country,final):
    if team in final:
        pass
    else:
        final[team] = list()
    final[team].append(list([output, cate, country]))
    
def getBest11(tup):
    sorted(tup, key=lambda x: x[0],reverse=True)
    reqBat = 4
    reqWk = 1
    reqAll = 2
    reqBow = 4
    MaxFor = 4
    currFor = 0
    curr = 0
    maxPlayers = 11

    team = list()
    for item in tup:
        if curr == maxPlayers:
            break
        if item[2] == 'F' and currFor == MaxFor:
            continue
        if item[1] == 'batsmen':
            if reqBat == 0:
                continue
            reqBat = reqBat - 1 
            curr = curr + 1              
            team.append(item)
        elif item[1] == 'bowler':
            if reqBow == 0:
                continue
            reqBow = reqBow - 1
            curr = curr + 1
            team.append(item)
        elif item[1] == 'wicketkeeper':
            if reqWk == 0:
                if reqBat == 0:
                    continue
                else:
                    reqBat = reqBat - 1
            else:
                reqWk = reqWk - 1
            team.append(item)
            curr = curr + 1
        else:
            if reqAll == 0:
                continue
            else:
                reqAll = reqAll - 1
            team.append(item)
            curr = curr + 1
        if item[2] == 'F':
            currFor = currFor + 1
    return team

from csv import reader
with open('ipl_Updated.csv', 'r') as read_obj:
    csv_reader = reader(read_obj)
    rows = list(csv_reader)
data = {}
for row in rows:
    if row[0] in data:
        pass
    else:
        data[row[0]] = {}
    if row[2] in data[row[0]]:
        pass
    else:
        data[row[0]][row[2]] = dict()
    if row[20] in data[row[0]][row[2]]:
        pass
    else:
        data[row[0]][row[2]][row[20]] = list()
    data[row[0]][row[2]][row[20]].append(row)

final = {}

for team in data:
    for cate in data[team]:
        for country in data[team][cate]:
            for player in data[team][cate][country]:
                if cate == 'allrounder':
                    player = player[4:]
                    allRound_stats=player[0:4]+player[6:14]
                    allRound_stats_Arr=np.asarray(allRound_stats,dtype=float)
                    allRound_stats_Arr=logScale(allRound_stats_Arr.reshape(1,-1),Stdscaler_All)
                    output = predictSGDOwn(allRound_stats_Arr,w_All,b_All)
                    appendOutput(output[0], team, cate, country, final)
                elif cate == 'bowler':
                    player = player[4:]
                    bowler_stats=player[0:5]
                    bowler_stats_Arr=np.asarray(bowler_stats,dtype=float)
                    bowler_stats_Arr=logScale(bowler_stats_Arr.reshape(1,-1),Stdscaler_Bowl)
                    output = predictSGDOwn(bowler_stats_Arr,w_Bowl,b_Bowl)
                    appendOutput(output[0], team, cate, country, final)
                else:
                    player = player[4:]
                    batsmen_stats=player[0:4]+player[6:9]
                    batsmen_stats_Arr=np.asarray(batsmen_stats,dtype=float)
                    batsmen_stats_Arr=logScale(batsmen_stats_Arr.reshape(1,-1),Stdscaler_Bat)
                    output = predictSGDOwn(batsmen_stats_Arr,w_Bat,b_Bat)
                    appendOutput(output[0], team, cate, country, final)
                            

totalRating = dict()
for team in final:
    bTeam = getBest11(final[team])
    totalSum = 0
    for tup in bTeam:
        totalSum = totalSum + tup[0]
    totalRating[team] = totalSum 

print(totalRating)


homeFactor = 1.05
homeDefactor = 0.95

home = dict({ 
    "CSK":"Chennai",
    "RR":"Rajastan",
    "DC":"Delhi",
    "SRH":"Hyderabad",
    "MI":"Mumbai",
    "KKR":"Kolkata",
    "RCB":"Bengaluru",
    "KX1P":"Punjab",
})

def pwinner(team1, team2, considerHF):
    if considerHF:
        if homeFactor*totalRating[team1] >= homeDefactor*totalRating[team2]:
            return team1
        else:
            return team2
    if totalRating[team1] >= totalRating[team2]:
        return team1
    else:
        return team2

import random
list_of_teams = list({"CSK", "MI", "RR", "KKR", "DC", "RCB", "SRH", "KX1P"})
matches = set()
totalLeagueMatches = 56
i=1

pointsTable = {}
for t in list_of_teams:
    pointsTable[t] = 0
while i <= totalLeagueMatches:
    curr = random.sample(list_of_teams, 2)
    if curr[0]+curr[1] in matches:
        continue
    matches.add(curr[0]+curr[1])
    venue = curr[0]
    winner = pwinner(curr[0], curr[1], True)
    pointsTable[winner] = pointsTable[winner] + 2
    print(curr[0]+"  vs  " +curr[1] + "   ||    venue at " + venue)
    print("Winner is "+ winner +"\n")
    i=i+1
import operator
pointsTable = sorted(pointsTable.items(), key=operator.itemgetter(1), reverse=True)

print("Qualifier1:")
print(pointsTable[0][0]+"  vs  " +pointsTable[1][0])
qual1=pwinner(pointsTable[0][0],pointsTable[1][0],False)
qual1L=pointsTable[1][0] if(qual1==pointsTable[0][0]) else pointsTable[0][0]
print("Winner is " + qual1+"\n")

print("Eliminator:")
print(pointsTable[2][0] + "  vs  "+pointsTable[3][0])
elemW = pwinner(pointsTable[2][0],pointsTable[3][0],False)
print("Winner is " + elemW+"\n")


print("Qualifier2:")
print(qual1L+"  vs  " +elemW)
qual2=pwinner(qual1L,elemW,False)
print("Winner is " + qual2+"\n")

print("******FINAL******")
print(qual1+"  vs  " +qual2)
finalWinner = pwinner(qual1, qual2, False)
print("Winner is " + finalWinner+"\n")

print(finalWinner)

final = {}

for team in data:
    for cate in data[team]:
        for country in data[team][cate]:
            for player in data[team][cate][country]:
                if cate == 'allrounder':
                    player = player[4:]
                    allRound_stats=player[0:4]+player[6:14]
                    allRound_stats_Arr=np.asarray(allRound_stats,dtype=float)
                    allRound_stats_Arr=logScale(allRound_stats_Arr.reshape(1,-1),Stdscaler_All)
                    output = KNNRegressionOwn(Xtrn_All,ytrn_All,best_neighbors_cv_KNN_own_All,allRound_stats_Arr)
                    appendOutput(output[0], team, cate, country, final)
                elif cate == 'bowler':
                    player = player[4:]
                    bowler_stats=player[0:5]
                    bowler_stats_Arr=np.asarray(bowler_stats,dtype=float)
                    bowler_stats_Arr=logScale(bowler_stats_Arr.reshape(1,-1),Stdscaler_Bowl)
                    output = KNNRegressionOwn(Xtrn_Bowl,ytrn_Bowl,best_neighbors_cv_KNN_own_Bowl,bowler_stats_Arr)
                    appendOutput(output[0], team, cate, country, final)
                else:
                    player = player[4:]
                    batsmen_stats=player[0:4]+player[6:9]
                    batsmen_stats_Arr=np.asarray(batsmen_stats,dtype=float)
                    batsmen_stats_Arr=logScale(batsmen_stats_Arr.reshape(1,-1),Stdscaler_Bat)
                    output = KNNRegressionOwn(Xtrn_Bat,ytrn_Bat,best_neighbors_cv_KNN_own_Bat,batsmen_stats_Arr)
                    appendOutput(output[0], team, cate, country, final)
                            

totalRating = dict()
for team in final:
    bTeam = getBest11(final[team])
    totalSum = 0
    for tup in bTeam:
        totalSum = totalSum + tup[0]
    totalRating[team] = totalSum 

print(totalRating)

pointsTable = {}
for t in list_of_teams:
    pointsTable[t] = 0
i=1
matches = set()

while i <= totalLeagueMatches:
    curr = random.sample(list_of_teams, 2)
    if curr[0]+curr[1] in matches:
        continue
    matches.add(curr[0]+curr[1])
    venue = curr[0]
    winner = pwinner(curr[0], curr[1], True)
    pointsTable[winner] = pointsTable[winner] + 2
    print(curr[0]+"  vs  " +curr[1] + "   ||    venue at " + venue)
    print("Winner is "+ winner +"\n")
    i=i+1
import operator
pointsTable = sorted(pointsTable.items(), key=operator.itemgetter(1), reverse=True)

print("Qualifier1:")
print(pointsTable[0][0]+"  vs  " +pointsTable[1][0])
qual1=pwinner(pointsTable[0][0],pointsTable[1][0],False)
qual1L=pointsTable[1][0] if(qual1==pointsTable[0][0]) else pointsTable[0][0]
print("Winner is " + qual1+"\n")

print("Eliminator:")
print(pointsTable[2][0] + "  vs  "+pointsTable[3][0])
elemW = pwinner(pointsTable[2][0],pointsTable[3][0],False)
print("Winner is " + elemW+"\n")


print("Qualifier2:")
print(qual1L+"  vs  " +elemW)
qual2=pwinner(qual1L,elemW,False)
print("Winner is " + qual2+"\n")

print("******FINAL******")
print(qual1+"  vs  " +qual2)
finalWinner = pwinner(qual1, qual2, False)
print("Winner is " + finalWinner+"\n")

print(finalWinner)



