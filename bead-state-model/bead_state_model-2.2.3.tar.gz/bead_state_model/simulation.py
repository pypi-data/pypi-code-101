import json
import os
import sys
from dataclasses import dataclass, asdict
from typing import Union, Dict, Any, Optional, List, Tuple

import numpy as np
import toml

from bead_state_model.base_setup_handler import BaseSetupHandler
from bead_state_model.components import Filament
from bead_state_model.data_reader import DataReader
from bead_state_model.system_setup import system_setup, simulation_setup, add_filaments_from_file, add_filaments

_ParticleName = str
_DiffusionConst = float
_ParticleCoordinates = np.ndarray
_Box = Union[np.ndarray, List[float], Tuple[float, float, float]]


@dataclass
class SimulationParameters:

    box_size: _Box
    k_bend: float
    k_stretch: float
    n_beads_max: int
    diffusion_const: float = 1.0
    min_network_distance: int = 6
    rate_motor_step: float = 0.0
    rate_motor_bind: float = 0.0
    rate_motor_unbind: float = 0.0
    reaction_radius_motor_binding: float = 1.05
    rate_attach: float = 0.0
    rate_detach: float = 0.0
    k_repulsion: float = 80.0
    n_max_motors: Optional[int] = None

    @staticmethod
    def load_parameters_from_generated_network(
            config_file: str
    ) -> Tuple[_Box, float, float]:
        with open(config_file, 'rt') as fp:
            network_config = json.load(fp)
        k_bend = network_config['k_bend']
        k_stretch = network_config['k_stretch']
        box = np.array(network_config['box'])
        return box, k_stretch, k_bend

    @staticmethod
    def load_parameters_from_simulation_toml(
            config_file: str
    ) -> 'SimulationParameters':
        with open(config_file, 'rt') as fp:
            config = toml.load(fp)
        config['parameters']['box_size'] = [float(value) for value in config['parameters']['box_size']]
        return SimulationParameters(**config['parameters'])


