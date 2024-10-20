# test_fancy.py

import pytest

# Este es un test simple que siempre pasa
def test_always_passes():
    assert True

# Este es un test que verifica la suma de dos números
def test_sum():
    num1 = 3
    num2 = 4
    expected_result = 7
    assert num1 + num2 == expected_result

# Este es un test parametrizado para verificar diferentes resultados de suma
@pytest.mark.parametrize("a, b, result", [
    (1, 2, 3),
    (2, 2, 4),
    (5, 5, 10),
    (0, 0, 0)
])
def test_parametrized_sum(a, b, result):
    assert a + b == result

# Un test para comprobar que una lista contiene un elemento específico
def test_list_contains():
    fruits = ["apple", "banana", "cherry"]
    assert "banana" in fruits

# Un test para comprobar que una excepción se lanza
def test_raises_exception():
    with pytest.raises(ZeroDivisionError):
        1 / 0
