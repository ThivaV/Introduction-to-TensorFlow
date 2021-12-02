# Week 3

## Transfer Learning

As We've seen, We can be limited by the data We have on hand. Not everybody has access to massive datasets or the compute power that's needed to train them effectively. <br>
`Transfer Learning` can help solve this -- where People with models trained on large datasets train them, so that We can either use them directly, or, We can use the features that they have learned and apply them to our scenario and that is called `Transfer Learning`.

* Check notebook `C2_W3_Lab_1_transfer_learning.ipynb`: [https://arxiv.org/abs/1512.00567](https://arxiv.org/abs/1512.00567) and [https://image-net.org/](https://image-net.org/)
* On how to freeze/lock layers, explore the documentation, which includes an example using MobileNet architecture: [https://www.tensorflow.org/tutorials/images/transfer_learning](https://www.tensorflow.org/tutorials/images/transfer_learning)
* What is `Inception` in `Transfer Learning` ?
* How to stop the already learned convolutions from retraining into our model using `freeze (or lock)` ?
* What is `dropouts` ? <br>
    Another useful tool to explore at this point is the Dropout. 

    The idea behind Dropouts is that they remove a random number of neurons in your neural network. This works very well for two reasons: The first is that neighboring neurons often end up with similar weights, which can lead to overfitting, so dropping some out at random can remove this. The second is that often a neuron can over-weigh the input from a neuron in the previous layer, and can over specialize as a result. Thus, dropping out can break the neural network out of this potential bad habit! 

    Check out Andrew's terrific video explaining dropouts here: [https://www.youtube.com/watch?v=ARq74QuavAo](https://www.youtube.com/watch?v=ARq74QuavAo)
* `Dropout` is another tool to overcome `overfitting` 
    <br>
    ![Overfitting](/img/C2/C2_Week_3.png "Overfitting")
    <br>
    <b>After `Dropout` added</b>
    <br>
    ![Dropout](/img/C2/C2_Week_3_with_dropouts.png "Dropout")
* What We learned so far ?
    
    We saw `Transfer Learning`, and how you can take an existing model, freeze many of its layers to prevent them being retrained, and effectively `remember` the convolutions it was trained on to fit images. 

    We then added our own DNN underneath this so that you could retrain on our images using the convolutions from the other model. 

    We learned about regularization using dropouts to make our network more efficient in preventing `over-specialization` and this `overfitting`.
* How do you change the number of classes the model can classify when using transfer learning? (i.e. the original model handled 1000 classes, but yours handles just 2) ?
    
    When We add our DNN at the bottom of the network, We specify out output layer with the number of classes We want.
* What would the symptom of a Dropout rate being set too high?
    
    The network would lose specialization to the effect that it would be inefficient or ineffective at learning, driving accuracy down.
* Which is the correct line of code for adding Dropout of 20% of neurons using TensorFlow ?
    
    `tf.keras.layers.Dropout(0.2),`