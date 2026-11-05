import pytest
from models import Paczka
from services import Paczkomat


def test_nowa_paczka_ma_status_oczekuje_i_opis():
    paczka = Paczka("PAC-001", "Anna Kowalska", 2.5)
    assert paczka.status == "oczekuje"
    assert paczka.opis() == "PAC-001 | Anna Kowalska | 2.5 kg | oczekuje"


@pytest.mark.parametrize("waga", [0, -1, -0.5])
def test_niepoprawna_waga_rzuca_valueerror(waga):
    with pytest.raises(ValueError, match="waga"):
        Paczka("PAC-002", "Jan Nowak", waga)


def test_odbierz_zmienia_status_na_odebrana():
    paczka = Paczka("PAC-003", "Ewa Lis", 1.0)
    paczka.odbierz()
    assert paczka.status == "odebrana"


def test_drugie_odbierz_rzuca_valueerror():
    paczka = Paczka("PAC-004", "Ola Wrona", 1.2)
    paczka.odbierz()
    with pytest.raises(ValueError):
        paczka.odbierz()


def test_wstawienie_ponad_limit_rzuca_valueerror():
    paczkomat = Paczkomat(pojemnosc=2)
    paczkomat.wstaw(Paczka("A", "X", 1))
    paczkomat.wstaw(Paczka("B", "Y", 1))
    with pytest.raises(ValueError):
        paczkomat.wstaw(Paczka("C", "Z", 1))


def test_wstaw_i_odbierz_zwalnia_miejsce():
    paczkomat = Paczkomat(pojemnosc=3)
    paczkomat.wstaw(Paczka("PAC-010", "Adam Mak", 3.0))
    assert paczkomat.ile_wolnych() == 2

    odebrana = paczkomat.odbierz("PAC-010")

    assert paczkomat.ile_wolnych() == 3
    assert odebrana.status == "odebrana"


def test_duplikat_kodu_rzuca_valueerror():
    paczkomat = Paczkomat()
    paczkomat.wstaw(Paczka("PAC-020", "Ala Ma", 1))
    with pytest.raises(ValueError):
        paczkomat.wstaw(Paczka("PAC-020", "Ola Ma", 2))


def test_odbior_nieistniejacego_kodu_rzuca_valueerror():
    paczkomat = Paczkomat()
    with pytest.raises(ValueError):
        paczkomat.odbierz("BRAK")


@pytest.mark.parametrize("waga", [0.1, 2.5, 30])
def test_poprawne_wagi(waga):
    paczka = Paczka("PAC-099", "Test", waga)
    assert paczka.waga_kg == waga
