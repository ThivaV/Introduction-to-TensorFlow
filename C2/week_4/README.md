# Week 4

## Multiclass Classifications

* References:

    * https://github.com/https-deeplearning-ai/tensorflow-1-public/blob/main/C2/W4/ungraded_lab/C2_W4_Lab_1_multi_class_classifier.ipynb
    * [sign-language-mnist](https://www.kaggle.com/datamunge/sign-language-mnist)
    * [dogs-vs-cats](https://www.kaggle.com/c/dogs-vs-cats/code)

* What is DNN ?
* [Introducing the Rock-Paper-Scissors dataset](http://www.laurencemoroney.com/rock-paper-scissors-dataset/)
* Rock / Paper or Scissors [training set](https://storage.googleapis.com/laurencemoroney-blog.appspot.com/rps.zip), [testing set](https://storage.googleapis.com/laurencemoroney-blog.appspot.com/rps-test-set.zip) and some more images which We can use it for [predictions](https://storage.googleapis.com/laurencemoroney-blog.appspot.com/rps-validation.zip). All these images are 300×300 pixels in 24-bit color.
    ![Rock_Paper_Scissors_Dataset](/img/C2/C2_Week_4_Rock_Paper_Scissors_Dataset.png)
* Changes to do from `binary` to `multiclass` classifications
    
    * Changing the class mode for `multiclass classification`

    **FROM**

    ![Binary Classification](/img/C2/C2_Week_4_Binary.png)

    **TO**

    ![Multiclass Classification](/img/C2/C2_Week_4_Categorical.png)

    * Changing output layers for `multiclass classification`
    
    **FROM**
    
    ![Sigmoid](/img/C2/C2_Week_4_Sigmoid.png)

    **TO**

    ![Sigmoid](/img/C2/C2_Week_4_Softmax.png)

    * Changing compile settings for `multiclass classification`
    
    **FROM**

    ![Binary_Crossentropy](/img/C2/C2_Week_4_Binary_Crossentropy.png)
    
    **TO**

    ![Sigmoid](/img/C2/C2_Week_4_Categorical_Crossentropy.png)

* We've come a long way! From first     principles in understanding how ML works, to using a DNN to do basic computer vision, and then beyond into Convolutions.

    With Convolutions, We then saw how to extract features from an image, and We saw the tools in TensorFlow and Keras to build with Convolutions and Pooling as well as handling complex, multi-sized images.

    Through this We saw how overfitting can have an impact on your classifiers, and explored some strategies to avoid it, including Image Augmentation, Dropouts, Transfer Learning and more. To wrap things up, this week We've looked at the considerations in our code that you need for moving towards multi-class classification!.

* `Augmentation`, `Dropouts`, `Regularization` and `Transfer Learning`, and coding considerations between `binary` or `multi-class classification`.