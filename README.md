# derivatives
Summary notes on derivatives.


## Black-Scholes PDE - Hedging Argument

Create portfolio $\pi$ from a short position in one call option $f$, and a long position in $\delta$ units of the underlying, $X$, where $\delta = \frac{\partial f}{\partial X}$:

$$\tag1
\pi = -f + \frac{\partial f}{\partial X} X
$$

Which implies:

$$\tag2
d\pi = -df + \frac{\partial f}{\partial X} \ dX
$$

From another view, such portfolio has no risk because changes in the long and short position will offset each other. Therefore, the portfolio must yield risk-free return:

$$\tag3
\frac{d\pi}{\pi} = r \ dt \ \ \
\Rightarrow \ \ \ d\pi = r \pi \ dt
$$

Assume the underlying follows this stochastic differential equation, where $\mu$ is replaced with $r$ accodring to the risk-neutral setting:

$$\tag4
dX = r X dt + \sigma X dW
$$

$$Where \ dW = \varepsilon \sqrt{dt} \ \, i.e. \varepsilon \sim N(0,1) \rightarrow dW \sim N(0,t)$$


Given (3), and since $f\rightarrow f(X,t)$, from [Ito's lemma](https://en.wikipedia.org/wiki/It%C3%B4%27s_lemma):


$$\tag5
$$

$$df = 
(\frac {\partial f}{\partial t} + 
\frac {\partial f}{\partial X} r X + 
\frac {1}{2} \frac{\partial^2 f}{\partial x^2} \sigma^2 X^2)dt +
\frac {\partial f}{\partial X} \sigma X dW
$$


Now in (2), substitute $d\pi$ with (3), $dX$ with (4), and $df$ with (5):

$$\tag6
$$


