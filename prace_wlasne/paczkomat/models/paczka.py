class Paczka:
    def __init__(self, kod: str, adresat: str, waga_kg: float) -> None:
        if waga_kg <= 0:
            raise ValueError("Nieprawidłowa waga: musi być większa od zera")
        self.kod = kod
        self.adresat = adresat
        self.waga_kg = waga_kg
        self.status = "oczekuje"

    def odbierz(self) -> None:
        if self.status != "oczekuje":
            raise ValueError(
                f"Nie można odebrać paczki {self.kod} o statusie '{self.status}'"
            )
        self.status = "odebrana"

    def zwroc(self) -> None:
        if self.status != "oczekuje":
            raise ValueError(
                f"Nie można zwrócić paczki {self.kod} o statusie '{self.status}'"
            )
        self.status = "zwrocona"

    def opis(self) -> str:
        return f"{self.kod} | {self.adresat} | {self.waga_kg} kg | {self.status}"
