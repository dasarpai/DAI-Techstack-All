setwd("D:/github/1-Projects/Projects-ML/Health-MLK04-BreastCancer")


# library(dplyr)
# library(ggplot2)
# library(corrplot)
# library(gridExtra)
# library(lattice)
# library(C50)
# library(caret)
# library(purrr)
# library(ggfortify)
# library(gmodels)
# library(nnet)
# library(vcd)
# library(NeuralNetTools)

wbcd <- read.csv("BreastCancer-data.csv", header=T, stringsAsFactors=F) 

wbcd$X <- NULL
wbcd <- wbcd[,-1]
wbcd$diagnosis <- factor(ifelse(wbcd$diagnosis=="B","Benign","Malignant"))

str(wbcd)

library(PerformanceAnalytics)

chart.Correlation(wbcd[,c(2:11)],histogram=TRUE, col="grey10", pch=1, main="Cancer Mean")

# install.packages("ggplot2", dependencies=TRUE)
# install.packages("GGally", dependencies=TRUE)

# install.packages("ggplot2")
# install.packages("GGally")
library("ggplot2")
library("GGally")
# ggpairs(data)+theme_bw()


#library(ggpairs)

ggpairs(wbcd[,c(2:11,1)], aes(color=diagnosis, alpha=0.75), 
        lower=list(continuous="smooth"))+ theme_bw()+
  labs(title="Cancer Mean")+
  theme(plot.title=element_text(face='bold',color='black',hjust=0.5,size=10))


ggcorr(wbcd[,c(2:11)], name = "corr", label = TRUE)+
  theme(legend.position="none")+
  labs(title="Cancer Mean")+
  theme(plot.title=element_text(face='bold',color='black',hjust=0.5,size=10))


#ap <- available.packages()
#data()





help(stat.desc)

library(Hmisc)
Hmisc::describe(wbcd)
Hmisc::describe(wbcd['radius_mean'])

library (pastecs)
stat.desc (wbcd['radius_mean'])         
stat.desc(wbcd[,2:5], basic=TRUE, desc=TRUE, norm=TRUE, p=0.95)

library(dummies)

get.dummy(wbcd, 'diagnosis')

# data( iris ) 
# d <- dummy.data.frame( iris )
# get.dummy( d, 'Species' )

