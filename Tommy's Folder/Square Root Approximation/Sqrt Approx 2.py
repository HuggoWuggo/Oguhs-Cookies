import math

SQRT_CONSTANT: int = 3131
last_approximation: float = 0
perfect_square: int = 1
TRUE_VALUE: float = math.sqrt(SQRT_CONSTANT)
print(f'{TRUE_VALUE = }\n')

while perfect_square ** 2 < SQRT_CONSTANT:
    perfect_square += 1

approximation: float = perfect_square

while approximation != last_approximation:
    last_approximation = approximation
    approximation = 0.5 * (approximation + SQRT_CONSTANT / approximation)
    difference: float = abs(TRUE_VALUE - approximation)
    print(f'Approx: {approximation:.16f}, Diff: {difference:.20f}, Per Cent: {difference / approximation * 100:.20f}')