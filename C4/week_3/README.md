# Week 3

## Recurrent Neural Networks for Time Series

* References:
    * [Huber Loss Function](https://en.wikipedia.org/wiki/Huber_loss)
    * [Temporal Loops: Intro to Recurrent Neural Networks for Time Series Forecasting in Python](https://towardsdatascience.com/temporal-loops-intro-to-recurrent-neural-networks-for-time-series-forecasting-in-python-b0398963dc1f)
    * [Youtube: Time Series Forecasting Using Recurrent Neural Network and Vector Autoregressive Model: When and How](https://youtu.be/i40Road82No)
    * [LSTM](https://www.coursera.org/lecture/nlp-sequence-models/long-short-term-memory-lstm-KXoay)
* What is `Lambda Layer` in `TensorFlow & Keras` ?
* What is RNN & how to implement it for Time Series ?
    ![RNN](/img/C4/C4_Week_3_RNN.png)
* What is `Recurrent Architecture` ?
    ![Recurrent Architecture](/img/C4/C4_Week_3_Recurrent_Layer.png)
* Shape of the inputs to the RNN    
    ![Recurrent Input](/img/C4/C4_Week_3_Recurrent_Input.png)
* Shape of the sequence input to the RNN
    ![Recurrent Sequence Input](/img/C4/C4_Week_3_Sequence_to_Vector.png)
* RNN with sequence data
* What is `TensorFlow Lambda Layers` ?
* What is `Huber Loss Function` ?
    * The Huber function is a loss function that's less sensitive to outliers.
* RNN and LSTM ?
* If X is the standard notation for the input to an RNN, what are the standard notations for the outputs?
    * Y(hat) and H
* What is a sequence to vector if an RNN has 30 cells numbered 0 to 29
    * The Y(hat) for the last cell
* What does a Lambda layer in a neural network do?
    * Allows you to execute arbitrary code while training
* What does the axis parameter of tf.expand_dims do?
    * Defines the dimension index at which you will expand the shape of the tensor 
* A new loss function was introduced in this module, named after a famous statistician. What is it called?
    * Huber loss
* What’s the primary difference between a simple RNN and an LSTM
    * In addition to the H output, LSTMs have a cell state that runs across all cells
* If you want to clear out all temporary variables that tensorflow might have from previous sessions, what code do you run?
    * tf.keras.backend.clear_session()  
* What happens if you define a neural network with these two layers?
    > `tf.keras.layers.Bidirectional(tf.keras.layers.LSTM(32)),` <br>
    > `tf.keras.layers.Bidirectional(tf.keras.layers.LSTM(32)),` <br>
    > `tf.keras.layers.Dense(1),`
    * Your model will fail because you need return_sequences=True after the first LSTM layer