- Decision trees are supervised methods
- Regression/Classification
- If-then rules
- think about 20 question game. A broader question like `is it alive?` can be a lot more **informative** at the beginning of the game than `does it have yellow stripes?`.
- leaf node is at the bottom of the tree
- Rather than figuring out a set of question manually, we use decision trees as a `supervised` algorithm to find those questions for us.
- What is a `split point`? 
- A split is called `informative` if it does an excellent job at splitting one class from the others. Example for `informative split` in the `iris` data set is 
    - if `petal length` <= 2.35 cm then it is `setosa`, where a single measurement is sufficient to create a homogenious node.
- `Information Gain`
- `Pure lean nodes`
- For `regression` problems the target value would be the mean value of the data points in that leaf node.
- Decision Trees tend to overfit. Strategies to prevent that are:
    - Pre-prunnig: Stop the growth early (use `max_depth` or `max_leaf_node` or `min_sample_leaf`)
        - `min_sample_leaf` specifies the minimum number of data points in a leaf before it can be split further. This helps preventing overfitting.
    - Post-prunning: create max depth tree and then prune nodes (not available in `sklearn`)
- Easy to interpret
## Code:
    from sklearn.tree import DecisionTreeClassifier
    clf = DecisionTreeClassifier().fit(X_train, y_train)

## Feature Importance Calculation
- a value between 0 (the feature didn't get used for prediction) and 1 (the feature predicts the target perfectly)
- The feature importance values are normalized to sum to 1.
    - `clf.feature_importance_` in sklearn
- Lower value of `feature importance` doesn't mean the feature is not important. Instead it means that the feature wasn't selected as a splitting feature at the top of the tree.
    - Lower values could mean the feature is highly correlated to another informative feature
    - Because feature importance values change across runs, they are usually averaged over multiple runs

## Pros and Cons
- easily visualized
- no normalization or preprocessing is needed
- mixture of features would be no problem (binary/continous/categorical)
- tend to overfit
    - use ensemble of Decision Trees