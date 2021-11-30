# Week 1

## Exploring a large dataset

* Dataset: [Kaggle - Dog Vs Cat](https://www.kaggle.com/c/dogs-vs-cats)
* Explore the training history and discovered an interesting phenomenon: Even though the training data set’s accuracy went very high, we saw that after only a few epochs, the validation set levelled out. This is a clear sign that we are overfitting again. Using more data should help with this, but there are some other techniques that you can use with smaller data sets too.
![Model History](/img/C2/C2_Week_1.png)
* What is `Conv2D` and what are it's input parameters ?
`tf.keras.layers.Conv2D(16, (3, 3), activation='relu', input_shape=(150, 150, 3)),` OR `tf.keras.layers.Conv2D(32, (3, 3), activation='relu')`
* What is `MaxPooling2D` and what are it's input parameters ?
`tf.keras.layers.MaxPooling2D(2, 2)` 