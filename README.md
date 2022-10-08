# derivatives
Summary notes on derivatives.


## Black-Scholes PDE - Hedging Argument

Create portfolio $\pi$ of a short position in one call option $f$, and a long position in $\delta$ units of the underlying, $X$, where $\delta = \frac{\partial f}{\partial X}$.

$$\tag1
\pi = -f + \frac{\partial f}{\partial X} X 
$$

Assume the underlying follows this stochastic differential equation:

$$\tag2
dX = \mu X dt + \sigma X dW
$$

Where $dW = \varepsilon \sqrt{dt} \ \, i.e. \varepsilon \sim N(0,1) \rightarrow dW \sim N(0,t) $



In a risk-netrial setting we replace $\mu\$ with $r$, and since $f$ is a function of time and the underlying, i.e. $f\rightarrow f(X,t)$, from [Ito's lemma](https://en.wikipedia.org/wiki/It%C3%B4%27s_lemma):


$$\tag3$$

$$df = 
(\frac {\partial f}{\partial t} + 
\frac {\partial f}{\partial X} r X + 
\frac {1}{2} \frac{\partial^2 f}{\partial x^2} \sigma^2 X^2)dt +
\frac {\partial f}{\partial X} \sigma X dW
$$






