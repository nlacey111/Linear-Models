
install.packages(c('quantmod','ff','foreign','R.matlab'),dependency=T)
suppressPackageStartupMessages(library(tidyverse))

data1 <- read_csv('GOOG.csv',show_col_types = FALSE)
head(data1, 5)

data1$log_closing_prices <- log(data1$Close)
data1$index <- 1:252

model2<- lm(data1$log_closing_prices ~ data1$index)

ggplot() + 
  geom_point(aes(x = data1$index, 
                          y = data1$log_closing_prices), colour = 'purple') +
  geom_line(aes(x = data1$index,
                y = predict(model2, newdata = data1)), colour = 'black') +
  ggtitle('Closing Price vs Date') +
  xlab('Date') +
  ylab('Closing Stock Price')

