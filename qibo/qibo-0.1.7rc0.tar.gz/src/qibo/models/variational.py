from qibo import K
from qibo.config import raise_error
from qibo.core.circuit import Circuit
from qibo.models.evolution import StateEvolution


class VQE(object):
    """This class implements the variational quantum eigensolver algorithm.

    Args:
        circuit (:class:`qibo.abstractions.circuit.AbstractCircuit`): Circuit that
            implements the variaional ansatz.
        hamiltonian (:class:`qibo.hamiltonians.Hamiltonian`): Hamiltonian object.

    Example:
        .. testcode::

            import numpy as np
            from qibo import gates, models, hamiltonians
            # create circuit ansatz for two qubits
            circuit = models.Circuit(2)
            circuit.add(gates.RY(0, theta=0))
            # create XXZ Hamiltonian for two qubits
            hamiltonian = hamiltonians.XXZ(2)
            # create VQE model for the circuit and Hamiltonian
            vqe = models.VQE(circuit, hamiltonian)
            # optimize using random initial variational parameters
            initial_parameters = np.random.uniform(0, 2, 1)
            vqe.minimize(initial_parameters)
    """
    from qibo import optimizers

    def __init__(self, circuit, hamiltonian):
        """Initialize circuit ansatz and hamiltonian."""
        self.circuit = circuit
        self.hamiltonian = hamiltonian

    def minimize(self, initial_state, method='Powell', jac=None, hess=None,
                 hessp=None, bounds=None, constraints=(), tol=None, callback=None,
                 options=None, compile=False, processes=None):
        """Search for parameters which minimizes the hamiltonian expectation.

        Args:
            initial_state (array): a initial guess for the parameters of the
                variational circuit.
            method (str): the desired minimization method.
                See :meth:`qibo.optimizers.optimize` for available optimization
                methods.
            jac (dict): Method for computing the gradient vector for scipy optimizers.
            hess (dict): Method for computing the hessian matrix for scipy optimizers.
            hessp (callable): Hessian of objective function times an arbitrary
                vector for scipy optimizers.
            bounds (sequence or Bounds): Bounds on variables for scipy optimizers.
            constraints (dict): Constraints definition for scipy optimizers.
            tol (float): Tolerance of termination for scipy optimizers.
            callback (callable): Called after each iteration for scipy optimizers.
            options (dict): a dictionary with options for the different optimizers.
            compile (bool): whether the TensorFlow graph should be compiled.
            processes (int): number of processes when using the paralle BFGS method.

        Return:
            The final expectation value.
            The corresponding best parameters.
            The optimization result object. For scipy methods it returns
            the ``OptimizeResult``, for ``'cma'`` the ``CMAEvolutionStrategy.result``,
            and for ``'sgd'`` the options used during the optimization.
        """
        def _loss(params, circuit, hamiltonian):
            circuit.set_parameters(params)
            final_state = circuit()
            return hamiltonian.expectation(final_state)

        if compile:
            if K.is_custom:
                raise_error(RuntimeError, "Cannot compile VQE that uses custom operators. "
                                          "Set the compile flag to False.")
            for gate in self.circuit.queue:
                _ = gate.cache
            loss = K.compile(_loss)
        else:
            loss = _loss

        if method == "cma":
            dtype = getattr(K.np, K._dtypes.get('DTYPE'))
            loss = lambda p, c, h: dtype(_loss(p, c, h))
        elif method != "sgd":
            loss = lambda p, c, h: K.to_numpy(_loss(p, c, h))

        result, parameters, extra = self.optimizers.optimize(loss, initial_state,
                                                             args=(self.circuit, self.hamiltonian),
                                                             method=method, jac=jac, hess=hess, hessp=hessp,
                                                             bounds=bounds, constraints=constraints,
                                                             tol=tol, callback=callback, options=options,
                                                             compile=compile, processes=processes)
        self.circuit.set_parameters(parameters)
        return result, parameters, extra


