- X = WH (sometimes approximatly)
- NP-hard problem
- we find a local minima
- objective function is minimization of the norm of ||X - WH||^2 where W, H >=0
- Method:
    - Multiplicative Update
    - Hierarchical Alternating Least Squares
        - faster than multiplicative update
        - updates 

- Sensitive to initial values

```python
def nmf(X, com=3):
    w, h = X.shape
    print(w,h)
    W = np.random.rand(w,com)
    H = np.random.rand(com, h)
    cost = norm(X - W.dot(H))
    max_step = 1000
    step = 0
    tol = 1e-5
    cost_path = []
    while cost > tol and step < max_step:        
        step += 1
        num1 = W.T.dot(X)
        denum1 = W.T.dot(W.dot(H))
        H = np.multiply(H, np.divide(num1, denum1))
        
        num2 = X.dot(H.T)
        denum2 = W.dot(H.dot(H.T))
        W = np.multiply(W, np.divide(num2, denum2))
        cost = norm(X - W.dot(H))
        cost_path.append(cost)
    return W, H, cost_path
```