NLP-chunks is a small project built for fun. I mainly used it to try out different machine learning ideas in the field of Natural Language Processing. Some of the ideas include: word embeddings of different dimensions, one-hot encodings, neural network depth, one-directional and bi-directional Long Short Term Memory (LSTM) networks. 

The project is built of two parts:

- **Name Entity Recognition (NER)**. Here the goal is - in a given text, attach a label to each word, where labels belong to: Person, Organisation, Location, Miscellaneous and Other.
- **Chunking of phrases**. Similar to NER, to each word in a given text snippet, we need to attach one of the labels: B - beginning of a chunk, I - continuation of a chunk, O - other (not part of any chunk).

## Data and Evaluation

I only had a small amount of data to work with, thanks to the team at <a href="https://util.co/" target="_blank">Util.co</a>, so it was important to properly evaluate the model. This was done with repeated K-fold cross-validation, and I looked at metrics such as precision, recall, F1-score and support. After running all the experiments, it turned out that the best performance was reached by a bi-directional two-layer LSTM network. The following figure shows the performance of the final model for the Name Entity Recognition part.

<img class="intext-img" src="../static/NER_performance.png">

The approach taken in the Prhases Chunking part was quite similar, and its performance is summarised in the following figure.

<img class="intext-img" src="../static/Chunking_performance.png">

## Examples

At the moment the both models for NER and Chunking work with running the appropriate Python script in the terminal. Here are a few examples of their work on real text.

<img class="intext-img" src="../static/NER_example.png"/>

<img class="intext-img" src="../static/Chunking_example.png"/>


## Way forward

The main challenge in the work done here was optimising the performance of the model using small amount of data. Since we've learned which things work best in this case, the next step would be to train a model on a bigger dataset, and possibly build a small web app to use the tools on user's inputs.