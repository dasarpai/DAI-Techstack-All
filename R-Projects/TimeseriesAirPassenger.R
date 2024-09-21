data(AirPassengers)
class(AirPassengers)
start(AirPassengers)
end(AirPassengers)
frequency(AirPassengers)
summary(AirPassengers)

# 2. Exploration of Time Series Data in R
#The number of passengers are distributed across the spectrum
plot(AirPassengers)

#This will plot the time series
abline(reg=lm(AirPassengers~time(AirPassengers)))

#This will print the cycle across years.
cycle(AirPassengers)

#This will aggregate the cycles and display a year on year trend
plot(aggregate(AirPassengers,FUN=mean))

#Box plot across months will give us a sense on seasonal effect
boxplot(AirPassengers~cycle(AirPassengers))

# 3. Introduction to ARMA Time Series Modeling

# install.packages('aTSA')
library('aTSA')

stationary.test((diff(AirPassengers)))



x <- arima.sim(list(order = c(1,0,0),ar = 0.2),n = 100)
stationary.test(x)
stationary.test(x, method = "pp")
