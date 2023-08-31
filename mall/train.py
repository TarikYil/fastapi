import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression



df2 = pd.read_csv("C:\\Users\\41muh\\OneDrive\\Masaüstü\\api_deploy\\mall\\dataset\\advertising.csv")

# Output variable
y = df2.iloc[:, -1]

# Feature matrix
X = df2.iloc[:, :-1]


# split test train
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)


reg_model = LinearRegression().fit(X_train, y_train)


joblib.dump(reg_model, "saved_models/pipline_model.pkl")


