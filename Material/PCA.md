
Principal Component Analysis (PCA) is by far the most popular dimensionality reduction algorithm. First it identifies the hyperplane that lies closest to the data, and then it projects the data onto it. By definition, the top PCs capture the dominant factors of heterogeneity in the data set. Thus, we can perform dimensionality reduction by restricting downstream analyses to the top PCs. This strategy is simple, highly effective and widely used throughout the data sciences

How many of the top PCs should we retain for downstream analyses? The choice of the number of PCs d is a decision that is analogous to the choice of the number of features to use. Using more PCs will retain more data. Most practitioners will simply set d to a “reasonable” but arbitrary value, typically ranging from 10 to 50. This is often satisfactory as the later PCs explain so little variance that their inclusion or omission has no major effect.

Principal Component Analysis (PCA) is an unsupervised technique used in machine learning to reduce the dimensionality of data. It does so by compressing the feature space by identifying a subspace that captures most of the information in the complete feature matrix. 

In simple words, It projects the original feature space into lower dimensionality.

If you are dealing with a very large feature matrix, you can use PCA before training models to compress the feature space
