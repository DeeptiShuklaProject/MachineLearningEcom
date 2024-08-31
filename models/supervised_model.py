from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression

def train_supervised_model(X_train, y_train, model_type='random_forest'):
    if model_type == 'random_forest':
        model = RandomForestClassifier()
    elif model_type == 'logistic_regression':
        model = LogisticRegression()
    model.fit(X_train, y_train)
    return model
