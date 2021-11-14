"""An extended version of SAM learner that is able to handle predicates inconsistency."""
from collections import defaultdict
from typing import Optional, Dict, Set, NoReturn, Iterable, List

from pddl.pddl import Action, Domain, Effect

from .core import ExtendedMatcher, extract_effects, LightProxyActionGenerator
from .sam_learner import SAMLearner
from .sam_models import Mode, GroundedAction, State, ComparablePredicate, Trajectory, SignatureType


def sort_predicates(predicates: Iterable[ComparablePredicate]) -> List[ComparablePredicate]:
    """Sorts the predicate list so that it could be compared to other lists.

    :param predicates: the predicates to sort.
    :return: the sorted predicate list.
    """
    return sorted(
        predicates, key=lambda predicate: (predicate.name, str(predicate.signature)))


class ESAMLearner(SAMLearner):
    """Extension to the SAM Learning algorithm."""

    matcher: ExtendedMatcher
    proxy_action_generator: LightProxyActionGenerator
    # Maps an action name to a dictionary of effect predicate names to their possible bindings.
    add_effect_cnfs: Dict[str, Dict[str, Set[ComparablePredicate]]]
    delete_effect_cnfs: Dict[str, Dict[str, Set[ComparablePredicate]]]
    # Maps an action name to a dictionary of preconditions predicate names to their possible bindings.
    precondition_cnfs: Dict[str, Dict[str, Set[ComparablePredicate]]]
    learned_actions_signatures: Dict[str, SignatureType]

    def __init__(
            self, working_directory_path: Optional[str] = None, domain_file_name: str = "domain.pddl",
            mode: Mode = "production", domain: Optional[Domain] = None, known_actions: Dict[str, Action] = {}):
        super().__init__(working_directory_path, domain_file_name, mode, domain, known_actions)
        self.proxy_action_generator = LightProxyActionGenerator()
        self.add_effect_cnfs = {}
        self.delete_effect_cnfs = {}
        self.precondition_cnfs = {}
        self.learned_actions_signatures = {}
        if mode == "development":
            self.matcher = ExtendedMatcher(domain=domain)
            return

        domain_path = self.working_directory_path / domain_file_name
        self.matcher = ExtendedMatcher(domain_path=str(domain_path))

    def _add_predicates_cnfs(
            self, predicates: List[ComparablePredicate]) -> Dict[str, Set[ComparablePredicate]]:
        """Adds fluents to a CNF clause when needed.

        :param predicates: the predicates that have been currently observed.
        :return: the dictionary of the fluents after the new information was added.
        """
        predicates_cnf = defaultdict(set)
        for predicate in predicates:
            for index, signature_item in enumerate(predicate.signature):
                if type(signature_item[1]) is tuple:
                    continue

                predicate.signature[index] = (signature_item[0], (signature_item[1], ))

            predicates_cnf[predicate.name].add(predicate)

        return predicates_cnf

    def _update_preconditions_cnfs(self, action_name: str,
                                   possible_preconditions: List[ComparablePredicate]) -> NoReturn:
        """Update the precondition CNFs for an action that had already been observed.

        :param action_name: the name of the action that is currently being learned.
        :param possible_preconditions: the fluents that were observed in the current trajectory triplet.
        """
        action_preconditions = self.precondition_cnfs[action_name]
        self.logger.debug("Removing predicates that don't exist in the current trajectory triplet.")
        current_precondition_names = [predicate.name for predicate in possible_preconditions]
        previous_precondition_names = [name for name in self.precondition_cnfs[action_name]]
        predicates_to_remove = set(previous_precondition_names).difference(current_precondition_names)
        intersection_predicates = set(previous_precondition_names).intersection(current_precondition_names)
        for cnf_predicate in predicates_to_remove:
            del action_preconditions[cnf_predicate]

        self.logger.debug("Removing redundant precondition if there are several bindings to the predicates.")
        remaining_predicates = [predicate for predicate in possible_preconditions if
                                predicate.name in intersection_predicates]
        current_preconditions_cnf = self._add_predicates_cnfs(remaining_predicates)
        for precondition_name in action_preconditions:
            current_cnfs = current_preconditions_cnf[precondition_name]
            action_preconditions[precondition_name] = current_cnfs.intersection(action_preconditions[precondition_name])

    def _update_effects_cnfs(self, new_lifted_effects: List[ComparablePredicate],
                             effects_to_update: Dict[str, Set[ComparablePredicate]]) -> NoReturn:
        """Update the CNF clauses of an already observed action.

        :param action_name: the name of the action that is being updated.
        :param new_lifted_effects: the newly observed lifted effects observed for the action.
        :param effects_to_update: the current CNF clauses that the action has.
        """
        new_effects_cnfs = self._add_predicates_cnfs(new_lifted_effects)
        not_encountered_cnfs = {}
        for predicate_name, new_possible_effect_cnfs in new_effects_cnfs.items():
            if predicate_name not in effects_to_update:
                self.logger.debug("Adding a new effect that hadn't been encountered before.")
                not_encountered_cnfs[predicate_name] = new_possible_effect_cnfs

            else:
                self.logger.debug("Removing redundant CNF clauses from the effect clauses of the predicate.")
                previous_effects = effects_to_update[predicate_name]
                effects_to_update[predicate_name] = new_possible_effect_cnfs.intersection(previous_effects)

        effects_to_update.update(not_encountered_cnfs)

    def add_new_action(
            self, grounded_action: GroundedAction, previous_state: State, next_state: State) -> NoReturn:
        """Learns the model of an action that was observed for the first time.

        :param grounded_action: the grounded action that was observed in the trajectory triplet.
        :param previous_state: the state that was observed prior to the action's exection.
        :param next_state: the state that was observed after the action's execution.
        """
        action_name = grounded_action.lifted_action_name
        self.logger.info(f"Action {action_name} encountered for the first time! Adding its data to the data structure.")
        action_signature = grounded_action.lifted_signature
        self.learned_actions_signatures[action_name] = action_signature
        possible_preconditions = self.matcher.get_possible_literal_matches(grounded_action,
                                                                           previous_state.facts)
        self.precondition_cnfs[action_name] = self._add_predicates_cnfs(possible_preconditions)

        grounded_add_effects, grounded_del_effects = extract_effects(previous_state, next_state)
        lifted_add_effects = self.matcher.get_possible_literal_matches(grounded_action, grounded_add_effects)
        self.add_effect_cnfs[action_name] = self._add_predicates_cnfs(lifted_add_effects)
        lifted_del_effects = self.matcher.get_possible_literal_matches(grounded_action, grounded_del_effects)
        self.delete_effect_cnfs[action_name] = self._add_predicates_cnfs(lifted_del_effects)
        self.logger.debug(f"Finished adding {action_name} information to the data structure")

    def update_action(self, grounded_action: GroundedAction, previous_state: State, next_state: State) -> NoReturn:
        """Updates an action that was observed at least once already.

        :param grounded_action: the grounded action that was executed according to the trajectory.
        :param previous_state: the state that the action was executed on.
        :param next_state: the state that was created after executing the action on the previous
            state.
        """
        action_name = grounded_action.lifted_action_name
        self.logger.info(f"Starting to update the action - {action_name}")
        possible_preconditions = self.matcher.get_possible_literal_matches(grounded_action,
                                                                           previous_state.facts)
        self._update_preconditions_cnfs(action_name, possible_preconditions)

        grounded_add_effects, grounded_del_effects = extract_effects(previous_state, next_state)
        new_lifted_add_effects = self.matcher.get_possible_literal_matches(grounded_action, grounded_add_effects)
        new_lifted_delete_effects = self.matcher.get_possible_literal_matches(grounded_action, grounded_del_effects)
        self._update_effects_cnfs(new_lifted_add_effects, self.add_effect_cnfs[action_name])
        self._update_effects_cnfs(new_lifted_delete_effects, self.delete_effect_cnfs[action_name])
        self.logger.debug(f"Done updating the action - {action_name}")

    def _is_proxy_action(self, action_name: str) -> bool:
        """Validate whether or not an action is supposed to be a proxy action due to the fact that it has ambiguous
            effects.

        :param action_name: the name of the action that is currently being tested.
        :return: whether or not an action is a proxy action.
        """
        action_add_effects = self.add_effect_cnfs[action_name]
        action_del_effects = self.delete_effect_cnfs[action_name]
        return any([len(cnf) > 1 for cnf in action_add_effects.values()]) or \
               any([len(cnf) > 1 for cnf in action_del_effects.values()])

    def create_proxy_actions(self) -> Dict[str, Action]:
        """Create the proxy actions for the cases where there is ambiguity in the learning process.

        :return: the actions that the model learned through its execution stage.
        """
        learned_actions = {}
        for action_name in self.precondition_cnfs:
            if not self._is_proxy_action(action_name):
                self.logger.debug(f"Action - {action_name} has no ambiguities, creating regular action.")
                action = self._create_action_from_cnf(action_name)
                learned_actions[action_name] = action

            else:
                # In the light version of the proxy action generator we don't have to remove the constants.
                self.logger.debug(f"Creating proxy actions for the action - {action_name}")
                proxy_actions = self.proxy_action_generator.create_proxy_actions(
                    action_name=action_name,
                    action_signature=self.learned_actions_signatures[action_name],
                    precondition_cnfs=self.precondition_cnfs[action_name],
                    add_effect_cnfs=self.add_effect_cnfs[action_name],
                    delete_effect_cnfs=self.delete_effect_cnfs[action_name]
                )
                for action in proxy_actions:
                    learned_actions[action.name] = action

        return learned_actions

    def _create_action_from_cnf(self, action_name: str) -> Action:
        """Create the action object from the CNF clauses collected through the algorithm's execution.

        :param action_name: the name of the action that is currently being created.
        :return: the action that was created from the CNF clauses (not proxy action).
        """
        action_preconditions_cnf = self.precondition_cnfs[action_name]
        action_add_effect_cnf = self.add_effect_cnfs[action_name]
        action_delete_effect_cnf = self.delete_effect_cnfs[action_name]
        preconditions = []
        add_effects = set()
        delete_effects = set()
        for fluents in action_preconditions_cnf.values():
            preconditions += list(fluents)

        for add_fluents, delete_fluents in zip(action_add_effect_cnf.values(), action_delete_effect_cnf.values()):
            add_effects.update(add_fluents)
            delete_effects.update(delete_fluents)

        effect = Effect()
        effect.addlist = add_effects
        effect.dellist = delete_effects

        return Action(name=action_name, signature=self.learned_actions_signatures[action_name],
                      precondition=preconditions, effect=effect)

    def learn_action_model(self, trajectories: List[Trajectory]) -> Domain:
        """Learn the SAFE action model from the input trajectories.

        :param trajectories: the list of trajectories that are used to learn the safe action model.
        :return: a domain containing the actions that were learned.
        """
        self.logger.info("Starting to learn the action model!")
        for trajectory in trajectories:
            for component in trajectory:
                self.handle_single_trajectory_component(component)

        learned_actions = self.create_proxy_actions()
        all_actions = learned_actions.update(self.known_actions)
        self.learned_domain.actions = all_actions
        return self.learned_domain
