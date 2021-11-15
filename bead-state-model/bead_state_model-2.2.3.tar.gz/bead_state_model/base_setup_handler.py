from abc import ABC, abstractmethod
from typing import Dict, Any

from readdy import ReactionDiffusionSystem


class BaseSetupHandler(ABC):
    """
    Derive from this class to implement setup handlers for your simulation setup.
    Provide an instance of your implemented class when creating ``bead_state_model.System`` instances.
    Override the ``__call__`` method to contain the configuration of interactions between
    the 4 filament particles ``["head", "core", "motor", "tail"]`` and any external particles/topologies
    you have defined. Furthermore, define any external potentials (to create layers of filaments, etc.)
    affecting filaments or any external particles.
    Override the ``from_config_dict`` and ``to_config_dict`` methods to make your simulation output
    reproducible. I.e., it has to be possible to create identical instances of your implemented SetupHandler
    through the ``from_config_dict`` method with the dictionary that your ``to_config_dict`` method returns.
    """

    @abstractmethod
    def __call__(self, system: ReactionDiffusionSystem):
        ...

    @staticmethod
    @abstractmethod
    def from_config_dict(d: Dict[str, Any]) -> 'BaseSetupHandler':
        ...

    @abstractmethod
    def to_config_dict(self) -> Dict[str, Any]:
        ...
