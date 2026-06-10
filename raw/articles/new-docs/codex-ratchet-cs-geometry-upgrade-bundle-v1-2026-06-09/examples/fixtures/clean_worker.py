# clean fixture
import torch

def f(x):
    return torch.utils.dlpack.to_dlpack(x)  # legacy API use would be handled by stricter JAX/Torch lints later
