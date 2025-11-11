from funciones.sumar_iriarte import sumar_iriarte

def test_sumar_iriarte():
    assert sumar_iriarte(2, 3) == 5
    assert sumar_iriarte(-1, 1) == 0
