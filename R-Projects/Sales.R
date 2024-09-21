# https://www.learnbymarketing.com/tutorials/linear-regression-in-r/#:~:text=lm()%20Function-,Linear%20Regression%20Example%20in%20R%20using%20lm()%20Function,variable%20from%20your%20new%20model.
  
#You may need to use the setwd(directory-name) command to
#change your working directory to wherever you saved the csv.
#Use getwd() to see what your current directory is.
dataset = read.csv("D:/github/R-Projects/data-marketing-budget-12mo.csv", header=T,
                   colClasses = c("numeric", "numeric", "numeric"))

#Simple (One Variable) and Multiple Linear Regression Using lm()
simple.fit = lm(Sales~Spend, data=dataset)
summary(simple.fit)
multi.fit = lm(Sales~Spend+Month, data=dataset)
summary(multi.fit)

#Analyzing Residuals
layout(matrix(c(1,1,2,3),2,2,byrow=T))
#Spend x Residuals Plot
plot(simple.fit$resid~dataset$Spend[order(dataset$Spend)],
     main="Spend x Residuals\nfor Simple Regression",
     xlab="Marketing Spend", ylab="Residuals")
abline(h=0,lty=2)
#Histogram of Residuals
hist(simple.fit$resid, main="Histogram of Residuals",
     ylab="Residuals")
#Q-Q Plot
qqnorm(simple.fit$resid)
qqline(simple.fit$resid)


# Residuals are normally distributed
library(fBasics)
jarqueberaTest(simple.fit$resid) #Test residuals for normality
#Null Hypothesis: Skewness and Kurtosis are equal to zero
#Residuals X-squared: 0.9575 p Value: 0.6195
# With a p value of 0.6195, we fail to reject the null hypothesis that the skewness and kurtosis 
# of residuals are statistically equal to zero.

# Residuals are independent
library(lmtest) #dwtest
dwtest(simple.fit) #Test for independence of residuals
#Null Hypothesis: Errors are serially UNcorrelated
#Results: DW = 1.1347, p-value = 0.03062
# Based on the results, we can reject the null hypothesis that the errors are serially uncorrelated.  
# This means we have more work to do.

layout(matrix(c(1,2,3,4),2,2,byrow=T))
plot(multi.fit$fitted, rstudent(multi.fit),
     main="Multi Fit Studentized Residuals",
     xlab="Predictions",ylab="Studentized Resid",
     ylim=c(-2.5,2.5))
abline(h=0, lty=2)
plot(dataset$Month, multi.fit$resid,
     main="Residuals by Month",
     xlab="Month",ylab="Residuals")
abline(h=0,lty=2)
hist(multi.fit$resid,main="Histogram of Residuals")
qqnorm(multi.fit$resid)
qqline(multi.fit$resid)

# Residuals are Normally Distributed
library(fBasics)
jarqueberaTest(multi.fit$resid) #Test residuals for normality
#Null Hypothesis: Skewness and Kurtosis are equal to zero
#Residuals X-squared: 1.3627 p Value: 0.5059

# Residuals are independent
library(lmtest) #dwtest
dwtest(multi.fit) #Test for independence of residuals
#Null Hypothesis: Errors are serially UNcorrelated
#Results: DW = 2.1077, p-value = 0.3133
multi.fit

