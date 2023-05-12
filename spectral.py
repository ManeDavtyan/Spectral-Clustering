import numpy as np
from scipy.linalg import eig
from sklearn.mixture import GaussianMixture
from sklearn.metrics.pairwise import pairwise_distances


class SpectralClustering:
    def __init__(self, n_clusters=3):
        self.n_clusters = n_clusters

    def gaussian_kernel(self, X):
        sigma = np.std(X)
        weights = np.exp(-pairwise_distances(X, metric='sqeuclidean') / (2 * sigma ** 2))
        return weights

    def fit(self, X):
        self.X = X
        self.W = self.gaussian_kernel(X)
        self.D = np.diag(np.sum(self.W, axis=1))
        self.L = self.D - self.W

    def predict(self,X):
        W = self.gaussian_kernel(X)
        D = np.diag(np.sum(W, axis=1))
        L = D - W
        eigenval, eigenvec = eig(L)
        index = np.argsort(eigenval)[:self.n_clusters]
        reduced = eigenvec[:, index]
        # applying GMM to the embedding
        gmm = GaussianMixture(n_components=self.n_clusters)
        gmm.fit(reduced)
        clusters = gmm.predict(reduced)
        return clusters