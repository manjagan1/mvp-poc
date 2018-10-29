
create_model <- function(fileName) {

    library(tidyverse)
    library(ggpubr)
    theme_set(theme_pubr())
    workingDir <- getwd()
    csvFile <- dirname(workingDir)
    pricingData <- read.csv(file=paste0(csvFile,fileName), header=TRUE, sep=",")
    pricingModel <- lm(formula=NumberOfTime3059DaysPastDueNotWorse~NumberRealEstateLoansOrLines, data=pricingData)
    summary(pricingModel)
    # save the model to disk
    saveRDS(pricingModel, "./final_model.rds")
}


# load the model
# create_model("/data/cs-training_Transactional.csv")
# super_model <- readRDS("./final_model.rds")
# summary(super_model)
