- Called naive because they assume each feature of the instances are independent [which is not true, price can be dependent on location and land size]
- learning the naive classifier is very fast
- The generalization performance can be a bit worse, but they are still highly efficient
- 3 flavours of naive bayes available in scikitlearn:
    - Bernooulli: binary features - good for textual data
    - Multinomial: discrete features - good for textual data
    - Gaussian: continuous/real-valued features
        - Generally has a parabolic decision boundary
        - `from sklearn.naive_bayes import GaussianNB`
        - `nbclf = GaussianNB().fit(X_train, y_train)`
- Naive Bayes classifiers support `parital_fit()` method in sklearn if your data set doesn't fit in the memory.
- Typically NB is used with high dimensional data with lots of data points

## Pros
- easy to understand
- simple and efficient
- work well with high dimensional
- baseline to compare

## Const
- assumption that features are independent, and as a result worse generalization performance
- confidence estimates for predictions are not very accurate