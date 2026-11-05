from models import Paczka


class Paczkomat:
    def __init__(self, pojemnosc: int = 3) -> None:
        self.pojemnosc = pojemnosc
        self.skrytki: list[Paczka] = []

    def wstaw(self, paczka: Paczka) -> None:
        if self.ile_wolnych() <= 0:
            raise ValueError("Brak wolnych skrytek")
        if any(p.kod == paczka.kod for p in self.skrytki):
            raise ValueError(f"Paczka o kodzie {paczka.kod} już jest w paczkomacie")
        self.skrytki.append(paczka)

    def odbierz(self, kod: str) -> Paczka:
        for paczka in self.skrytki:
            if paczka.kod == kod:
                paczka.odbierz()
                self.skrytki.remove(paczka)
                return paczka
        raise ValueError(f"Brak paczki o kodzie {kod}")

    def ile_wolnych(self) -> int:
        return self.pojemnosc - len(self.skrytki)

    def lista_oczekujacych(self) -> list[Paczka]:
        return [p for p in self.skrytki if p.status == "oczekuje"]
