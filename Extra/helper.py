

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

chess_df=chess_df[['rated', 'created_at', 'last_move_at', 'turns', 'victory_status',
       'winner', 'increment_code', 'white_rating',
       'black_rating', 'moves', 'opening_eco','opening_name','opening_ply']]
chess_df_subset

chess_df.dtypes
