# derivatives
Summary notes on derivatives.

## Geometric Brownian Motion (GBM)

GBM is a model for the evolution of an asset price, $X_t$, where the returns follow a standard brownian motion with the following stochastic differential equation (SDE):

$$\tag1$$

$$
\frac{dX}{X} = \mu dt + \sigma dW \ \ \rightarrow \ \ dX =  \mu X dt + \sigma X dW
$$

And $dW$ is a Wierner process:

$$
dW = \varepsilon \sqrt dt \sim N(0, t)
$$

The $dX/X$ suggests that the price function, $f$, is in the following form:

$$\tag2$$

$$
f = log(X)
$$

Given (1), (2), and [Ito's lemma](https://en.wikipedia.org/wiki/It%C3%B4%27s_lemma):

$$\tag3$$

$$
df = (
\frac{\partial f}{\partial t} + 
\frac{\partial f}{\partial X} \mu X +
\frac{1}{2} \frac{\partial^2 f}{\partial X^2} \sigma^2 X^2) dt + 
\frac{\partial f}{\partial X} \sigma X dW
$$


Substituting the derivatives of $f$ in (3):

$$
df = (0 + 
\frac{1}{X} \mu X +
\frac{1}{2} \frac{-1}{X^2} \sigma^2 X^2) dt + 
\frac{1}{X} \sigma X dW
$$

Which simplifies to:

$$\tag4$$

$$
df = (\mu - \frac{\sigma^2}{2})dt + \sigma dW
$$

Now integerating from time $0$ to time $t$:

$$
f_t - f_0 = (\mu - \frac{\sigma^2}{2})t + \sigma W_t
$$


$$
log(X_t) - log(X_0) = (\mu - \frac{\sigma^2}{2})t + \sigma W_t
$$

$$
log(\frac{X_t}{X_0}) = (\mu - \frac{\sigma^2}{2})t + \sigma W_t
$$

Finally, the solution to the SDE:

$$\tag5$$

$$
X_t = X_0 \\ exp \left( (\mu - \frac{\sigma^2}{2})t + \sigma W_t \right)
$$

Or equivalently:

$$
X_t = X_0 \\ exp \left( (\mu - \frac{\sigma^2}{2})t + \sigma \sqrt t \ \varepsilon \right)
\ \ , \ \ \varepsilon \sim N(0,1)
$$

### Sample code

[GBM in Python](https://github.com/ghasimi/derivatives/blob/main/gbm.py)



## Black-Scholes PDE - Hedging Argument

Create portfolio $\Pi$ from a short position in the option $f$, and a long position in $\delta$ amount of the underlying, $X$, where $\delta = \frac{\partial f}{\partial X}$:

$$\tag1$$

$$\Pi = -f + \frac{\partial f}{\partial X} X$$

Which implies:

$$\tag2$$

$$d\Pi = -df + \frac{\partial f}{\partial X} \ dX$$

From another view, such portfolio has no risk because changes in the long and short position will offset each other. Therefore, the portfolio must yield risk-free return:

$$\tag3$$

$$ 
\frac{d\Pi}{\Pi} = r \ dt \
\Rightarrow \ d\Pi = r \Pi \ dt
$$

In (3), substitute $\Pi$ with (1):
$$\tag4 d\Pi = -rf \ dt + \frac{\partial f}{\partial X} r X \ dt$$

Assume the underlying follows this stochastic differential equation, where $\mu$ is replaced with $r$ accodring to the risk-neutral setting:


$$\tag5$$

$$
dX = r X dt + \sigma X dW
$$

$$Where \ dW = \varepsilon \sqrt{dt} \ \, i.e. \varepsilon \sim N(0,1) \rightarrow dW \sim N(0,t)$$


Given (3), and since $f\rightarrow f(X,t)$, from [Ito's lemma](https://en.wikipedia.org/wiki/It%C3%B4%27s_lemma):


$$\tag6$$

$$df = 
(\frac {\partial f}{\partial t} + 
\frac {\partial f}{\partial X} r X + 
\frac {1}{2} \frac{\partial^2 f}{\partial x^2} \sigma^2 X^2)dt +
\frac {\partial f}{\partial X} \sigma X dW
$$


Now in (2), substitute $d\Pi$ with (4), $dX$ with (5), and $df$ with (6):

$$\tag7$$

$$-rf \ {\color{blue}dt} + 
{\color{red}\frac{\partial f}{\partial X} r X} \ {\color{blue}dt} =
-(\frac {\partial f}{\partial t} + 
\frac {\partial f}{\partial X} r X + 
\frac {1}{2} \frac{\partial^2 f}{\partial x^2} \sigma^2 X^2) \ {\color{blue}dt} -
{\color{maroon}\frac {\partial f}{\partial X} \sigma X dW} +
{\color{red}\frac{\partial f}{\partial X} r X} \ {\color{blue}dt} +
{\color{maroon}\frac {\partial f}{\partial X} \sigma X dW}
$$

Which simplifies to the Black-Scholes PDE:

$$\tag8$$

$$-rf  +
\frac {\partial f}{\partial t} + 
\frac {\partial f}{\partial X} r X + 
\frac {1}{2} \frac{\partial^2 f}{\partial x^2} \sigma^2 X^2 = 0
$$

