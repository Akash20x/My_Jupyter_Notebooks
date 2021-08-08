https://towardsdatascience.com/clustering-algorithm-for-customer-segmentation-e2d79e28cbc3


Clustering can be used in process of Semi-Supervised Learning. There are some problems where in you might not have any idea about the data and relationships whatsoever with missing labels or no labels at all. So clustering first to find natural segmentation of the data and then create labels is recommended. We can then use per-processed data with labels to develop a semi-supervised classification.

Semi-supervised clustering uses a small amount of labeled data to aid and bias the clustering of unlabeled data. k-means algorithm is one of the approach for Semi-supervised clustering, It proposes a max-distance search approach in order to find some optimal initial cluster centers from unlabeled data, especially when labeled data can’t provide enough initial cluster centers. Experimental results demonstrate the advantages of this method over standard random selection and partial random selection, in which some initial cluster centers come from labeled data while the other come from unlabeled data by random selection.
