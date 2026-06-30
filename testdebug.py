import torch
import torch.nn as nn
x = torch.randn(3,3)    
y=x @ x.T
p=nn.Linear(3,3)
q=p(y)
z=y.sum()
print(z)
print(q)