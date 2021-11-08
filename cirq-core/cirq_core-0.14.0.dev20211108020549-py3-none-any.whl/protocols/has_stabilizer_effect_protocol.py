# Copyright 2018 The Cirq Developers
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from typing import (
    Any,
    Optional,
)

from cirq.ops.clifford_gate import SingleQubitCliffordGate

from cirq import protocols


def has_stabilizer_effect(val: Any) -> bool:
    """Returns whether the input has a stabilizer effect.

    For 1-qubit gates always returns correct result. For other operations relies
    on the operation to define whether it has stabilizer effect.
    """
    strats = [
        _strat_has_stabilizer_effect_from_has_stabilizer_effect,
        _strat_has_stabilizer_effect_from_gate,
        _strat_has_stabilizer_effect_from_unitary,
    ]
    for strat in strats:
        result = strat(val)
        if result is not None:
            return result

    # If you can't determine if it has stabilizer effect,  it does not.
    return False


# TODO(#3388) Add summary line to docstring.
# pylint: disable=docstring-first-line-empty
def _strat_has_stabilizer_effect_from_has_stabilizer_effect(val: Any) -> Optional[bool]:
    """
    Attempts to infer whether val has stabilizer effect via its
    _has_stabilizer_effect_ method.
    """
    if hasattr(val, '_has_stabilizer_effect_'):
        result = val._has_stabilizer_effect_()
        if result is not NotImplemented and result is not None:
            return result
    return None


# TODO(#3388) Add summary line to docstring.
def _strat_has_stabilizer_effect_from_gate(val: Any) -> Optional[bool]:
    """
    Attempts to infer whether val has stabilizer effect via the value of
    _has_stabilizer_effect_ method of its constituent gate.
    """
    if hasattr(val, 'gate'):
        return _strat_has_stabilizer_effect_from_has_stabilizer_effect(val.gate)
    return None


# pylint: enable=docstring-first-line-empty
def _strat_has_stabilizer_effect_from_unitary(val: Any) -> Optional[bool]:
    """Attempts to infer whether val has stabilizer effect from its unitary.
    Returns whether unitary of `val` normalizes the Pauli group. Works only for
    2x2 unitaries.
    """
    # Do not try this strategy if there is no unitary or if the number of
    # qubits is not 1 since that would be expensive.
    if not protocols.has_unitary(val) or protocols.num_qubits(val) != 1:
        return None
    unitary = protocols.unitary(val)
    return SingleQubitCliffordGate.from_unitary(unitary) is not None
