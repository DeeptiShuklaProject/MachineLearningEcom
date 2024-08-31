def custom_metric(y_true, y_pred):
    # Define your custom metric here
    return sum(y_true == y_pred) / len(y_true)
