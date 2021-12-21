# Week 2

## Deep Neural Networks for Time Series

* References:

    * [How to identify the Learning Rate](/C4/week_2/C4_W2_Lab_3_deep_NN.ipynb)
* Why Sequence data tends to work better with RNNs ?
* What is `Sequence bias` ?
    * `Sequence bias` is when the order of things can impact the selection of things. For example, if I were to ask you your favorite TV show, and listed "Game of Thrones", "Killing Eve", "Travellers" and "Doctor Who" in that order, you're probably more likely to select 'Game of Thrones' as you are familiar with it, and it's the first thing you see. Even if it is equal to the other TV shows. So, when training data in a dataset, we don't want the sequence to impact the training in a similar way, so it's good to shuffle them up. 
* What is `Windowed Data` in `Time Series` ?
* What is `Mean Absolute Error (MAE)`, `Root Mean Squared Error (RMSE)`, `Mean Squared Error (MSE)` ?
* What is `Learning Rate (lr)` ?
    ![Learning Rate](/img/C4/C4_Week_2_learning_rate.png)
* What is `LearningRateSchedular` ?
* What is a windowed dataset?
    * A fixed-size subset of a time series 
* What does ‘drop_remainder=true’ do?
    * It ensures that all rows in the data window are the same length by cropping data
* What’s the correct line of code to split an n column window into n-1 columns for features and 1 column for a label
    * dataset = dataset.map(lambda window: (window[:-1], window[-1:]))
* What does MSE stand for?
    * Mean Squared error
* What does MAE stand for?
    * Mean Absolute Error
* If time values are in time[], series values are in series[] and we want to split the series into training and validation at time 1000, what is the correct code?
    * > `time_train = time[:split_time]` <br>
    `x_train = series[:split_time]` <br>
    `time_valid = time[split_time:]` <br>
    `x_valid = series[split_time:]`
* If you want to inspect the learned parameters in a layer after training, what’s a good technique to use?
    * Assign a variable to the layer and add it to the model using that variable. Inspect its properties after training
* How do you set the learning rate of the SGD optimizer?
    * Use the lr property
* If you want to amend the learning rate of the optimizer on the fly, after each epoch, what do you do?
    * Use a LearningRateScheduler object in the callbacks namespace and assign that to the callback 