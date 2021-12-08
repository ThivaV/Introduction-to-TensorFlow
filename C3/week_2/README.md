# Week 2

## Word Embeddings

* References:

    * [TensorFlow Word Embedding Projector](https://projector.tensorflow.org/)
    * [TensorFlow Dataset Documentations](https://www.tensorflow.org/datasets/catalog/overview)
    * Datasets:
        * [Large Movie Review Dataset](https://ai.stanford.edu/~amaas/data/sentiment/)
        * [TensorFlow Datasets](https://github.com/tensorflow/datasets/tree/master/docs)
            * [TensorFlow datasets docs README.md](https://github.com/tensorflow/datasets/blob/master/docs/README.md)
            * [List of datasets](https://www.tensorflow.org/datasets/catalog/overview)
            * [Colab Yutorial](https://github.com/tensorflow/datasets/tree/master/docs/overview.ipynb)
            * [API Documentation](https://www.tensorflow.org/datasets/api_docs/python/tfds)
            * [Splits](https://github.com/tensorflow/datasets/blob/master/docs/splits.md)
            * [Adding a new dataset](https://github.com/tensorflow/datasets/blob/master/docs/add_dataset.md)
            * [Using Google Cloud Storage and tfds](https://github.com/tensorflow/datasets/blob/master/docs/gcs.md)
        * [TensorFlow Datasets Catalogs](https://github.com/tensorflow/datasets/tree/master/docs/catalog)
        * [IMDB Reviews Datasets](https://github.com/tensorflow/datasets/blob/master/docs/catalog/imdb_reviews.md)

* What is word embedding ?
* `TensorFlow Data Services` or `TFTS` (for short) and that contains many data sets and lots of different categories.

    * `!pip install -q tensorflow-datasets`

    * TensorFlow Data Services 
    ![TensorFlow Data Services](/img/C3/C3_Week_2_TF_DataServices.png)

    * Large Movie Review Dataset (We will find here 50,000 movie reviews which are classified as positive of negative)  
    ![Large Movie Review Dataset](/img/C3/C3_Large_Dataset.png)

* How word embedding works ?
* Difference between `Flatten()` & `GlobalAveragePooling1D()` layers ?
* Explain `Loss Function` ?
    * Simply, **The confidence in the in the `Prediction` is called `loss`**
* What is [SubwordTextEncoder](https://www.tensorflow.org/datasets/api_docs/python/tfds/deprecated/text/SubwordTextEncoder) ?
* What is the name of the TensorFlow library containing common data that you can use to train and test neural networks?
* How many reviews are there in the IMDB dataset and how are they split?
* How are the labels for the IMDB dataset encoded?
* What is the purpose of the embedding dimension?
* When tokenizing a corpus, what does the num_words=n parameter do?
* To use word embeddings in TensorFlow, in a sequential layer, what is the name of the class?
* IMDB Reviews are either positive or negative. What type of loss function should be used in this scenario?
* When using IMDB Sub Words dataset, our results in classification were poor. Why?
    * Sequence becomes much more important when dealing with subwords, but we’re ignoring word positions
* This week We looked at taking our tokenized words and using Embeddings to establish meaning from them in a mathematical way. Words were mapped to vectors in higher dimensional space, and the semantics of the words then learned when those words were labelled with similar meaning. So, for example, when looking at movie reviews, those movies with positive sentiment had the dimensionality of their words ending up ‘pointing’ a particular way, and those with negative sentiment pointing in a different direction. From this, the words in future sentences could have their ‘direction’ established, and from this the sentiment inferred. We then looked at sub word tokenization, and saw that not only do the meanings of the words matter, but also the sequence in which they are found. 