
clf = DecisionTreeClassifier(random_state=0, max_depth=2)
X = train.drop(['income'], axis=1)
y = train.income

scores = cross_val_score(clf, X, y, cv=10, scoring = 'accuracy')
avg_score = scores.mean()
avg_score
