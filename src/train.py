
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.externals import joblib
import pandas as pd
import math


def main():

    # Data
    print('Loading data...')
    data = pd.read_csv("data/zoo.csv")

    # Grab variables
    X = data.iloc[:, 1:17]  # all rows, all the features and no labels
    y = data.iloc[:, 17]  # all rows, label only

    # Train and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

    # Model
    clf = svm.SVC(gamma='scale')

    # Fit
    print('Fitting model...')
    clf.fit(X_train, y_train)  

    # Evaluate
    print('Evaluating model...')
    score = clf.score(X_test, y_test)
    print('Score: {}'.format(score))

    # Predict
    print('Predicting on test data...')
    predictions = clf.predict(X_test[15:25])
    print('Predicted: \t{}'.format(', '.join([ str(i) for i in predictions ])))
    print('True values: \t{}'.format(', '.join([ str(i) for i in y_test[15:25] ])))

    # Save model
    print('Saving model...')
    # Export the classifier to a file
    joblib.dump(clf, 'models/zoo.joblib')

    print(list(X_test.iloc[0, :]))


if __name__ == '__main__':
    main()
