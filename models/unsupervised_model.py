from sklearn.cluster import KMeans

def train_unsupervised_model(X, n_clusters=3):
    model = KMeans(n_clusters=n_clusters)
    model.fit(X)
    return model
