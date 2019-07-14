import numpy as np

class Boundary:

    #initializer #1 - Dirichlet
    def __init__(self, ind_x=None, ind_y=None, value=None, bc_type=None):

        self.ind_x = ind_x
        self.ind_y = ind_y
        self.value = value
        if isinstance(value, float): self.type = 'dirichlet'
        elif isinstance(value, list): self.type = 'neumann'


    # @classmethod
    # def Dirichlet(cls, ind_x: list, ind_y: list, value: float) -> 'Boundary':
    #     return cls(ind_x, ind_y, value, 'dirichlet')
    #
    # @classmethod
    # def Neumann(cls, ind_x: list, ind_y: list, value: list) -> 'Boundary':
    #     return cls(ind_x, ind_y, value, 'neumann')


