from ndn4sid import linearalgebra
import numpy as np


def main():
    A = np.random.randn(3,3)
    B = np.random.randn(3,3)
    A[:,0] = A[0,:] = B[0,:] = B[:,0] = 0
    A[0,0],B[0,0] = 1,2
    L = linearalgebra.get_lie_group([A,B])

    assert len(L)==5

    E1 = linearalgebra.get_random_element_of_group(L)
    assert linearalgebra.get_dim_of_matrix_space(L) == linearalgebra.get_dim_of_matrix_space(L+ [E1])

    E2 = np.random.randn(3,3)
    assert linearalgebra.get_dim_of_matrix_space(L)+1 == linearalgebra.get_dim_of_matrix_space(L+ [E2])


if __name__ == "__main__":
    main()