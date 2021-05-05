# Clustering

### The term clustering describes the process of partitioning a dataset into several subsets, also known as clusters. A key challenge in clustering is unsupervised learning (it means that no target variable, a.k.a. Y variable, is required to train the algorithm).

# K-Means Clustering

### The K-means clustering algorithm is a popular unsupervised clustering algorithm which searches for a pre-determined number of clusters within an unlabeled multidimensional dataset. It is arguably most popular and simple clustering model in Machine Learning.Its idea is incredibly simple and yet powerful: we assume that the input data can be partitioned into k clusters, such that every data point only belongs to exactly one cluster.Every data point belongs to the particular cluster for which the Euclidean distance of that point to the cluster centre is smaller compared to all other clusters.
<br>

### What it means is that each point is closer to its own cluster center than to other cluster centers.
### Note: The cluster center is the arithmetic mean of all the points belonging to the cluster.

# Algorithm for K-means clustering

### K-means imagines each cluster as a solar system.The star that everything (all the observations) in the cluster revolves around is known as the cluster’s centroid.So given a set of centroids and their coordinates (where the X coordinate is fare and the Y coordinate is age), we can easily figure out what cluster each observation belongs to by calculating which centroid it is closest to (in terms of Euclidean distance).

### But how do we decide where the centroids are? That’s where the K-means algorithm comes in. First, we pick a value for $k$, the number of centroids (this is a hyperparameter that we must tune). Let’s say we pick $k=4$. Then we can just pick $4$ points at random and assign them to be our starting centroids. And using our randomly chosen starting centroids, we can create $4$ clusters. Sounds kind of silly right? What’s the point to picking random centroids and creating random clusters?

### Here’s the trick: the means of our clusters become our new centroids. And as long as our starting randomly picked centroids were even slightly different from each other, the new centroids (the cluster means) will be more optimal than our initial clusters; where optimization is based on all the mathematics we just described.

### Once we have our new centroids, we can reassign each observations' cluster based on which of the new centroids it is closest to. Since the centroids became a bit more optimal, our clusters should improve too (in terms of homogeneity within cluster and variance across clusters). And now we can again calculate new centroids from the means of the coordinates of the reassigned clusters. These centroids will have again improved upon their predecessors, and we can keep rinsing and repeating this process until the algorithm has converged.

### Before we start coding it up, let’s refresh ourselves on the steps:
### 1. Randomly assign centroids to start things up.
### 2. Based on those centroids (and an observation’s distance from it), assign each observation to a cluster.
### 3. Calculate the mean coordinates of each cluster; these are our new centroids.
### 4. Reassign clusters based on new centroids.
### 5. Keep repeating steps 3 and 4 until convergence.





