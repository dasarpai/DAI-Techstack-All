INC=c(3.5,5.6,13.9,8.4,9.5,8.1)
DEF=c(1,0,0,1,0,0)
mod1=glm(as.factor(DEF)~INC,family="binomial")
summary(mod1)

#################################
###  CASE STUDY ANALSYSIS
#################################
##### Importing data
data1=read.csv("data1.csv")

##### Filtering data: considering only those customers for the analysis for whom the 3rd visit happened 
data2=subset(data1,data1$NUM_PAID_VIS==2&is.na(data1$VISIT3)==FALSE)

##### Checking number of observations (customers) on whom the analysis will be performed 
N=nrow(data2)
N
######### Filtering relevant columns needed for analysis
########################################################
data_an=data2[,c(5,7,8,9,10,11,12,14,15,16,17,18,19)]
nn=nrow(data_an)

### Creating training and test set
set.seed(123)
indx=sample(1:nn,0.9*nn)
traindata=data_an[indx,]
testdata=data_an[-indx,]

#### Fitting full logistic regression (LR) model with all features
fullmod=glm(as.factor(VISIT3)~as.factor(PROD_MOD2)
            +as.factor(CITY2)+AGE+as.factor(GEN)+INCOME+as.factor(LOAN)
            +NUM_FREE_VIS+FREE_AV_US+PAID_AV_US+PAID_AV_TIME+PAID_AV_FD
            +(NUM_OVRCH),data=traindata,family="binomial")
summary(fullmod)













#### Selecting features for fitting reduced logistic regression model
library(MASS)
step=stepAIC(fullmod)

mod2=glm(as.factor(VISIT3) ~ as.factor(PROD_MOD2) + as.factor(LOAN) + 
           NUM_FREE_VIS + FREE_AV_US + PAID_AV_US, family = "binomial", 
         data = traindata)
summary(mod2)












### predicting success probabilities using the LR model
testdata_new=testdata[,c(1,6,7,8,9)]
pred_prob=predict(mod2,testdata_new,type="response")
hist(pred_prob)















### predicting success probability for an individual
sampletest=data.frame(t(c(6,0,3,3500,5000)))
colnames(sampletest)=c("PROD_MOD2","LOAN","NUM_FREE_VIS","FREE_AV_US","PAID_AV_US")
predict(mod2,sampletest,type="response")













#### Plotting ROC 
library(pROC)
roc1=roc(testdata[,13],pred_prob,plot=TRUE,legacy.axes=TRUE)
plot(roc1)
roc1$auc

















#### Using ROC in deciding threshold
thres=data.frame(sen=roc1$sensitivities, spec=roc1$specificities,thresholds=roc1$thresholds)
thres[thres$sen>0.65&thres$spec>0.4,]

library(caret)
pred_Y=ifelse(pred_prob > 0.098,1,0)
confusionMatrix(as.factor(testdata[,13]), as.factor(pred_Y))













###############################
## Random Forest
###############################
library(randomForest)
data_an$VISIT3=as.factor(data_an$VISIT3)
data_an$PROD_MOD2=as.factor(data_an$PROD_MOD2)
data_an$CITY2=as.factor(data_an$CITY2)
data_an$GEN=as.factor(data_an$GEN)
data_an$LOAN=as.factor(data_an$LOAN)


modRF=randomForest(VISIT3~ ., data=data_an,ntree=500, mtry=8)
modRF

testdata$VISIT3=as.factor(testdata$VISIT3)
testdata$PROD_MOD2=as.factor(testdata$PROD_MOD2)
testdata$CITY2=as.factor(testdata$CITY2)
testdata$GEN=as.factor(testdata$GEN)
testdata$LOAN=as.factor(testdata$LOAN)




predict(modRF,testdata[3,-13],type="response")













######################################
####################
fulldat=read.csv("demo_dt.csv")

datatrain=fulldat[1:90,]
datatest=fulldat[91:100,]


library(rpart)
# grow tree
fit=rpart(as.factor(HOSP) ~ AGE + SBP ,
          method="class", data=datatrain)


# create attractive postscript plot of tree
library(rpart.plot)
rpart.plot(fit)

### predict
pred=predict(fit,datatest[,1:2],type="class")
table(datatest[,3], pred)





