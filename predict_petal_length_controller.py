import seaborn as sns
from sklearn.linear_model import LinearRegression
import pandas as pd


#Loading iris dataset from seaborn library
iris_data= sns.load_dataset("iris")

X = iris_data.petal_width.as_matrix(columns=None)
X=X.reshape(-1, 1)

#Fitting linear model to predict petal length if petal width is given
lm=LinearRegression()
model=lm.fit(X,iris_data.petal_length)


#User defined function
def function_predict(petal_width):
           # convert the input to a number
           petal_width= int(petal_width)
      
           #create the prediction data frame
           prediction_data=pd.DataFrame({'petal_width':[petal_width]})
      
           # create the prediction
           return(lm.predict(prediction_data))