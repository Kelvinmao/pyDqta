from numpy import *

import matplotlib.pyplot as plt

def loadDataSet(fileName, delim='\t'):
    fr = open(fileName)
    stringArr = [line.strip().split(delim) for line in fr.readlines()]
    datArr = [map(float,line) for line in stringArr]
    return mat(datArr)

def zeroMean(dataMat):
    meanVal=mean(dataMat,axis=0)
    newDataMat=dataMat-meanVal
    return newDataMat,meanVal

def computeCovMat(dataMat):
    newMat,meanVal=zeroMean(dataMat)
    covMat=cov(newMat,rowvar=0)
    return covMat

def eigenValue(covMat):
    eigVal,eigMat=linalg.eig(mat(covMat))
    return eigVal,eigMat

def savePricinpal(eigVal,eigMat,covMat,newDataMat,dim,meanVal):
    eigValSorted=argsort(eigVal)
    eigValNMax=eigValSorted[-1:-(dim+1):-1]
    print  eigValNMax
    eigMatN=eigMat[:,eigValNMax]
    lowDataMat=newDataMat*eigMatN
    recordMat=(lowDataMat*eigMatN.T)+meanVal
    return recordMat,lowDataMat

if __name__ == '__main__':
    mata = loadDataSet('C:/Users/39235/Desktop/PCA-master/testSet.txt')
    newdatamat,meanval=zeroMean(mata)
    conv=computeCovMat(newdatamat)
    eigval,eigmat=eigenValue(conv)
    savePricinpal(eigval,eigmat,conv,newdatamat,999999,meanval)
