## PCA
- unsupervised
- variations:
    - Sparse PCA
    - Kernel PCA
- make sure data is standardized
- since unsupervised, no need to split into train/test
- an application of PCA would be to reduce dimensionality before the data is fed to a supervised method.
    - in the breast cancer data set reducing the dataset to 2 features will make it almost linearly separable.



## Maniforld learning algorithms
- very efficient at reducing high dimensional datasets into lower dimensional datasets
- Some example algorithms in this field are:
    - MDS or multidimensional scaling
        - `from sklean.manfold import MDS`
        - `mds = MDS(n_components=2)`
        - `mds.fit_transform(myData)`
    - t-SNE: finds a 2-D projection 


-[wikipedia](https://en.wikipedia.org/wiki/Nonlinear_dimensionality_reduction)