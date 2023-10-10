from typing import Self


class AutomataState:
    def __init__(self, name: str, accepting: bool = False, token_type: TokenType | None = None):
        self._name = name
        self.accepting = accepting
        if accepting and not token_type:
            raise ValueError('Can not have an accepting state that does not specify token type')
        self.token_type = token_type

    def __eq__(self, other: Self) -> bool:
        if type(self) is not type(other):
            raise ValueError(f"Can not compare {type(self)} with {type(other)}.")
        if self._name == other._name:
            return True
        return False

    def __hash__(self):
        return hash(self._name)

    def __repr__(self):
        return f"AutomataState({self._name})"
