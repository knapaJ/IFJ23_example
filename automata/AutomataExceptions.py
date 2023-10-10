class DeterminismFaultException(Exception):
    """Značí, že při vytváření DKA došlo k porušení determinismu."""
    def __init__(self, *args):
        super().__init__(*args)


class TransitionFaultException(Exception):
    """Nebyl nalezen žádný přechod v DKA odpovídající aktuální konfiguraci a vstupnímu znaku"""
    def __init__(self, *args):
        super().__init__(*args)