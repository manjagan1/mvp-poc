library(tidyverse)
library(ggpubr)
theme_set(theme_pubr())
workingDir <- getwd()
csvFile <- dirname(dirname(dirname(workingDir)))
pricingData <- read.csv(file=paste0(csvFile,"/data/cs-training_Transactional.csv"), header=TRUE, sep=",")
pricingModel <- lm(formula=NumberOfTime3059DaysPastDueNotWorse~NumberRealEstateLoansOrLines, data=pricingData)
summary(pricingModel)
# save the model to disk
saveRDS(pricingModel, "./final_model.rds")

# load the model
super_model <- readRDS("./final_model.rds")
print(super_model) 
