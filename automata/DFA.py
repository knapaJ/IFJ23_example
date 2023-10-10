from .AState import AutomataState
from .DFATransitionTable import TransitionTable
from typing import List, Mapping
from .InStream import InStream, EOF
from .AutomataExceptions import TransitionFaultException


class DeterministicFiniteAutomaton:
    def __init__(self,
                 begin_state: AutomataState,
                 transition_table: TransitionTable
                 ):
        self._state = begin_state
        self._transition_table = transition_table
        self._buffer: str = ""

    def run(self, instream: InStream) -> Token:
        while instream:
            char = instream.current_char
            try:
                new_state = self._transition_table.get_transition(self._state, char)
            except TransitionFaultException as e:
                if self._state.accepting:
                    return Token