class Simulation:

    def __init__(
            self,
            output_folder: str,
            parameters: Union[SimulationParameters, Dict[str, Any]],
            kernel: str = 'SingleCPU',
            non_filament_particles: Optional[Dict[_ParticleName, _DiffusionConst]] = None,
            interaction_setup_handler: Optional[BaseSetupHandler] = None
    ):
        self._filaments_were_added = False
        self.output_folder = output_folder
        self._run_parameters = None  # type: Union[None, Dict[str, Any]]
        os.makedirs(output_folder, exist_ok=True)
        if isinstance(parameters, dict):
            self._parameters = SimulationParameters(**parameters)
        else:
            self._parameters = SimulationParameters(**asdict(parameters))

        self._system, self._filament_handler = system_setup(**asdict(self._parameters))

        if non_filament_particles:
            for name, diffusion_const in non_filament_particles.items():
                self._system.add_species(name, diffusion_const)

        if interaction_setup_handler:
            interaction_setup_handler(self._system)
        self._interaction_setup_handler = interaction_setup_handler

        self.readdy_simulation = simulation_setup(self._system, self._filament_handler, kernel)
        self._configure_output_files()

    def _configure_output_files(self):
        self._filament_handler.output_file = os.path.join(self.output_folder, 'links.h5')
        self.readdy_simulation.output_file = os.path.join(self.output_folder, 'data.h5')
        if os.path.exists(self._filament_handler.output_file):
            os.remove(self._filament_handler.output_file)
        if os.path.exists(self.readdy_simulation.output_file):
            os.remove(self.readdy_simulation.output_file)

    def add_non_filament_particles(self, **particles: _ParticleCoordinates):
        if self._filaments_were_added:
            raise RuntimeError("You need to add all non-filament particles before adding filament particles.")
        for name in particles:
            coords = particles[name]
            assert coords.ndim == 2, ("External particle coordinates has to be an array "
                                      "with two axes: (number of particles, xyz coordinates")
            for c in coords:
                self._filament_handler.add_non_filament_particle(name, c)

    def add_filaments(self, filament_init_file: Union[str, None]):
        self._filaments_were_added = True
        if filament_init_file is None:
            raise NotImplementedError("Currently you have to provide a file with initial filaments."
                                      " If you want to start with empty simulation boxes, use the "
                                      "lower level functions system_setup and simulation_setup, or"
                                      "make a feature request on gitlab.")

        ext = os.path.splitext(filament_init_file)[1]
        if ext == '.txt':
            beads, filaments, links = add_filaments_from_file(self.readdy_simulation, filament_init_file,
                                                              offset=-np.array(self._parameters.box_size)/2)
        elif ext == '.h5':
            dr = DataReader(filament_init_file)
            positions_final_frame = dr.read_particle_positions(minimum_image=True)[-1]
            n_frames = dr.read_n_frames()
            filaments_init, links_init = dr.get_filaments(n_frames-1)
            map_filament_indices, map_bead_indices, filaments, links = add_filaments(
                self.readdy_simulation,
                positions_final_frame[dr.get_n_non_filament_particles():],
                filaments_init, links_init
            )

            np.save(os.path.join(self.output_folder, 'map_filaments_to_init_state.npy'), map_filament_indices)
            np.save(os.path.join(self.output_folder, 'map_beads_to_init_state.npy'), map_bead_indices)
        else:
            raise RuntimeError("File has to end on .txt or .h5.")

        self._filament_handler.initialize(filaments, links)

    def add_filaments_via_arrays(self, filament_positions: np.ndarray, links_init: np.ndarray):
        if len(filament_positions) != len(links_init):
            raise ValueError("Provided initial filament positions and links between filament particles have "
                             "to be of same length.")
        self._filaments_were_added = True
        filaments_init = _generate_filaments_from_link_array(links_init)
        map_filament_indices, map_bead_indices, filaments, links = add_filaments(
            self.readdy_simulation,
            filament_positions,
            filaments_init, links_init
        )

        np.save(os.path.join(self.output_folder, 'map_filaments_to_init_state.npy'), map_filament_indices)
        np.save(os.path.join(self.output_folder, 'map_beads_to_init_state.npy'), map_bead_indices)
        self._filament_handler.initialize(filaments, links)

    def run(self, n_steps: int, dt: float, observation_interval: int, mute=False):
        if not self._filaments_were_added:
            raise RuntimeError("Add filaments via method add_filaments before running the simulation.")
        self._run_parameters = {
            'n_steps': n_steps,
            'dt': dt,
            'observation_interval': observation_interval
        }
        self.readdy_simulation.record_trajectory(observation_interval)
        self.readdy_simulation.observe.particles(observation_interval,
                                                 callback=self._filament_handler.write,
                                                 save=False)
        self._save_configuration()
        if mute:
            _normal_stdout = sys.stdout
            _normal_stderr = sys.stderr
            sys.stdout = open(os.devnull, 'w')
            sys.stderr = open(os.devnull, 'w')
            self.readdy_simulation.run(n_steps, dt)
            sys.stdout = _normal_stdout
            sys.stderr = _normal_stderr
        else:
            self.readdy_simulation.run(n_steps, dt)

        self._save_final_state()

    def _save_final_state(self):
        positions_final = np.full((len(self.readdy_simulation.current_particles), 3), np.nan)
        for i, p in enumerate(self.readdy_simulation.current_particles):
            positions_final[i] = p.pos

        np.save(os.path.join(self.output_folder, 'positions_final_frame.npy'), positions_final)

    def _save_configuration(self):
        p = asdict(self._parameters)
        p['box_size'] = [float(v) for v in self._parameters.box_size]
        config = {
            'parameters': p,
            'run-parameters': self._run_parameters,
            'filament-handler': {
                'index_offset': self._filament_handler.get_index_offset()
            }
        }
        if self._interaction_setup_handler is not None:
            config['interaction_setup_parameters'] = self._interaction_setup_handler.to_config_dict()
        with open(os.path.join(self.output_folder, 'config.toml'), 'wt') as fp:
            toml.dump(config, fp)


def _generate_filaments_from_link_array(links: np.ndarray) -> List[Filament]:
    filaments = []
    for i, row in enumerate(links):
        if not _is_tail(*row):
            continue
        id_ = len(filaments)
        filaments.append(Filament(id_, i, links))
    return filaments


def _is_tail(previous, nxt, cross_filament) -> bool:
    if previous != -1:
        return False
    if nxt == -1:
        return False
    if cross_filament != -1:
        return False
    return True
