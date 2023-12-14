
def _sum(a: int, b: int) -> int:
    if isinstance(a, int) and isinstance(b, int):
        return a + b
    raise TypeError("Operands must be integers")