- is an ensemble method which aggregates simpler models
- constructed from multiple decision trees
- both for classification `RandomForesetClassifier` and regression `RandomForestRegressor`
## randomization in random foresets:
randomness introduced in 2 ways:
1. the data used to build each tree is randomly selected
  - bootstrap samples: create a sample the same size as the original data set by sampling with replacement from it
2. the feature used to split is randomly selected
  - we only look at a random subset of features as opposed to the whole set of features, which is the case in decision trees

## Decision parameters:
- how many trees to build
- how many features to consider when splitting

## Predictions
- each tree prediction a value for the new data
  - for regression: average the tree predictions
  - for classification: voting system