# Week 2

## A Technique to Avoid Overfitting

* What is loss ?
* What F1 Measure and how it works ?
* **Image augmentation and data augmentation** is one of the most widely used tools in deep learning to increase your dataset size and make your neural networks perform better.
* **Image Augmentation:** <br>
    Image Augmentation is a very simple, but very powerful tool to help you avoid overfitting your data. The concept is very simple though: If you have limited data, then the chances of you having data to match potential future predictions is also limited, and logically, the less data you have, the less chance you have of getting accurate predictions for data that your model hasn't yet seen. To put it simply, if you are training a model to spot cats, and your model has never seen what a cat looks like when lying down, it might not recognize that in future. 
    <br><br>
    Augmentation simply amends your images `on-the-fly `while training using transforms like rotation. So, it could `simulate` an image of a cat lying down by rotating a `standing` cat by 90 degrees. As such you get a cheap way of extending your dataset beyond what you have already.
    <br><br>
    To learn more about Augmentation, and the available transforms, check out [https://github.com/keras-team/keras-preprocessing](https://github.com/keras-team/keras-preprocessing) -- and note that it's referred to as preprocessing for a very powerful reason: that it doesn't require you to edit your raw images, nor does it amend them for you on-disk. It does it in-memory as it's performing the training, allowing you to experiment without impacting your dataset. [keras.io](https://keras.io/)  
* Can see more about the different APIs at the **Keras site here on Image data preprocessing**: [https://keras.io/preprocessing/image/](https://keras.io/preprocessing/image/)
* TensorFlow gives you with `Image Augmentation`. With it, you can effectively simulate a larger dataset from a smaller one with tools to move images around the frame, skew them, rotate them, and more. It can be an effective tool in fixing overfitting. 