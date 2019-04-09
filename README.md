# learning-curves

Learning-curves is a Python module that will help you calculating and ploting the learning curve of a model.

Learning curves give an opportunity to diagnose bias and variance in supervised learning models, but also to visualize how training set size influence the performance of the models.

### Installation

```
$ pip install git+https://github.com/H4dr1en/learning-curves.git
```

To create learning curve plots, first import the module with `import learning_curves`.

### Usage

It is as simple as:

```
lc = LearningCurve()
lc.get_lc(estimator, X, Y)
```
Where `estimator` implements `fit(X,Y)` and `predict(X,Y)`.

Output:

![alt text](https://github.com/H4dr1en/learning-curves/blob/dev/images/learning_curve_no_fit.png)

On this example the green curve suggests that adding more data to the training set is likely to improve a bit the model accuracy.
The green curve also shows a saturation near 0.95. We can easily fit a function to this curve:

```
lc.plot_lc(**lc.recorder["data"], predictor="best")
```
Output:

![alt text](https://github.com/H4dr1en/learning-curves/blob/dev/images/learning_curve_simple.png)

Here we used a predefined function, `exp_log`, to fit the green curve. The R2 score is very close to 1, meaning that the fit is optimal. We can therefore use this curve to extrapolate the evolution of the accuracy with the training set size.

This also tells us how many data we should use to train our model to maximize performances and accuracy.

### Add custom functions to fit the learning curve
Such function are called `Predictor`. You can create a `Predictor` like this:
```
predictor = Predictor("myPredictor", lambda x,a,b : a*x + b, [1,0])
```
Here we created a Predictor called "myPredictor" with the function `y(x) = a*x + b`.
Because internally SciPy `optimize.curve_fit` is called, a first guess of the parameters `a` and `b` are required. Here we gave them respective value 1 and 0.
You can then add the `Predictor` to the `LearningCurve` object in two different ways:
- Pass the `Predictor` to the `LearningCurve` constructor:
```
lc = LearningCurve([predictor])
```
- Register the `Predictor` inside the predictors of the `LearningCurve` object:
```
lc.predictors.append(predictor)
```

By default, two `Predictors` are instantiated: `exp_log` and `exp`. Some predictors perform better (R2 score is closer to 1) than others, depending on the dataset, the model and the value to be preditected.

### Find the best Predictor

To find the Predictor that will fit best your learning curve, we provide a `best_predictor` function:
```
lc.best_predictor()
```
Output:
```
('exp_log', 0.999147437907635, <learning_curve.Predictor at 0x7feb9f2a4ac8>)
```
You can either directly plot it with the `plot_lc` function:
```
lc.plot_lc(predictor="best")
```
Ouput:

![alt text](https://github.com/H4dr1en/learning-curves/blob/dev/images/learning_curve_simple.png)

Note that this is the exact same output as calling `get_lc` because internally this function just calls `train` to compute the data points of the learning curve and then call `plot_lr(predictor="best")`.
