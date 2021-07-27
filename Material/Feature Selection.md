
Feature selection

The process of selecting the most important features in a given dataset

Why can't we simply give all the features to our ML algorithm?

There are mainly 3⃣ reasons:
- Curse of Dimensionality
- Occam's Razor
- GIGO (Garbage In Garbage Out)

💡Curse of Dimensionality

Having no. of columns (features) more than no. of rows is termed as high-dimensional data. Among those, some remain irrelevant, unimportant, redundant features & don't help our model in any way

 Instead this makes the model bulky, time-consuming

💡Occam's Razor

While interpreting the prediction made by our model, we want it to be simple and explainable

If we have many redundant features (extension of other features) - understanding which features are actually affecting the prediction of our model becomes difficult

💡Garbage In Garbage out

When we give noisy, non-informative features to our model, it will affect the performance of the model.

🦄Poor quality input will produce poor quality output🦄


A large no. of features make the model complex, bulky, & harder to implement in production
