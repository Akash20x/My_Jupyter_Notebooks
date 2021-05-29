

plt.scatter(data.comubstion,data.emission)

from sklearn.metrics import r2_score,mean_squared_error

print("R2 score",r2_score(y_test,y_pred))
print("RMSE",np.sqrt(mean_squared_error(y_test,y_pred)))

plt.plot(X_test,L.predict(X_test),label="Modal")
plt.scatter(X_train,y_train,label="data", color="r")
plt.legend()
plt.show()


data['column-name'].fillna('S',inplace=True)
data.column-name.isnull.any() 


sns.distplot(chess_df['turns'])
sns.boxplot(chess_df['turns'])

plt.hist(cereals_df.carbo)
plt.title('Carbohydrates Histogram')
plt.xlabel('Carbohydrates')
plt.ylabel('Frequency')


chess_df=chess_df[['rated', 'created_at', 'last_move_at', 'turns', 'victory_status',
       'winner', 'increment_code', 'white_rating',
       'black_rating', 'moves', 'opening_eco','opening_name','opening_ply']]
chess_df_subset

chess_df.dtypes

#plot a scatterplot of sugars and ratings variables
cereals_df.plot.scatter(x='sugars',y='rating',c='green', figsize=(12,7))
plt.xlabel("Sugars (in grams)")
plt.ylabel("Rating")
plt.title('Sugars Amount vs Rating')


#compute correlation table to analyze variables relationship
corr=cereals_df.corr().round(2)
corr

#create a heatmap to demonstrate the correlation magnitude among the variables
sns.set(font_scale=1.2)
fig, ax = plt.subplots(figsize=(12,8))
sns.heatmap(corr, xticklabels=corr.columns, yticklabels=corr.columns, annot=True, annot_kws={'fontsize':13},
            fmt=".2f", cmap='PiYG', center=0) #annot argument writes the data value into each cell 
                                                #fmt parameter add text to the heatmap cell and formats the cell values
       
      
fig, ax = plt.subplots(nrows=2, ncols=5, figsize=(18,8))
i=0

#adjust the space between main title and subplots
fig.subplots_adjust(top=0.90)

for row in ax:
    for col in row:
        n=cereals_df.columns[i]
        i=i+1
        plt.subplot(2,5,i)
        plt.hist(cereals_df[n], color='mediumturquoise')
        plt.xlabel(n, fontsize=13)
               
plt.suptitle("Cereals Components Distribution", size=15)   
plt.show()

#convert "mfr" variable into a column
manufacturer_df.reset_index('mfr', inplace=True)

#group cereal manufacturer using the mean rating
manufacturer=cereals_df2.groupby(['mfr'])['rating'].mean()
manufacturer_df = pd.DataFrame(manufacturer)

plt.figure(figsize=(10,6))

with plt.style.context('ggplot'):
    sns.countplot(x='mfr',hue='shelf',data=cereals_df2)
plt.title('Grouped by mfr and shelf')

cereals_df2[cereals_df2.mfr=='Quaker Oats']


sns.regplot(x='fat',y='calories',data=cereals)
plt.title('Fat vs Calories')
