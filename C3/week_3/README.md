# Week 3

## Sequence Models

* References:

    * [RNN - Recurrent Neural Network](https://www.coursera.org/lecture/nlp-sequence-models/deep-rnns-ehs0S)
    * [LSTM - Long Short Term Memory](https://www.coursera.org/lecture/nlp-sequence-models/long-short-term-memory-lstm-KXoay)
    * [GloVe - Global Vectors](https://nlp.stanford.edu/projects/glove/)
    * Datasets:
        * [Sentiment140 dataset with 1.6 million tweets](https://www.kaggle.com/kazanova/sentiment140) 

* What is RNN ?
* Types of RNNs ?
* What is LSTM ?
* What is GRU ?
* LSTM `cell state` vs `hidden state` ?
* Why does sequence make a large difference when determining semantics of language?
    * Because the order in which words appear dictate their impact on the meaning of the sentence
* How do Recurrent Neural Networks help you understand the impact of sequence on meaning?
    * They carry meaning from one cell to the next
* How does an LSTM help understand meaning when words that qualify each other aren’t necessarily beside each other in a sentence?
    * Values from earlier words can be carried to later ones via a cell state
* What keras layer type allows LSTMs to look forward and backward in a sentence?
    * Bidirectional
* What’s the output shape of a bidirectional LSTM layer with 64 units?
    * (None, 128)
* When stacking LSTMs, how do you instruct an LSTM to feed the next one in the sequence?
    * Ensure that return_sequences is set to True only on units that feed to another LSTM
* If a sentence has 120 tokens in it, and a Conv1D with 128 filters with a Kernal size of 5 is passed over it, what’s the output shape?
    * (None, 116, 128)
* What’s the best way to avoid overfitting in NLP datasets?
    * 
* What is `GloVe` (Global Vectors) ?