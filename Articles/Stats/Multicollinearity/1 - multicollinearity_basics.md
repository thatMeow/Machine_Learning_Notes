http://blog.minitab.com/blog/adventures-in-statistics-2/what-are-the-effects-of-multicollinearity-and-when-can-i-ignore-them

Multicollinearity refers to predictors that are correlated with other predictors in the model. Unfortunately, the effects of multicollinearity can feel murky and intangible, which makes it unclear whether it’s important to fix.

- How Problematic is Multicollinearity?

Moderate multicollinearity may not be problematic. However, severe multicollinearity is a problem because it can increase the variance of the coefficient estimates and make the estimates very sensitive to minor changes in the model. The result is that the coefficient estimates are unstable and difficult to interpret. Multicollinearity saps the statistical power of the analysis, can cause the coefficients to switch signs, and makes it more difficult to specify the correct model.

- Do I Have to Fix Multicollinearity?

The symptoms sound serious, but the answer is both yes and no—depending on your goals. (Don’t worry, the example we'll go through next makes it more concrete.) In short, multicollinearity:

    - can make choosing the correct predictors to include more difficult.
    - interferes in determining the precise effect of each predictor, but...
    - doesn’t affect the overall fit of the model or produce bad predictions.
    
Depending on your goals, multicollinearity isn’t always a problem. However, because of the difficulty in choosing the correct model when severe multicollinearity is present, it’s always worth exploring.

