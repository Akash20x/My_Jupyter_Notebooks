Class imbalance is predominant in medical data. In this situation, the predictive model developed using conventional machine learning algorithms could be biased and inaccurate.

This happens because Machine Learning Algorithms don’t take into account the class distribution / proportion or balance of classes.
In this implementation 3 approaches used to handle this problem. 

- Over Sampling Technique : Smote
- Over Sampling and Under Sampling Techniques : Smote+Tomek Links
- Under Sampling Technique : Nearmiss-2

We can see that the results after smote, smote+tomek links and nearmiss are more accurate.
