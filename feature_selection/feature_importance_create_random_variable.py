from sklearn.ensemble import RandomForestClassifier

clf = RandomForestClassifier()

df['random'] = np.random.random(size=len(df))
X = df.drop(['Churn?'], axis=1)
y = df['Churn?']

clf_fit = clf.fit(X, y)

importance = clf_fit.feature_importances_
importance
