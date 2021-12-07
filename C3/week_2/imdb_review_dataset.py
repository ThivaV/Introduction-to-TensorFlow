# %%
# !pip install - q tensorflow-datasets
# %%
import io
import numpy as np
from tensorflow.keras.preprocessing import sequence
import tensorflow_datasets as tfds
import tensorflow as tf
print(tf.__version__)

# %%
imdb, info = tfds.load("imdb_reviews", with_info=True, as_supervised=True)
# %%
train_data, test_data = imdb['train'], imdb['test']
# %%
training_sentences = []
training_labels = []

testing_sentences = []
testing_labels = []

# str(s.tonumpy()) is needed in Python3 instead of just s.numpy()
for s, l in train_data:
    training_sentences.append(str(s.numpy()))
    training_labels.append(l.numpy())

for s, l in test_data:
	testing_sentences.append(str(s.numpy()))
	testing_labels.append(l.numpy())

training_labels_final = np.array(training_labels)
testing_labels_final = np.array(testing_labels)
# %%
# Hyperparameter
vocab_size = 10000
embedding_dim = 16
max_length = 120
trunc_type = 'post'
oov_tok = '<OOV>'
# %%
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
# %%
tokenizer = Tokenizer(num_words=vocab_size, oov_token=oov_tok)
tokenizer.fit_on_texts(training_sentences)

word_index = tokenizer.word_index

# Training data
sequences = tokenizer.texts_to_sequences(training_sentences)
padded = pad_sequences(sequences, maxlen=max_length, truncating=trunc_type)

# Testing data
testing_sequences = tokenizer.texts_to_sequences(testing_sentences)
testing_padded = pad_sequences(testing_sequences, maxlen=max_length)

reverse_word_index = dict([(value, key) for (key, value) in word_index.items()])

def decode_review(text):
    return ' '.join([reverse_word_index.get(i, '?') for i in text])

print(decode_review(padded[3]))
print(training_sentences[3])
# %%
# With Flatten layer
model_1 = tf.keras.Sequential([
    tf.keras.layers.Embedding(vocab_size, embedding_dim, input_length=max_length),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(6, activation='relu'),
    tf.keras.layers.Dense(1, activation='sigmoid')
])
model_1.summary()
# %%
# With GlobalAveragePooling1D layer
model_2 = tf.keras.Sequential([
    tf.keras.layers.Embedding(vocab_size, embedding_dim, input_length=max_length),
    tf.keras.layers.GlobalAveragePooling1D(),
    tf.keras.layers.Dense(6, activation='relu'),
    tf.keras.layers.Dense(1, activation='sigmoid')
])
model_2.summary()
# %%
model_1.compile(
    loss='binary_crossentropy',
    optimizer='adam', 
    metrics=['accuracy']
)
model_1.summary()
# %%
model_2.compile(
    loss='binary_crossentropy',
    optimizer='adam',
    metrics=['accuracy']
)
model_2.summary()
# %%
num_epochs = 10

# Trainging the model_1
model_1.fit(
    padded,
    training_labels_final,
    epochs = num_epochs,
    validation_data=(testing_padded, testing_labels_final)
)
# %%
# Trainging the model_2
model_2.fit(
    padded,
    training_labels_final,
    epochs=num_epochs,
    validation_data=(testing_padded, testing_labels_final)
)
# %%
e_1 = model_1.layers[0]
weights_1 = e_1.get_weights()[0]
print(weights_1.shape)  # shape: (vocab_size, embedding_dim)
# %%
e_2 = model_2.layers[0]
weights_2 = e_2.get_weights()[0]
print(weights_2.shape)  # shape: (vocab_size, embedding_dim)
# %%
# Save vectors
import io

out_v = io.open('/vector_meta_data/vecs_1.tsv', 'w', encoding='utf-8')
out_m = io.open('/vector_meta_data/meta_1.tsv', 'w', encoding='utf-8')
for word_num in range(1, vocab_size):
  word = reverse_word_index[word_num]
  embeddings = weights_1[word_num]
  out_m.write(word + "\n")
  out_v.write('\t'.join([str(x) for x in embeddings]) + "\n")
out_v.close()
out_m.close()
# %%
out_v = io.open('/vector_meta_data/vecs_2.tsv', 'w', encoding='utf-8')
out_m = io.open('/vector_meta_data/meta_2.tsv', 'w', encoding='utf-8')
for word_num in range(1, vocab_size):
  word = reverse_word_index[word_num]
  embeddings = weights_2[word_num]
  out_m.write(word + "\n")
  out_v.write('\t'.join([str(x) for x in embeddings]) + "\n")
out_v.close()
out_m.close()
# %%
sentence = "I really think this is amazing. honest."
sequence = tokenizer.texts_to_sequences([sentence])
print(sequence)
# %%
