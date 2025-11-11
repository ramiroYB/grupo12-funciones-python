from funciones.sumarguiza import sumarguiza

def test_sumarguiza():
    assert sumarguiza(3, 5) == 8
    assert sumarguiza(-2, 2) == 0
