# SpectralClustering
This class is an implementation of the spectral clustering algorithm. The class includes two main methods: fit and predict.

## /__init__/
In the constructor __init__, you can pass the number of clusters you want to see as a result of the clustering algorithm. This number is stored in the n_clusters variable.

The gaussian_kernel method computes the Gaussian similarity matrix of the data. Given a data matrix X, it calculates the pairwise distance between all data points and returns a matrix of weights that are based on the Euclidean distance between each pair of data points.

## fit

The fit method computes the Laplacian matrix, which is used to cluster the data. It starts by computing the weight matrix using gaussian_kernel. It then computes the degree matrix D, which is a diagonal matrix that contains the sum of each row of the weight matrix. Finally, it computes the Laplacian matrix L as the difference between D and W.

## predict
The predict method computes the cluster assignments for a new dataset. It first computes the Laplacian matrix for the new dataset using the same gaussian_kernel function. It then calculates the eigenvectors and eigenvalues of the Laplacian matrix. The eigenvectors corresponding to the smallest n_clusters eigenvalues are extracted and passed to a Gaussian mixture model for clustering.


To use this class, you can create an instance of the SpectralClustering class with the desired number of clusters, and then call the fit method with your data to compute the Laplacian matrix. You can then call the predict method to cluster a new dataset using the computed Laplacian matrix.

```
# create a SpectralClustering object with 3 clusters
sc = SpectralClustering(n_clusters=3)
# fit the model
sc.fit(X)
# predict the classes
sc.predict(X)
```
