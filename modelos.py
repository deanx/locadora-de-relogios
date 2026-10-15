# modelos.py — entidades do domínio da locadora de relógios

class Relogio:
    """Um relógio disponível para aluguel."""

    codigo: str
    marca: str
    modelo: str
    diaria: float
    disponivel: bool

    def __init__(self, codigo: str, marca: str, modelo: str, diaria: float):
        self.codigo = codigo
        self.marca = marca
        self.modelo = modelo
        self.diaria = diaria
        self.disponivel = True

    def alugar(self) -> bool:
        if not self.disponivel:
            return False
        self.disponivel = False
        return True

    def devolver(self) -> None:
        self.disponivel = True

    def __str__(self) -> str:
        status = "livre" if self.disponivel else "alugado"
        return f"{self.codigo}: {self.marca} {self.modelo} — R$ {self.diaria:.2f}/dia ({status})"


class Estoque:
    """Coleção de relógios da locadora."""

    relogios: list[Relogio]

    def __init__(self):
        self.relogios = []

    def adiciona(self, relogio: Relogio) -> bool:
        if self.busca_por_codigo(relogio.codigo) is not None:
            return False
        self.relogios.append(relogio)
        return True

    def busca_por_codigo(self, codigo: str) -> Relogio | None:
        for relogio in self.relogios:
            if relogio.codigo == codigo:
                return relogio
        return None

    def disponiveis(self) -> list[Relogio]:
        return [r for r in self.relogios if r.disponivel]

    def __len__(self) -> int:
        return len(self.relogios)
