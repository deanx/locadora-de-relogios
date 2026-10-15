# importa.py — carrega o estoque a partir do arquivo CSV

from modelos import Estoque, Relogio


def carrega_estoque(caminho: str) -> Estoque:
    """Lê o CSV e devolve um Estoque populado.
    Formato de cada linha: codigo,marca,modelo,diaria
    """
    estoque = Estoque()

    try:
        with open(caminho, "r", encoding="utf-8") as arquivo:
            for numero, linha in enumerate(arquivo, start=1):
                linha_limpa = linha.strip()
                if not linha_limpa:
                    continue

                partes = linha_limpa.split(",")
                if len(partes) != 4:
                    print(f"[AVISO] Linha {numero} ignorada: formato invalido.")
                    continue

                try:
                    codigo = partes[0].strip()
                    marca = partes[1].strip()
                    modelo = partes[2].strip()
                    diaria = float(partes[3])
                    estoque.adiciona(Relogio(codigo, marca, modelo, diaria))
                except ValueError:
                    print(f"[AVISO] Linha {numero} ignorada: diaria invalida.")
                    continue

    except FileNotFoundError:
        print(f"[ERRO] Arquivo '{caminho}' nao encontrado.")

    return estoque
