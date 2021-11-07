# -*- coding: utf-8 -*-
from qibo import matrices, K
from qibo.config import raise_error
from qibo.core.hamiltonians import Hamiltonian, SymbolicHamiltonian, TrotterHamiltonian
from qibo.core.terms import HamiltonianTerm


def multikron(matrix_list):
    """Calculates Kronecker product of a list of matrices.

    Args:
        matrices (list): List of matrices as ``np.ndarray``s.

    Returns:
        ``np.ndarray`` of the Kronecker product of all ``matrices``.
    """
    h = 1
    for m in matrix_list:
        h = K.np.kron(h, m)
    return h


def _build_spin_model(nqubits, matrix, condition):
    """Helper method for building nearest-neighbor spin model Hamiltonians."""
    h = sum(multikron(
      (matrix if condition(i, j) else matrices.I for j in range(nqubits)))
            for i in range(nqubits))
    return h


def XXZ(nqubits, delta=0.5, dense=True):
    """Heisenberg XXZ model with periodic boundary conditions.

    .. math::
        H = \\sum _{i=0}^N \\left ( X_iX_{i + 1} + Y_iY_{i + 1} + \\delta Z_iZ_{i + 1} \\right ).

    Args:
        nqubits (int): number of quantum bits.
        delta (float): coefficient for the Z component (default 0.5).
        dense (bool): If ``True`` it creates the Hamiltonian as a
            :class:`qibo.core.hamiltonians.Hamiltonian`, otherwise it creates
            a :class:`qibo.core.hamiltonians.SymbolicHamiltonian`.

    Example:
        .. testcode::

            from qibo.hamiltonians import XXZ
            h = XXZ(3) # initialized XXZ model with 3 qubits
    """
    if dense:
        condition = lambda i, j: i in {j % nqubits, (j+1) % nqubits}
        hx = _build_spin_model(nqubits, matrices.X, condition)
        hy = _build_spin_model(nqubits, matrices.Y, condition)
        hz = _build_spin_model(nqubits, matrices.Z, condition)
        matrix = hx + hy + delta * hz
        return Hamiltonian(nqubits, matrix)

    hx = K.np.kron(matrices.X, matrices.X)
    hy = K.np.kron(matrices.Y, matrices.Y)
    hz = K.np.kron(matrices.Z, matrices.Z)
    matrix = hx + hy + delta * hz
    terms = [HamiltonianTerm(matrix, i, i + 1) for i in range(nqubits - 1)]
    terms.append(HamiltonianTerm(matrix, nqubits - 1, 0))
    ham = SymbolicHamiltonian()
    ham.terms = terms
    return ham


def _OneBodyPauli(nqubits, matrix, dense=True, ground_state=None):
    """Helper method for constracting non-interacting X, Y, Z Hamiltonians."""
    if dense:
        condition = lambda i, j: i == j % nqubits
        ham = -_build_spin_model(nqubits, matrix, condition)
        return Hamiltonian(nqubits, ham)

    matrix = - matrix
    terms = [HamiltonianTerm(matrix, i) for i in range(nqubits)]
    ham = SymbolicHamiltonian(ground_state=ground_state)
    ham.terms = terms
    return ham


def X(nqubits, dense=True):
    """Non-interacting Pauli-X Hamiltonian.

    .. math::
        H = - \\sum _{i=0}^N X_i.

    Args:
        nqubits (int): number of quantum bits.
        dense (bool): If ``True`` it creates the Hamiltonian as a
            :class:`qibo.core.hamiltonians.Hamiltonian`, otherwise it creates
            a :class:`qibo.core.hamiltonians.SymbolicHamiltonian`.
    """
    from qibo import K
    def ground_state():
        n = K.cast((2 ** nqubits,), dtype='DTYPEINT')
        state = K.ones(n, dtype='DTYPECPX')
        return state / K.sqrt(K.cast(n, dtype=state.dtype))
    return _OneBodyPauli(nqubits, matrices.X, dense, ground_state)


def Y(nqubits, dense=True):
    """Non-interacting Pauli-Y Hamiltonian.

    .. math::
        H = - \\sum _{i=0}^N Y_i.

    Args:
        nqubits (int): number of quantum bits.
        dense (bool): If ``True`` it creates the Hamiltonian as a
            :class:`qibo.core.hamiltonians.Hamiltonian`, otherwise it creates
            a :class:`qibo.core.hamiltonians.SymbolicHamiltonian`.
    """
    return _OneBodyPauli(nqubits, matrices.Y, dense)


def Z(nqubits, dense=True):
    """Non-interacting Pauli-Z Hamiltonian.

    .. math::
        H = - \\sum _{i=0}^N Z_i.

    Args:
        nqubits (int): number of quantum bits.
        dense (bool): If ``True`` it creates the Hamiltonian as a
            :class:`qibo.core.hamiltonians.Hamiltonian`, otherwise it creates
            a :class:`qibo.core.hamiltonians.SymbolicHamiltonian`.
    """
    return _OneBodyPauli(nqubits, matrices.Z, dense)


def TFIM(nqubits, h=0.0, dense=True):
    """Transverse field Ising model with periodic boundary conditions.

    .. math::
        H = - \\sum _{i=0}^N \\left ( Z_i Z_{i + 1} + h X_i \\right ).

    Args:
        nqubits (int): number of quantum bits.
        h (float): value of the transverse field.
        dense (bool): If ``True`` it creates the Hamiltonian as a
            :class:`qibo.core.hamiltonians.Hamiltonian`, otherwise it creates
            a :class:`qibo.core.hamiltonians.SymbolicHamiltonian`.
    """
    if dense:
        condition = lambda i, j: i in {j % nqubits, (j+1) % nqubits}
        ham = -_build_spin_model(nqubits, matrices.Z, condition)
        if h != 0:
            condition = lambda i, j: i == j % nqubits
            ham -= h * _build_spin_model(nqubits, matrices.X, condition)
        return Hamiltonian(nqubits, ham)

    matrix = -(K.np.kron(matrices.Z, matrices.Z) + h * K.np.kron(matrices.X, matrices.I))
    terms = [HamiltonianTerm(matrix, i, i + 1) for i in range(nqubits - 1)]
    terms.append(HamiltonianTerm(matrix, nqubits - 1, 0))
    ham = SymbolicHamiltonian()
    ham.terms = terms
    return ham


def MaxCut(nqubits, dense=True):
    """Max Cut Hamiltonian.

    .. math::
        H = - \\sum _{i,j=0}^N  \\frac{1 - Z_i Z_j}{2}.

    Args:
        nqubits (int): number of quantum bits.
        dense (bool): If ``True`` it creates the Hamiltonian as a
            :class:`qibo.core.hamiltonians.Hamiltonian`, otherwise it creates
            a :class:`qibo.core.hamiltonians.SymbolicHamiltonian`.
    """
    import sympy as sp

    Z = sp.symbols(f'Z:{nqubits}')
    V = sp.symbols(f'V:{nqubits**2}')
    sham = - sum(V[i * nqubits + j] * (1 - Z[i] * Z[j]) for i in range(nqubits) for j in range(nqubits))
    sham /= 2

    v = K.qnp.ones(nqubits**2, dtype='DTYPEINT')
    smap = {s: (i, matrices.Z) for i, s in enumerate(Z)}
    smap.update({s: (i, v[i]) for i, s in enumerate(V)})

    ham = SymbolicHamiltonian(sham, smap)
    if dense:
        return ham.dense
    return ham
