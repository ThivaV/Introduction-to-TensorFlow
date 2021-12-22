# Week 4

## Real-World time series data (Convolutions with LSTM)

* References:
    * [Sunspots dataset](https://www.kaggle.com/robervalt/sunspots)
    * [MachineLearningMastery.com](https://machinelearningmastery.com/)
    * [jbrownlee datasets](https://github.com/jbrownlee/Datasets)
    * [TensorFlow: Advanced Techniques Specialization](https://bit.ly/39iAsZQ)
    * [TensorFlow: Data and Deployment Specialization](https://bit.ly/3ojuT1o)
* [Convolutional Neural Networks - Andrews course within the Deep Learning Specialization](https://www.coursera.org/learn/convolutional-neural-networks)
* [CNN with TensorFlow](https://www.coursera.org/learn/convolutional-neural-networks-tensorflow)
* What is `Bi-directional LSTMs` ?
* [Large Scale Machine Learning | Mini Batch Gradient Descent — [ Andrew Ng ]](https://www.youtube.com/watch?v=l4lSUAcvHFs)
* [Batch Vs Mini-Batch Gradient Descent](https://www.youtube.com/watch?v=4qJaSmvhxi8)
* What is `Stochastic Gradient Descent` ?
* How do you add a 1 dimensional convolution to your model for predicting time series data?
    * Use a Conv1D layer type
* What’s the input shape for a univariate time series to a Conv1D?
    * [None, 1]
* You used a sunspots dataset that was stored in CSV. What’s the name of the Python library used to read CSVs?
    * CSV
* If your CSV file has a header that you don’t want to read into your dataset, what do you execute before iterating through the file using a ‘reader’ object?
    * next(reader)
* When you read a row from a reader and want to cast column 2 to another data type, for example, a float, what’s the correct syntax?
    * float(row[2])
* What was the sunspot seasonality?
    * 11 or 22 years depending on who you ask
* After studying this course, what neural network type do you think is best for predicting time series like our sunspots dataset?
    * A combination of DNN, RNN, LSTM and Convolutions
* Why is MAE a good analytic for measuring accuracy of predictions for time series?
    * It doesn’t heavily punish larger errors like square errors do
* What is the `Input & Output` shapes for DNN, RNN, CNN, LSTM and others ?
* Work wtth `Multivariate Time Series` data ?