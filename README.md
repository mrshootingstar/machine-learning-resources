"Machine Learning Resources" 

# Articles
- [50 years of Data Science](https://courses.csail.mit.edu/18.337/2015/docs/50YearsDataScience.pdf)
- [Ten Simple Rules for Better Figures](https://hal.inria.fr/hal-01063732/document)
- [The Foundations of Algorithmic Bias](http://approximatelycorrect.com/2016/11/07/the-foundations-of-algorithmic-bias/)
- [Rules of Machine Learning: Best Practices for ML Engineering](http://martin.zinkevich.org/rules_of_ml/rules_of_ml.pdf)
- [The Unreasonable Effectiveness of Recurrent Neural Networks](http://karpathy.github.io/2015/05/21/rnn-effectiveness/)
- [Vanilla LSTM with numpy](https://blog.varunajayasiri.com/numpy_lstm.html)
- http://colah.github.io/
    - [Understanding LSTM Networks](http://colah.github.io/posts/2015-08-Understanding-LSTMs/)
- [An overview of gradient descent optimization algorithms](http://ruder.io/optimizing-gradient-descent/)
- [Vanilla LSTM with numpy](https://blog.varunajayasiri.com/numpy_lstm.html)
- [LSTM](https://machinelearningmastery.com/how-to-develop-lstm-models-for-multi-step-time-series-forecasting-of-household-power-consumption/)

- [MIT Deep Learning Basics: Introduction and Overview with TensorFlow](https://medium.com/tensorflow/mit-deep-learning-basics-introduction-and-overview-with-tensorflow-355bcd26baf0)

- Deep Learning in a nutshell [[part 1](https://devblogs.nvidia.com/deep-learning-nutshell-core-concepts/)][[part 2](https://devblogs.nvidia.com/deep-learning-nutshell-history-training/)][[part 3](https://devblogs.nvidia.com/parallelforall/deep-learning-nutshell-sequence-learning/)][[part 4](https://devblogs.nvidia.com/parallelforall/deep-learning-nutshell-reinforcement-learning/)]
- [Neural Machine Translation (seq2seq) Tutorial](https://github.com/tensorflow/nmt#background-on-the-attention-mechanism)
- [Non negative matrix factorization](http://www.billconnelly.net/?p=534)

- [design patters in scikit learn](https://arxiv.org/abs/1309.0238)
- Attention:
    - [A Beginner's Guide to Attention Mechanisms and Memory Networks](https://skymind.ai/wiki/attention-mechanism-memory-network)
    - [Google AI Blog: Transformer: A Novel Neural Network Architecture for Language Understanding ](https://ai.googleblog.com/2017/08/transformer-novel-neural-network.html)
    - [Jay Alammar: The Illustrated Transformer](https://jalammar.github.io/illustrated-transformer/)
    - [The Annotated Transformer - Python Code](http://nlp.seas.harvard.edu/2018/04/03/attention.html)



- Recommender Systems
    - Collaborative Filtering
    - Content Based
    - Social Recommenders
- Bagging (Bootstrap Aggregating)
- Boosting Methods
    - Adaboost AKA Adaptive Boosting:
        - Types:
            - Discrete AdaBoost AKA AdaBoost.M1
            - AdaBoost.SAMME
            - AdaBoost.SAMME.R
            - AdaBoost.R2
        - Weights are adaptive. Incorrect predictions get larger and larger weights, and correct weights get smaller and smaller weights
        - Each classifier has an adaptive weight as well
        - Uses decision stumps, or decision trees of height 1 that are weak learners (accuracy of > 50%)
        - Steps:
            1. Initialize sample weights to be 1/N
            2. Fit m classifier h_m on training data weighted by w_i
                1. compute the classifier's error e_m = sum( w_i * (predicted - actual) ) / sum(w_i)
                2. compute the classifier's weight a_m = log( (1-e_m)/e_m )
                3. w_i <- w_i * exp(a_m * e_m)
            3. FINAL CLASSIFIER = H(x) = sign( sum(a_m x h_m(x) ) )
        - Caveats:
            - weak learner too complex -> overfitting
            - weak learner too weak -> underfitting
            - susceptible to noise
        - can be viewed as a coordinate based gradient descent algorithm
        - [A Step by Step Adaboost Example](https://sefiks.com/2018/11/02/a-step-by-step-adaboost-example/):  With numerical examples and python code
    - Gradient Boosting:
        - Regression and Classification
        - Optimizes a loss function (in contrast to AdaBoost)
        - ensemble of weak models
        - Next Model = Previous Model + learning_rate * some_multiplier * h(x) -- learning rate is to apply **shrinkage**
        - The goal is to make Next Model = Previous Model + h(x) = actual value, hence, h(x)  is fit on the residual of (y-Previous Model)
        - Example Algorithms:
            - Gradient Tree Boosting:
                - Sequential built of trees (unlike random forests)
                - Week Trees built non randomly.
                - Prediction is fast and memory efficient
                - Learning rate parameter (RF don't have it.) Higher LR: more emphasis on correcting the previous tree (more complex) and vice versa
                - `clf = GradientBoostingClassifier(learning_rate=0.01, max_depth=2).fit(X_train, y_train)`
                - To avoid overfitting reduce max depth and learning rate and n_estimators
                - No feature scaling needed
                - Hard to interpret; training computationally expensive; tunning hard; bad for text classification and other problems with high dimensional sparse features
    - Fast scalable GBM:
        - XGBoost
        - LightGBM
        - CatBoost

    - Naive Bayes Classifiers
    - Random Forests
    - Manifold Learning
    - 
# Books
- [R Graphics Cookbook, 2nd Edition](https://r-graphics.org/chapter-r-basics)

- [R for Data Science](https://r4ds.had.co.nz/)
![foo](http://amzn.to/2aHLAQ1)

- [Deep Learning](https://github.com/janishar/mit-deep-learning-book-pdf)

# Courses
- [Google Machine Learning Crash Course](https://developers.google.com/machine-learning/crash-course/)
- [6.S191: Introduction to Deep Learning](http://introtodeeplearning.com/)
- [Geoffrey Hinton's Neural Networks for Machine Learning](https://www.coursera.org/learn/neural-networks/home/welcome)
- [Data Visualization](http://shancarter.github.io/ucb-dataviz-fall-2013/)
# Repos
- [Natural Language Processing Best Practices & Examples ](https://github.com/microsoft/nlp)

- [lucid](https://github.com/tensorflow/lucid)
    - Lucid is a collection of infrastructure and tools for research in neural network interpretability.
- [oxford-cs-deepnlp-2017](https://github.com/oxford-cs-deepnlp-2017/lectures)
# Twitter
- [Gabriel Goh](https://twitter.com/gabeeegoooh)

# Datasets
- [Quick Draw](https://github.com/googlecreativelab/quickdraw-dataset)

# Videos
- [MIT 6.S094: Recurrent Neural Networks for Steering Through Time](https://www.youtube.com/watch?v=nFTQ7kHQWtc)

-  [Arxiv Insights](https://www.youtube.com/channel/UCNIkB2IeJ-6AmZv7bQ1oBYg)


# Websites
- [distill](https://distill.pub/)
- [skymind A.I. Wiki](https://skymind.ai/wiki/)
- [Tensorflow Playground](https://playground.tensorflow.org)
- [Shan Carter's website](http://shancarter.com/)
- [Kevin Quealy's website](http://kpq.github.io/)
- [Pandas Trick by Kevin Markham](https://www.dataschool.io/python-pandas-tips-and-tricks/)

# Other directories
- [Awesome Deep Learning](https://github.com/ChristosChristofidis/awesome-deep-learning)
- [Data Science Learning Directory](www.datasciguide.com/contenttype/book/)

# Checklist
- [How to Use a Machine Learning Checklist to Get Accurate Predictions, Reliably](https://machinelearningmastery.com/machine-learning-checklist/)
- [Machine Learning Project Review Checklist](https://agilescientific.com/blog/2019/4/9/machine-learning-project-review-checklist)