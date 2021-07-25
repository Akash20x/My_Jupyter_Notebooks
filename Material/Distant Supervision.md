How to create labelled data from unlabelled data in NLP?!

The beauty about text data is that it is available in abundance in unstructured form.

Say, you have a NER problem in hand with little tagged data but large unlabelled data. You can train your model on the small labelled data and then predict labels on the remaining non-annotated text.

Now this untagged data becomes your new labelled data. Yes it contains noise, but out of 20 instances 14 will be correct (assuming your model achieves about 70% accuracy) and if you retrain a new model on this enormous corpus, it's bound to outperform everything else!!

This technique has a fancy name. Its called Distant Supervision.
