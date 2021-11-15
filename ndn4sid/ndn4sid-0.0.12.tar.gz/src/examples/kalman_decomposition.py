import numpy as np
import ndn4sid
from ndn4sid import linearalgebra
from ndn4sid import systems
np.set_printoptions(precision=2,suppress=True)

def main():
    # Calculate a random premutation
    n = 10
    T = np.eye(4,dtype=int)
    T_inv = np.eye(4,dtype=int)
    for _ in range(n):
        Tk,T_inv_k = linearalgebra.get_random_permutation(4)
        T = T@Tk
        T_inv = T_inv_k@T_inv

        
    A = np.diag([1,2,3,4])
    B = np.diag([5,6,7,8])
    x0 = np.array([1,1,0,0])
    C = np.array([1,0,1,0])

    my_system = systems.SS([A,B],C,x0,suppress_warnings=True)
    new_sys = systems.transformSS(my_system,T_inv,T,'Original System')

    systems.print_state_space_model(new_sys)
    T,T_inv = systems.get_kalman_decomposition(new_sys)
    kal_sys = systems.transformSS(new_sys,T,T_inv,'Kalman Decomposition')
    systems.print_state_space_model(kal_sys)


if __name__ == "__main__":
    main()