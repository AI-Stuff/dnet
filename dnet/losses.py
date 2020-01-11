import jax.numpy as tensor
from jax import jit


@jit
def binary_crossentropy(outputs: tensor.array, targets: tensor.array) -> float:
    return -tensor.mean(targets * tensor.log(outputs) + (1 - targets) * tensor.log(1 - outputs))


@jit
def categorical_crossentropy(outputs: tensor.array, targets: tensor.array) -> float:
    return tensor.mean(a=-tensor.sum(a=targets * tensor.log(1 - outputs), axis=1))
