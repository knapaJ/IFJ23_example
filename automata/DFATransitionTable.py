from typing import Mapping, Dict
from .AState import AutomataState
from AutomataExceptions import DeterminismFaultException, TransitionFaultException


class TransitionTable:
    def __init__(self, table: Dict[AutomataState, Dict[str, AutomataState]]):
        if table is not None:
            self._transition_mapping: Dict[AutomataState, Dict[str, AutomataState]] = table
        else:
            self._transition_mapping: Dict[AutomataState, Dict[str, AutomataState]] = {}

    def add_transition(self, initial_state: AutomataState,
                       character: str,
                       new_state: AutomataState):
        if character == "":
            raise DeterminismFaultException("Epsilon transitions are prohibited in DFAs")
        if initial_state in self._transition_mapping and character in self._transition_mapping[initial_state]:
            raise DeterminismFaultException("Two transitions beginning in the same state can not accept "
                                            "the same character")
        self._transition_mapping[initial_state] = {character: new_state}

    def get_transition(self, current_state: AutomataState, character: str) -> AutomataState:
        if current_state not in self._transition_mapping:
            raise TransitionFaultException(f"No viable transition for state {current_state}")
        if character not in self._transition_mapping[current_state]:
            raise TransitionFaultException(f"No viable transition for state {current_state} and inpput character "
                                           f"'{character}'")
        return self._transition_mapping[current_state][character]

