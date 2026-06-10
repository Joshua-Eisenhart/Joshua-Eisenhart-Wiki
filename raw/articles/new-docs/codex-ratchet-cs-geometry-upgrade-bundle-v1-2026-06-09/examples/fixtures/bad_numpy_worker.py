import numpy as np
import pandas as pd
import networkx as nx
import torch

def bad(x):
    a = np.asarray(x)
    b = np.array(a)
    c = torch.tensor([1]).cpu().detach().numpy()
    d = pd.DataFrame({"x": [1]})
    g = nx.Graph()
    return b, c, d, g
