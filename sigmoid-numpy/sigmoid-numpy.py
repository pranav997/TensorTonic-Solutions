import numpy as np

def sigmoid(x: list | float) -> np.ndarray | float:
    """
    Returns the sigmoid value for a scalar or each element of a list.
    """
    # Write code here
    x=np.array(x)
    if np.size(x)==1:
        sigm=1/(1+np.exp(-x))
    elif np.size(x)>1:
        sigm=[1/(1+np.exp(-i)) for i in x]
    
    return sigm