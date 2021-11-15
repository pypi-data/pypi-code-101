import numpy as np
from ndn4sid import linearalgebra as la
from ndn4sid import systems


def main():
    # Define an example system
    A = np.diag([1,2,3,4])
    B = np.diag([5,6,7,8])
    x0 = np.array([1,1,1,1])
    C = np.array([1,1,1,1])

    my_system = systems.SS([A,B],C,x0,suppress_warnings=True)

    polynomials,variables = systems.cayley_hamilton(my_system)

    for polynomial in polynomials:
        print(f'Evaluating: {polynomial}')
        f = systems.eval_matrix_polynomial(polynomial,variables,[A,B])
        norm = np.linalg.norm(f)
        print(f'Norm: {norm}')
        assert norm < 1e-10


if __name__ == "__main__":
    main()