# Clustering

### The term clustering describes the process of partitioning a dataset into several subsets, also known as clusters. A key challenge in clustering is unsupervised learning (it means that no target variable, a.k.a. Y variable, is required to train the algorithm).

# K-Means Clustering

### The K-means clustering algorithm is a popular unsupervised clustering algorithm which searches for a pre-determined number of clusters within an unlabeled multidimensional dataset. It is arguably most popular and simple clustering model in Machine Learning.Its idea is incredibly simple and yet powerful: we assume that the input data can be partitioned into k clusters, such that every data point only belongs to exactly one cluster.Every data point belongs to the particular cluster for which the Euclidean distance of that point to the cluster centre is smaller compared to all other clusters.
<br>

### What it means is that each point is closer to its own cluster center than to other cluster centers.
<br>

### Note: The cluster center is the arithmetic mean of all the points belonging to the cluster.
<br>

### Let us dive into little bit of mathematics before we start coding from scratch (you can totally skip this section if you are interested only in the coding part).



