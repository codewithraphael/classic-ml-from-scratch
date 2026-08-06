# Model Structure

Linear regression is a relatively simple method that is extremely widely-used. It is also a great stepping stone for more sophisticated methods, making it a natural algorithm to study first.

In linear regression, the target variable is assumed to follow a linear function of one or more predictor variables, plus some random error. Specifically, we assume the model for the observation in our sample is of the
form

Here the intercept term, through are the coefficients on our feature variables, and is an error term that represents the difference between the true value and the linear function of the predictors. Note that the terms
with an in the subscript differ between observations while the terms without (namely the ) do not.

The math behind linear regression often becomes easier when we use vectors to represent our predictors and
coefficients.