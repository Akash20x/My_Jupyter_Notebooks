Topic modelling is the idea of retrieving the various themes from a text to easily classify or segregate them. The algorithms to be used are:

- LDA: Latent Dirichlet Allocation
- NMF: Non Negative Matrix Factorization

Both of these are unsupervised approaches used to get a fixed set of topics from a text. In both approaches, the semantic meaning of each topic has to be assigned manually.

LDA works by randomly assigning each word in each document to a topic randomly and then updating them over multiple iterations based on how likely is that a document belongs to a topic and how likely is a that a particular word belongs to a topic. LDA can help us analyze the what all topics and in all what proportions is a document composed of and all also the list of words and a set of scores that measures the relevancy of a word belonging to a topic.

NMF is a statistical matrix factorization approach that is considered better for non negative matrices than SVD. NMF uses the TF-IDF matrix where each column is a word and each row represents a document with its TF-IDF values. Decomposing this matrix results in a set of matrix that gives the topic composition of each document as well as list of words in each topic similar to LDA.
