def add(a: float, b: float) -> float:
    """Retourne la somme de a et b."""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("a et b doivent être des nombres")
    return a + b