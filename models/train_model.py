from sklearn.model_selection import train_test_split
from .supervised_model import train_supervised_model
from .unsupervised_model import train_unsupervised_model
from .evaluate import evaluate_model

def train_models(df):
    # Prepare data
    X = df.drop('target', axis=1)
    y = df['target']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train supervised model
    supervised_model = train_supervised_model(X_train, y_train)
    evaluate_model(supervised_model, X_test, y_test)

    # Train unsupervised model
    unsupervised_model = train_unsupervised_model(X)
