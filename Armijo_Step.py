#Given a function f, with evaluation fval(x) and gradient grad(x), we have:

def armijo(x, alpha = 1/2):
    t = 1
    d = - grad(x)
    while fval(x+t*d) >= fval(x) - alpha*t*np.linalg.norm(d)**2:
        t = t/2
    return t