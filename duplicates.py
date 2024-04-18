from pymoo.core.duplicate import ElementwiseDuplicateElimination

class MyDuplicateElimination(ElementwiseDuplicateElimination):

    def is_equal(self, a, b):

        return 0
