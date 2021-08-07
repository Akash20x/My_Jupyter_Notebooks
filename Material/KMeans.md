
https://www.linkedin.com/pulse/k-mean-clustering-use-cases-security-domain-muskaan-bakshi

Silhouette score is a metric to compare the effectiveness of a clustering technique. It is also used to calculate the optimal number of clusters for distance based clustering techniques such as K Means and is better than the alternatives such as the elbow method.

Silhouette score is calculated by comparing the average intra cluster distance with the average inter cluster distance. The idea behind is that the under optimal scenarios, all clusters should be as distinct and separable from each other as possible. This gives us a score between -1 and 1 where 1 denotes that all clusters are perfect whereas -1 denotes that all data points are clustered in the wrong cluster.

https://towardsdatascience.com/selecting-optimal-k-for-k-means-clustering-c7579fd2e926

To process the learning data, the K-means algorithm in data mining starts with a first group of randomly selected centroids, which are used as the beginning points for every cluster, and then performs iterative (repetitive) calculations to optimize the positions of the centroids. It halts creating and optimizing clusters when either The centroids have stabilized — there is no change in their values because the clustering has been successful or the defined number of iterations has been achieved.

The clusters formed using K-means are evaluated using metric called Inertia. Intuitively, inertia tells how far away the points within a cluster are. Therefore, a small of inertia is aimed for. The range of inertia’s value starts from zero and goes up.


Silhouette score is used to evaluate the quality of clusters created using clustering algorithms such as K-Means in terms of how well samples are clustered with other samples that are similar to each other. The Silhouette score is calculated for each sample of different clusters. To calculate the Silhouette score for each observation, the mean intra-cluster distance and mean nearest-cluster distance need to be found out for each observations belonging to all the clusters.

Image segmentation is the classification of an image into different groups. There are different methods and one of the most popular methods is K-Means clustering algorithm. K-Means clustering algorithm is an unsupervised algorithm and it is used to segment the interest area from the background. It clusters, or partitions the given data into K-clusters or parts based on the K-centroids.
