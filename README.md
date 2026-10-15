# Locadora de Relógios

Um pequeno sistema de linha de comando para gerenciar o aluguel de
relógios. Projeto simples, feito em Python puro (só biblioteca padrão),
pensado para servir de exercício de leitura e contribuição.

## Como rodar

Requer Python 3.10 ou superior.

    git clone https://github.com/deanx/locadora-de-relogios.git
    cd locadora-de-relogios
    python locadora.py

Não há dependências externas — roda direto, sem instalar nada.

## Como usar

O programa abre um menu interativo:

    === LOCADORA DE RELOGIOS ===
      [1] Listar relogios
      [2] Buscar por codigo
      [3] Alugar relogio
      [4] Devolver relogio
      [0] Sair

Digite o número da opção e siga as instruções.

## Estrutura

- `modelos.py` — as classes `Relogio` e `Estoque`.
- `importa.py` — carrega o estoque a partir de `relogios.csv`.
- `locadora.py` — o programa principal (menu).
- `relogios.csv` — os dados iniciais dos relógios.

## Contribuindo

Contribuições são bem-vindas! Veja as *issues* abertas — algumas são
marcadas como `good first issue`, ideais para quem está começando.

O fluxo é o padrão do GitHub: faça um fork, crie uma branch para sua
mudança, e abra um Pull Request.

## Licença

MIT — veja o arquivo `LICENSE`.