class QAOA(object):
    """ Quantum Approximate Optimization Algorithm (QAOA) model.

    The QAOA is introduced in `arXiv:1411.4028 <https://arxiv.org/abs/1411.4028>`_.

    Args:
        hamiltonian (:class:`qibo.abstractions.hamiltonians.Hamiltonian`): problem Hamiltonian
            whose ground state is sought.
        mixer (:class:`qibo.abstractions.hamiltonians.Hamiltonian`): mixer Hamiltonian.
            If ``None``, :class:`qibo.hamiltonians.X` is used.
        solver (str): solver used to apply the exponential operators.
            Default solver is 'exp' (:class:`qibo.solvers.Exponential`).
        callbacks (list): List of callbacks to calculate during evolution.
        accelerators (dict): Dictionary of devices to use for distributed
            execution. See :class:`qibo.core.distcircuit.DistributedCircuit`
            for more details. This option is available only when ``hamiltonian``
            is a :class:`qibo.abstractions.hamiltonians.SymbolicHamiltonian`.

    Example:
        .. testcode::

            import numpy as np
            from qibo import models, hamiltonians
            # create XXZ Hamiltonian for four qubits
            hamiltonian = hamiltonians.XXZ(4)
            # create QAOA model for this Hamiltonian
            qaoa = models.QAOA(hamiltonian)
            # optimize using random initial variational parameters
            # and default options and initial state
            initial_parameters = 0.01 * np.random.random(4)
            best_energy, final_parameters, extra = qaoa.minimize(initial_parameters, method="BFGS")
    """
    from qibo import hamiltonians, optimizers
    from qibo.core import states

    def __init__(self, hamiltonian, mixer=None, solver="exp", callbacks=[],
                 accelerators=None):
        from qibo.abstractions.hamiltonians import AbstractHamiltonian
        # list of QAOA variational parameters (angles)
        self.params = None
        # problem hamiltonian
        if not isinstance(hamiltonian, AbstractHamiltonian):
            raise_error(TypeError, "Invalid Hamiltonian type {}."
                                   "".format(type(hamiltonian)))
        self.hamiltonian = hamiltonian
        self.nqubits = hamiltonian.nqubits
        # mixer hamiltonian (default = -sum(sigma_x))
        if mixer is None:
            trotter = isinstance(
                self.hamiltonian, self.hamiltonians.SymbolicHamiltonian)
            self.mixer = self.hamiltonians.X(self.nqubits, dense=not trotter)
        else:
            if type(mixer) != type(hamiltonian):
                  raise_error(TypeError, "Given Hamiltonian is of type {} "
                                         "while mixer is of type {}."
                                         "".format(type(hamiltonian),
                                                   type(mixer)))
            self.mixer = mixer

        # create circuits for Trotter Hamiltonians
        if (accelerators is not None and (
            not isinstance(self.hamiltonian, self.hamiltonians.SymbolicHamiltonian)
            or solver != "exp")):
            raise_error(NotImplementedError, "Distributed QAOA is implemented "
                                             "only with SymbolicHamiltonian and "
                                             "exponential solver.")
        if isinstance(self.hamiltonian, self.hamiltonians.SymbolicHamiltonian):
            self.hamiltonian.circuit(1e-2, accelerators)
            self.mixer.circuit(1e-2, accelerators)

        # evolution solvers
        from qibo import solvers
        self.ham_solver = solvers.factory[solver](1e-2, self.hamiltonian)
        self.mix_solver = solvers.factory[solver](1e-2, self.mixer)

        self.state_cls = self.states.VectorState
        self.callbacks = callbacks
        self.accelerators = accelerators
        self.normalize_state = StateEvolution._create_normalize_state(
            self, solver)
        self.calculate_callbacks = StateEvolution._create_calculate_callbacks(
            self, accelerators)

    def set_parameters(self, p):
        """Sets the variational parameters.

        Args:
            p (np.ndarray): 1D-array holding the new values for the variational
                parameters. Length should be an even number.
        """
        self.params = p

    def _apply_exp(self, state, solver, p):
        """Helper method for ``execute``."""
        solver.dt = p
        state = solver(state)
        if self.callbacks:
            state = self.normalize_state(state)
            self.calculate_callbacks(state)
        return state

    def execute(self, initial_state=None):
        """Applies the QAOA exponential operators to a state.

        Args:
            initial_state (np.ndarray): Initial state vector.

        Returns:
            State vector after applying the QAOA exponential gates.
        """
        state = self.get_initial_state(initial_state)
        self.calculate_callbacks(state)
        n = int(self.params.shape[0])
        for i in range(n // 2):
            state = self._apply_exp(state, self.ham_solver,
                                    self.params[2 * i])
            state = self._apply_exp(state, self.mix_solver,
                                    self.params[2 * i + 1])
        return self.normalize_state(state)

    def __call__(self, initial_state=None):
        """Equivalent to :meth:`qibo.models.QAOA.execute`."""
        return self.execute(initial_state)

    def get_initial_state(self, state=None):
        """"""
        if self.accelerators is not None:
            c = self.hamiltonian.circuit(self.params[0])
            if state is None:
                state = self.states.DistributedState.plus_state(c)
            return c.get_initial_state(state)

        if state is None:
            return self.state_cls.plus_state(self.nqubits).tensor
        return Circuit.get_initial_state(self, state)

    def minimize(self, initial_p, initial_state=None, method='Powell',
                 jac=None, hess=None, hessp=None, bounds=None, constraints=(),
                 tol=None, callback=None, options=None, compile=False, processes=None):
        """Optimizes the variational parameters of the QAOA.

        Args:
            initial_p (np.ndarray): initial guess for the parameters.
            initial_state (np.ndarray): initial state vector of the QAOA.
            method (str): the desired minimization method.
                See :meth:`qibo.optimizers.optimize` for available optimization
                methods.
            jac (dict): Method for computing the gradient vector for scipy optimizers.
            hess (dict): Method for computing the hessian matrix for scipy optimizers.
            hessp (callable): Hessian of objective function times an arbitrary
                vector for scipy optimizers.
            bounds (sequence or Bounds): Bounds on variables for scipy optimizers.
            constraints (dict): Constraints definition for scipy optimizers.
            tol (float): Tolerance of termination for scipy optimizers.
            callback (callable): Called after each iteration for scipy optimizers.
            options (dict): a dictionary with options for the different optimizers.
            compile (bool): whether the TensorFlow graph should be compiled.
            processes (int): number of processes when using the paralle BFGS method.

        Return:
            The final energy (expectation value of the ``hamiltonian``).
            The corresponding best parameters.
            The optimization result object. For scipy methods it
            returns the ``OptimizeResult``, for ``'cma'`` the
            ``CMAEvolutionStrategy.result``, and for ``'sgd'``
            the options used during the optimization.
        """
        if len(initial_p) % 2 != 0:
            raise_error(ValueError, "Initial guess for the parameters must "
                                    "contain an even number of values but "
                                    "contains {}.".format(len(initial_p)))

        def _loss(params, qaoa, hamiltonian):
            qaoa.set_parameters(params)
            state = qaoa(initial_state)
            return hamiltonian.expectation(state)

        if method == "sgd":
            loss = lambda p, c, h: _loss(K.cast(p), c, h)
        else:
            loss = lambda p, c, h: K.to_numpy(_loss(p, c, h))

        result, parameters, extra = self.optimizers.optimize(loss, initial_p, args=(self, self.hamiltonian),
                                                             method=method, jac=jac, hess=hess, hessp=hessp,
                                                             bounds=bounds, constraints=constraints,
                                                             tol=tol, callback=callback, options=options,
                                                             compile=compile, processes=processes)
        self.set_parameters(parameters)
        return result, parameters, extra


class FALQON(QAOA):
    """ Feedback-based ALgorithm for Quantum OptimizatioN (FALQON) model.

    The FALQON is introduced in `arXiv:2103.08619 <https://arxiv.org/abs/2103.08619>`_.
    It inherits the QAOA class.

    Args:
        hamiltonian (:class:`qibo.abstractions.hamiltonians.Hamiltonian`): problem Hamiltonian
            whose ground state is sought.
        mixer (:class:`qibo.abstractions.hamiltonians.Hamiltonian`): mixer Hamiltonian.
            If ``None``, :class:`qibo.hamiltonians.X` is used.
        solver (str): solver used to apply the exponential operators.
            Default solver is 'exp' (:class:`qibo.solvers.Exponential`).
        callbacks (list): List of callbacks to calculate during evolution.
        accelerators (dict): Dictionary of devices to use for distributed
            execution. See :class:`qibo.tensorflow.distcircuit.DistributedCircuit`
            for more details. This option is available only when ``hamiltonian``
            is a :class:`qibo.abstractions.hamiltonians.SymbolicHamiltonian`.

    Example:
        .. testcode::

            import numpy as np
            from qibo import models, hamiltonians
            # create XXZ Hamiltonian for four qubits
            hamiltonian = hamiltonians.XXZ(4)
            # create FALQON model for this Hamiltonian
            falqon = models.FALQON(hamiltonian)
            # optimize using random initial variational parameters
            # and default options and initial state
            delta_t = 0.01
            max_layers = 3
            best_energy, final_parameters, extra = falqon.minimize(delta_t, max_layers)
    """

    def __init__(self, hamiltonian, mixer=None, solver="exp", callbacks=[],
                 accelerators=None):
        super().__init__(hamiltonian, mixer, solver, callbacks, accelerators)
        self.evol_hamiltonian = 1j * (self.hamiltonian @ self.mixer - self.mixer @ self.hamiltonian)

    def minimize(self, delta_t, max_layers, initial_state=None, tol=None, callback=None):
        """Optimizes the variational parameters of the FALQON.

        Args:
            delta_t (float): initial guess for the time step. A too large delta_t will make the algorithm fail.
            max_layers (int): maximum number of layers allowed for the FALQON.
            initial_state (np.ndarray): initial state vector of the FALQON.
            tol (float): Tolerance of energy change. If not specified, no check is done.
            callback (callable): Called after each iteration for scipy optimizers.
            options (dict): a dictionary with options for the different optimizers.

        Return:
            The final energy (expectation value of the ``hamiltonian``).
            The corresponding best parameters.
            extra: variable with historical data for the energy and callbacks.
        """
        import numpy as np
        parameters = np.array([delta_t, 0])

        def _loss(params, falqon, hamiltonian):
            falqon.set_parameters(params)
            state = falqon(initial_state)
            return hamiltonian.expectation(state)

        energy = [np.inf]
        callback_result = []
        for it in range(1, max_layers + 1):
            beta = K.to_numpy(_loss(parameters, self, self.evol_hamiltonian))

            if tol is not None:
                energy.append(K.to_numpy(_loss(parameters, self, self.hamiltonian)))
                if abs(energy[-1] - energy[-2]) < tol:
                    break

            if callback is not None:
                callback_result.append(callback(parameters))

            parameters = np.concatenate([parameters, [delta_t, delta_t * beta]])

        self.set_parameters(parameters)
        final_loss = _loss(parameters, self, self.hamiltonian)
        extra = {'energies': energy, 'callbacks': callback_result}
        return final_loss, parameters, extra
