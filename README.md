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



    <!--Load the AJAX API-->
    <script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>
    <script type="text/javascript">

      // Load the Visualization API and the corechart package.
      google.charts.load('current', {'packages':['corechart']});

      // Set a callback to run when the Google Visualization API is loaded.
      google.charts.setOnLoadCallback(drawChart);

      // Callback that creates and populates a data table,
      // instantiates the pie chart, passes in the data and
      // draws it.
      function drawChart() {

        // Create the data table.
        var data = new google.visualization.DataTable();
        data.addColumn('string', 'Topping');
        data.addColumn('number', 'Slices');
        data.addRows([
          ['Mushrooms', 3],
          ['Onions', 1],
          ['Olives', 1],
          ['Zucchini', 1],
          ['Pepperoni', 2]
        ]);

        // Set chart options
        var options = {'title':'How Much Pizza I Ate Last Night',
                       'width':400,
                       'height':300};

        // Instantiate and draw our chart, passing in some options.
        var chart = new google.visualization.PieChart(document.getElementById('chart_div'));
        chart.draw(data, options);
      }
    </script>

    <!--Div that will hold the pie chart-->
    <div id="chart_div"></div>
