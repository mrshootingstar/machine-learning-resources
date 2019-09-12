1. Frame the problem:
    - What is the business objective
    - How is the company benefiting from the project
    - this will determine the model to be used and the evaluation metrics and the effort needed.
    - Is there an existing solution that can be used as the benchmark?
2. Check the assumptions
    - How is the output of the model used?
3. Check data:
    - Histogram tail heavy ==> Some ML approaches are sensitive to this
    - Features different scales ==> normalize/standardize
    - missing values:
      0. get rows with any missing values: `df[df.isnull().any(axis=1)]`
      1. drop the whole rows: `dropna()`
      2. drop the whole column/feature: `drop()` or `dropna(axis=1)`
      3. fill missing values with other values: `fillna(value, inplace=True)`
        - for this option, the same value should be used to fill both training and test data sets.
        - use an `Imputer` (after temporarily dropping non-numerical columns):
            - `from sklearn.impute import SimpleImputer`
            - `imputer = SimpleImputer(strategy="median")`
            - `imputer.fit(test_data)`
            - `imputer.transform(test_data)`
    
    from sklearn.impute import SimpleImputer
    imputer = SimpleImputer(strategy="median")
    # drop non numerical attributes
    housing_num = housing.drop("ocean_proximity", axis=1)
    # fit the imputer instance
    imputer.fit(housing_num)
    # sanity check the following lines should produce the same results
    imputer.statistics_
    housing_num.median().values
    # the actual transformation
    X = imputer.transform(housing_num)
    # optional: if you want to put it back in a dataframe format
    housing_tr = pd.DataFrame(X, columns=housing_num.columns,
                          index=housing_num.index)

- [design patters in scikit learn](https://arxiv.org/abs/1309.0238)

## Create user defined transformers
- create a class and implement `fit()`, `transform()`, `fit_transform()` [not needed if adding `TransformerMixin` as a base class]
- adding `BaseEstimator` as a base class gives you 2 extra methods: `get_params()` and `set_params()`.
- If you want to add a `hyperparameter` to your transformer, add it to the `__init__` method.
```python
from sklearn.base import BaseEstimator, TransformerMixin

rooms_ix, bedrooms_ix, population_ix, households_ix = 3, 4, 5, 6

# BaseEstimator
# TransformerMixin
class CombinedAttributesAdder(BaseEstimator, TransformerMixin):
    def __init__(self, add_bedrooms_per_room = True): # no *args or **kargs
        self.add_bedrooms_per_room = add_bedrooms_per_room
    def fit(self, X, y=None):
        return self  # nothing else to do
    def transform(self, X, y=None):
        rooms_per_household = X[:, rooms_ix] / X[:, households_ix]
        population_per_household = X[:, population_ix] / X[:, households_ix]
        if self.add_bedrooms_per_room:
            bedrooms_per_room = X[:, bedrooms_ix] / X[:, rooms_ix]
            return np.c_[X, rooms_per_household, population_per_household,
                         bedrooms_per_room]

        else:
            return np.c_[X, rooms_per_household, population_per_household]

attr_adder = CombinedAttributesAdder(add_bedrooms_per_room=False)
housing_extra_attribs = attr_adder.transform(housing.values)
```


## Feature Scaling
- normalization via `MinMaxScaler`: subtract the min vaue and divide by the max minus min
    - has a `feature_rante` hyper parameter if you don't want your end result to be in the rante [0,1]
- standadization via `StandardScaler`: subtract the mean and divide by std
    - unlike normalization standardization doesn't bound values to a specific range which can be a problem for some ML algorithms. It however is less affected by outliers.

## Note
- with any transformation, fit the data to only training data set and use that to transforom the whole dataset