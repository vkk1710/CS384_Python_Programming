# All decimal 3 places
import tutorial01 as A1
import math
# Function to compute mean
def mean(first_list):
    # mean Logic
    mean_value = summation(first_list)/len(first_list)
    mean_value = round(mean_value,3)
    return mean_value


# Function to compute median. You cant use Python functions
def median(first_list):
    # median Logic
    sort = sorting(first_list)
    n = len(first_list)
    if(n%2==0):
        median_value = (sort[n//2] + sort[n//2 - 1])/2
    else:
        median_value = sort[n//2]
    median_value = round(median_value,3)
    return median_value


# Function to compute Standard deviation. You cant use Python functions
def standard_deviation(first_list):
    # Standard deviation Logic
    standard_deviation_value = math.sqrt(variance(first_list))
    standard_deviation_value = round(standard_deviation_value,3)
    return standard_deviation_value


# Function to compute variance. You cant use Python functions
def variance(first_list):
    # variance Logic
    x = mean(first_list)
    s=0
    for i in first_list:
        if(isinstance(i,str)):
            return 0
        s+=A1.power(i-x,2)
    variance_value = s/len(first_list) 
    variance_value = round(variance_value,3)
    return variance_value


# Function to compute RMSE. You cant use Python functions
def rmse(first_list, second_list):
    # RMSE Logic
    rmse_value = math.sqrt(mse(first_list, second_list))
    rmse_value = round(rmse_value,3)
    return rmse_value


# Function to compute mse. You cant use Python functions
def mse(first_list, second_list):
    # mse Logic
    if(len(first_list)!=len(second_list)):
        return 0
    mse_value = 0
    for i in range(len(first_list)):
        if(isinstance(first_list[i],str) or isinstance(second_list[i],str)):
            return 0
        mse_value += A1.power(first_list[i]-second_list[i],2)
    mse_value = mse_value/len(first_list)
    mse_value = round(mse_value,3)
    return mse_value


# Function to compute mae. You cant use Python functions
def mae(first_list, second_list):
    # mae Logic
    if(len(first_list)!=len(second_list)):
        return 0
    mae_value = 0
    for i in range(len(first_list)):
        if(isinstance(first_list[i],str) or isinstance(second_list[i],str)):
            return 0
        mae_value += abs(first_list[i]-second_list[i])
    mae_value = mae_value/len(first_list)
    mae_value = round(mae_value,3)
    return mae_value


# Function to compute NSE. You cant use Python functions
def nse(first_list, second_list):
    # nse Logic
    if(len(first_list)!=len(second_list)):
        return 0
    for i in second_list:
        if(isinstance(i, str)):
            return 0
    m = mse(first_list, second_list)
    var = variance(first_list)
    if(var==0):
        return 0
    nse_value = 1 - (m/var)
    nse_value = round(nse_value,3)
    return nse_value


# Function to compute Pearson correlation coefficient. You cant use Python functions
def pcc(first_list, second_list):
    # nse Logic
    x = mean(first_list)
    y = mean(second_list)
    if(len(first_list)!=len(second_list)):
        return 0
    n = len(first_list)
    d1 = standard_deviation(first_list)*math.sqrt(n)
    d2 = standard_deviation(second_list)*math.sqrt(n)
    if(d1==0 or d2==0):
        return 0
    pcc_value=0
    for i in range(n):
       if(isinstance(first_list[i],str) or isinstance(second_list[i],str)):
            return 0 
       pcc_value += (first_list[i]-x)*(second_list[i]-y) 
    pcc_value = pcc_value/(d1*d2) 
    pcc_value = round(pcc_value,3)
    return pcc_value


# Function to compute Skewness. You cant use Python functions
def skewness(first_list):
    # Skewness Logic
    x = mean(first_list)
    s = standard_deviation(first_list)
    if(s==0):
        return 0
    skewness_value = 0
    for i in first_list:
        skewness_value += A1.power((i-x)/s,3)
    skewness_value = skewness_value/len(first_list)
    skewness_value = round(skewness_value,3)
    return skewness_value
    
def sorting(first_list):
    # Sorting Logic
    sorted_list = first_list[:]
    for i in range(len(sorted_list)):
        if(isinstance(sorted_list[i],str)):
            return []
        j=i-1
        while(j>=0 and sorted_list[j]>sorted_list[j+1]):
            c = sorted_list[j]
            sorted_list[j] = sorted_list[j+1]
            sorted_list[j+1] = c
            j-=1          
    return sorted_list


# Function to compute Kurtosis. You cant use Python functions
def kurtosis(first_list):
    # Kurtosis Logic
    x = mean(first_list)
    s = standard_deviation(first_list)
    if(s==0):
        return 0
    kurtosis_value = 0
    for i in first_list:
        kurtosis_value += A1.power((i-x)/s,4)
    kurtosis_value = kurtosis_value/len(first_list)
    kurtosis_value = round(kurtosis_value,3)
    return kurtosis_value


# Function to compute sum. You cant use Python functions
def summation(first_list):
    # sum Logic
    summation_value=0
    for i in first_list:
        if(isinstance(i,str)):
            return 0
        summation_value+=i
    summation_value = round(summation_value,3)    
    return summation_value
