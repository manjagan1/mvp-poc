import os
import rpy2.robjects as robjects
from rpy2.robjects.packages import importr



# change this to a config file. Directory where the R model will be saved
R_MODEL_NAME = os.path.join(os.path.dirname(__file__),"final_model.rds")

# the directory where the R code will be save
R_CODE_FILE = os.path.join(os.path.dirname(__file__),"RModel.R")



r_source = robjects.r['source']
r_source(R_CODE_FILE)
r_create_model = robjects.globalenv['create_model']


print (R_MODEL_NAME)
print (R_CODE_FILE)


def invoke_R_model():
    print ("invoke R code to create the model, inputs should be the filename with the features")
    r_create_model("/data/cs-training_Transactional.csv")
    base = importr('base')
    model = base.readRDS(R_MODEL_NAME)
    base.summary(model)

if __name__ == "__main__":
    # Invoke R Model from python
    invoke_R_model()