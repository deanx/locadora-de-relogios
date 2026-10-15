# locadora.py — programa principal da locadora de relogios

from importa import carrega_estoque


def mostra_menu() -> None:
    print()
    print("=== LOCADORA DE RELOGIOS ===")
    print("  [1] Listar relogios")
    print("  [2] Buscar por codigo")
    print("  [3] Alugar relogio")
    print("  [4] Devolver relogio")
    print("  [0] Sair")


def main() -> None:
    estoque = carrega_estoque("relogios.csv")
    print(f"Estoque carregado: {len(estoque)} relogios.")

    while True:
        mostra_menu()
        opcao = input("Opcao: ").strip()

        if opcao == "1":
            if len(estoque) == 0:
                print("(estoque vazio)")
            else:
                for numero, relogio in enumerate(estoque.relogios, start=1):
                    print(f"  {numero}. {relogio}")

        elif opcao == "2":
            codigo = input("Codigo: ").strip().upper()
            encontrado = estoque.busca_por_codigo(codigo)
            if encontrado is None:
                print(f"Codigo {codigo} nao encontrado.")
            else:
                print(encontrado)

        elif opcao == "3":
            codigo = input("Codigo do relogio: ").strip().upper()
            relogio = estoque.busca_por_codigo(codigo)
            if relogio is None:
                print("Relogio nao encontrado.")
            elif relogio.alugar():
                print(f"Alugado: {relogio.marca} {relogio.modelo}")
            else:
                print("Relogio ja esta alugado.")

        elif opcao == "4":
            codigo = input("Codigo do relogio: ").strip().upper()
            relogio = estoque.busca_por_codigo(codigo)
            if relogio is None:
                print("Relogio nao encontrado.")
            else:
                relogio.devolver()
                print(f"Devolvido: {relogio.marca} {relogio.modelo}")

        elif opcao == "0":
            print("Ate logo!")
            break

        else:
            print(f"Opcao '{opcao}' invalida.")


if __name__ == "__main__":
    main()
