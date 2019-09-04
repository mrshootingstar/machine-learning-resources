"Machine Learning Resources" 

# Articles
- [The Unreasonable Effectiveness of Recurrent Neural Networks](http://karpathy.github.io/2015/05/21/rnn-effectiveness/)
- [Vanilla LSTM with numpy](https://blog.varunajayasiri.com/numpy_lstm.html)
- http://colah.github.io/
    - [Understanding LSTM Networks](http://colah.github.io/posts/2015-08-Understanding-LSTMs/)
- [An overview of gradient descent optimization algorithms](http://ruder.io/optimizing-gradient-descent/)
- [Vanilla LSTM with numpy](https://blog.varunajayasiri.com/numpy_lstm.html)
- [LSTM](https://machinelearningmastery.com/how-to-develop-lstm-models-for-multi-step-time-series-forecasting-of-household-power-consumption/)

-[MIT Deep Learning Basics: Introduction and Overview with TensorFlow](https://medium.com/tensorflow/mit-deep-learning-basics-introduction-and-overview-with-tensorflow-355bcd26baf0)

- [Neural Machine Translation (seq2seq) Tutorial](https://github.com/tensorflow/nmt#background-on-the-attention-mechanism)

- Attention:
    - [A Beginner's Guide to Attention Mechanisms and Memory Networks](https://skymind.ai/wiki/attention-mechanism-memory-network)
    - [Google AI Blog: Transformer: A Novel Neural Network Architecture for Language Understanding ](https://ai.googleblog.com/2017/08/transformer-novel-neural-network.html)
    - [Jay Alammar: The Illustrated Transformer](https://jalammar.github.io/illustrated-transformer/)
    - [The Annotated Transformer - Python Code](http://nlp.seas.harvard.edu/2018/04/03/attention.html)


- Recommender Systems
    - Collaborative Filtering
    - Content Based
    - Social Recommenders

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
                1. compute the classifier's error e_m
                2. compute the classifier's weight a_m = log( (1-e_m)/e_m )
                3. w_i <- w_i * exp(a_m)
            3. FINAL CLASSIFIER = H(x) = sign( sum(a_m x h_m(x) ) )

        - [A Step by Step Adaboost Example](https://sefiks.com/2018/11/02/a-step-by-step-adaboost-example/):  With numerical examples and python code
    - Gradient Boosting
    - xGBoost
# Books
- [R Graphics Cookbook, 2nd Edition](https://r-graphics.org/chapter-r-basics)

- [R for Data Science](https://r4ds.had.co.nz/)
![foo](http://amzn.to/2aHLAQ1)

- [Deep Learning](https://github.com/janishar/mit-deep-learning-book-pdf)

# Courses
- [Google Machine Learning Crash Course](https://developers.google.com/machine-learning/crash-course/)
- [6.S191: Introduction to Deep Learning](http://introtodeeplearning.com/)
- [Geoffrey Hinton's Neural Networks for Machine Learning](https://www.coursera.org/learn/neural-networks/home/welcome)
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


# Other directories
- [Awesome Deep Learning Awesome](https://github.com/ChristosChristofidis/awesome-deep-learning)
- [Data Science Learning Directory](www.datasciguide.com/contenttype/book/)
