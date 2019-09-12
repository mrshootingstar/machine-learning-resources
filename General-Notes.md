- Explaining the contribution of individual features to the output of tree ensemble models: SHapley Additive exPlanations, or SHAP values
- Coordinate descent is just like gradient descent, exceptthat you can’t move along the gradient, you have to choose just one coordinateat a time to move along.
- Conditional Random Fields (2001): a frame-work  for  building  probabilistic  models  to  seg-ment and label sequence data.
- p-hacking AKA data dredging: Performing many statistical tests on the data and only paying attention to those that come back with significatnt results.
    - at a confidence level of 0.05, we expect to find one positive result out of 20 tests.
    - remedies:
        - Bonferroni Correction: You are running 3 tests, multiply alpha by 1/3
        - Hold-out Tests: heavily used in machine learning (cross validation)
        - Investigation Pre-registration: Used in academic fields

- Hyperparameter tuning based on a sample of the data is a bad [There are people who disagree] idea because hyper parameters are depended on the size of the data. Once the hyper parameters are optimized, train a new model using the whole dataset you have to use for unforeseen data points. Some poeple say you can use a algorithm that supports multifidelity evaluations to find an estimate of your optimized hyperparameter from a subset of the data.

- Multiple vs Multivariate Regression: Multiple has more than one feature - Multivariate predicts more than one target variable
- if your histograms are tail-heavy it may make it hard for some ML algorithms. You may need to transfer the data (e.g., by computing their logarithm).
- Sample feature engineering:
  1. number of bedrooms not useful. number of bedrooms/total number of rooms is useful

- Train/Validation/Test
    - Train: Used for training the models with various hyper parameters
    - Validation: select the model that performs best on the validation set
    - ** After selecting the model, train your model again on (train+validation) sets
    - Alternatively, you can use cross validation
    - Train model with multiple hyperparameters on the training set and select the one that performs the best on the validation set and then train the best model on the full training set to get the `final model`. Then you use the final model on the test set to estimate the `generalization error`.
    - **possible problems**: validation set too small => model evaluation will be imprecise. Validation set too large => training set is too small and you will end up picking the fastest sprinter to run a marathon. **solution**: Use cross validation: Each model is evaluated once on each validation set.
- attribute vs feature: attribute is a datatype, feature is an attribute and its value
- anomaly detection vs novelty detection (finding new instances that look different from all instances in the training set)
- Association rule lerning: which items are bought together
- semisupervised learning: Deep Belief Networks and Restricted Boltzmann Machines
- Batch vs Online learning vs Out-of-core learning:  Batch (unable to learn incrementally, all training data needed) Online (usefull if you receive data incrementally in a stream- you need to define how quickly you respond to new data -- learning rate) Out-of-core(huge data sets)
- Instance based methods are usually based on a similarity measure
- Bad features / bad data/ non-representative data / irrelevant features => nemesis
- feature selection vs feature extraction (select among existing ones/ create new features from existing ones)
- Solve overfitting: regularization, simplify the model, gather more data, remove noise and outliers
- Solve underfitting: better model, better features, reduce regularization
- Generalization error is estimated by evaluating your model on the test set
- How to detect **data mismatch**? You train your camera app to detect flowers on flower images found on the web that are not representative of the flower pictures users will take using the app. Andrew Ng suggest having yet another data split called `train-dev` set that is used only to see if model has overfitted the training set. If the performance on this set is good, we move on to evaluation on the validation set.
- What happens if you use the test set to select hyperparameters? You are twitching your algorithm to work on the same test set and you end up overfitting your model.

- Checklist for ML projects
- for ordered categorical data you can use OrdinalEncoder `from sklearn.preprocessing import OrdinalEncoder`
- in general for categorical data use onehot encoder `from sklearn.preprocessing import OneHotEncoder`
- If your categorical data has a lot of labels, you need to downsize it or replace it with a more meaningful feature (ocean_proximity -> distance form ocean)