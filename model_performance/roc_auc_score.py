

# for random forest model

model.fit(X, y)
orc = roc_auc_score(y, model.oob_prediction_)

