import math
import random

from pymoo.core.mutation import Mutation

import protein_mutation
import valueGenerator


class MyMutation(Mutation):
    def __init__(self):
        super().__init__()

    def _do(self, problem, X, **kwargs):

        for i in range(len(X)):

            r = random.random()

            if r < 0.5:

                X[i,0]=protein_mutation.mutate1(X[i,0],allowed=problem.allows)

        return X
