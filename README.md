# SpectralClustering
Implemented spectral clustering algorithm. The model includes fit and predict methods. For calling both of them you need to provide the data , like fit(X) or predict(X). But in general to call the class you need to provide a number of clusters k you want to see as a result of this clustering algorithm. 

Here is an example of calling the class.

sc = SpectralClustering(8)
sc.fit(X)
sc.predict(X)


## Fit
The weights of the matrix W are taken from the formula of gaussian kernel. The Laplace matrix is taken to be the subtraction of W and D, which is diagonal matrix of d values.
## Predict
The matrices above like W, L, D are counted for the given data, then the solution is taken to be the matrix of k eigenvectors corresponding to the eigenvalues from 2nd to k-th. In this case k is again a parameter which is defined by the user. 

