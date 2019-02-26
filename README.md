# Zoo

Example to develop a quick model using Scikit-learn and serve that model using a Flask API.

```
$ python src/train
Loading data...
Fitting model...
Evaluating model...
Score: 0.9615384615384616
Predicting on test data...
Predicted: 	6, 1, 6, 2, 4, 2, 7, 1, 2, 1
True values: 	6, 1, 6, 2, 4, 2, 3, 1, 2, 1
Saving model...
[0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 4, 0, 0, 0]
```

Start the API:
```
$ python src/app.py
```

Test using Python's requests library:
```
$ python src/request.py
{ 
    "Prediction": 5
}
```

Test using curl:
```
(env) $ sh src/run.sh
{
  "Prediction": 5
}
```

## Deployment

### Virtual Environment using Bash

1. Creation of a virtual environments done by executing the command venv
2. Command to activate virtual environment
3. Install dependencies
4. List the libraries installed on your environment
5. Do your work!
6. When you are done, the command to deactivate virtual environment
```
$ python3 -m venv env/
$ source env/bin/activate
(env) $ pip install -r requirements.txt
(env) $ pip freeze
(env) $ ...
(env) $ deactivate
```

## Resources

* https://github.com/amirziai/sklearnflask/
* [Learning Scikit-Learn (AI Adventures)](https://www.youtube.com/watch?v=rvVkVsG49uU&list=PLIivdWyY5sqJxnwJhe3etaK7utrBiPBQ2&index=26&t=0s) & [Serving Scikit-learn Models at Scale](https://www.youtube.com/watch?v=MaKLWy5zXe8&index=26&list=PLIivdWyY5sqJxnwJhe3etaK7utrBiPBQ2)