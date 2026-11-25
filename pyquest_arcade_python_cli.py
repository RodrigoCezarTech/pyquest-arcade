"""
PyQuest Arcade — Versao Terminal em Python.

Executa os 25 casos de codigo Python e analise de dados (df_, read_csv, read_json)
com pontuacao, bonus de velocidade, dica opcional e placar final.
"""
import random
import time
from typing import Any


CASOS_PYTHON: list[dict[str, Any]] = [
    {
        "id": 1,
        "personagem": "Terturiano",
        "tema": "if / else",
        "titulo": "Parada Cardiaca com Adrenalina",
        "historia": (
            "Terturiano monitora um paciente com batimentos zerados (bpm == 0). "
            "Se nao houver pulso, ele precisa aplicar 'adrenalina' imediatamente!"
        ),
        "codigo": [
            "bpm = 0",
            "if bpm == 0:",
            "    acao = ___",
            "else:",
            '    acao = "monitorar"',
        ],
        "opcoes": [
            '"adrenalina"',
            "adrenalina()",
            'print("adrenalina")',
            'bpm = "adrenalina"',
        ],
        "correta": 0,
        "dica": "Quando bpm == 0, a resposta certa e uma string entre aspas com o nome do medicamento.",
        "explicacao": "Como a condicao verifica bpm == 0, atribuimos a string 'adrenalina' a variavel acao.",
    },
    {
        "id": 2,
        "personagem": "Alipio",
        "tema": "else",
        "titulo": "Alipio e o Guarda-Chuva",
        "historia": (
            "Alipio olhou para o ceu: esta chovendo! Se chover, ele leva 'guarda-chuva'; "
            "senao (else), leva 'oculos_escuros'."
        ),
        "codigo": [
            "chovendo = True",
            "if chovendo:",
            '    item = "guarda-chuva"',
            "___:",
            '    item = "oculos_escuros"',
        ],
        "opcoes": ["else", "elif", "senao", "default"],
        "correta": 0,
        "dica": "A propria historia ja cita a palavra em ingles para 'senao' quando o if nao executa.",
        "explicacao": "Em Python, o bloco alternativo quando o if e falso usa a palavra reservada else:.",
    },
    {
        "id": 3,
        "personagem": "Tiburcio",
        "tema": "read_json",
        "titulo": "Tiburcio precisa ler um arquivo JSON",
        "historia": (
            "Tiburcio recebeu o arquivo 'dados_tiburcio.json' estruturado em JSON. "
            "Qual comando do pandas le JSON corretamente?"
        ),
        "dados": [
            {"chave": "analista", "valor": '"Tiburcio"', "tipo": "str"},
            {"chave": "registros", "valor": "1420", "tipo": "int"},
            {"chave": "valido", "valor": "true", "tipo": "bool"},
        ],
        "codigo": [
            "import pandas as pd",
            'caminho = "dados_tiburcio.json"',
            "df_tiburcio = ___ (caminho)",
        ],
        "opcoes": [
            "pd.read_json",
            "pd.read_csv",
            "pd.open_json",
            "json.read_csv",
        ],
        "correta": 0,
        "dica": "O arquivo termina em .json e o prefixo do pandas e pd.read_...",
        "explicacao": "Para ler arquivos JSON com pandas, usamos pd.read_json(caminho).",
    },
    {
        "id": 4,
        "personagem": "Amnesio",
        "tema": "read_csv",
        "titulo": "Amnesio precisa estruturar os dados CSV",
        "historia": (
            "Amnesio encontrou uma tabela separada por virgulas ('inventario_amnesio.csv') "
            "e quer carrega-la em um DataFrame estruturado df_amnesio."
        ),
        "dados": [
            {"id": "101", "setor": "Norte", "qtd": "48"},
            {"id": "102", "setor": "Sul", "qtd": "95"},
            {"id": "103", "setor": "Leste", "qtd": "72"},
        ],
        "codigo": [
            "import pandas as pd",
            'arquivo = "inventario_amnesio.csv"',
            "df_amnesio = ___ (arquivo)",
        ],
        "opcoes": [
            "pd.read_csv",
            "pd.read_json",
            "pd.struct_csv",
            "csv.dataframe",
        ],
        "correta": 0,
        "dica": "Qual funcao do pandas le arquivos com extensao .csv para criar um DataFrame?",
        "explicacao": "O comando pd.read_csv(arquivo) le dados separados por virgula e os estrutura em DataFrame.",
    },
    {
        "id": 5,
        "personagem": "Tiburcio",
        "tema": "df_.head()",
        "titulo": "Inspecionando as 5 Primeiras Linhas de df_vendas",
        "historia": (
            "Tiburcio carregou o DataFrame df_vendas com 50 mil linhas e quer visualizar "
            "as primeiras linhas para conferir as colunas."
        ),
        "dados": [
            {"mes": "Jan", "loja": "SP", "receita": "18400"},
            {"mes": "Fev", "loja": "RJ", "receita": "21900"},
            {"mes": "Mar", "loja": "MG", "receita": "15300"},
        ],
        "codigo": [
            "primeiras = df_vendas.___()",
            "print(primeiras)",
        ],
        "opcoes": ["head", "top5", "first", "start"],
        "correta": 0,
        "dica": "Em ingles, 'cabeca / topo' de uma tabela DataFrame e chamado de head().",
        "explicacao": "O metodo df_vendas.head() retorna por padrao as 5 primeiras linhas de um DataFrame.",
    },
    {
        "id": 6,
        "personagem": "Genoveva",
        "tema": "df_.dropna()",
        "titulo": "Limpando Valores Nulos (NaN) em df_amostras",
        "historia": (
            "Na analise de laboratorio de Genoveva, varias medicoes vieram vazias (NaN). "
            "Ela precisa remover as linhas com valores ausentes de df_amostras."
        ),
        "dados": [
            {"tubo": "A1", "ph": "7.1", "pureza": "98%"},
            {"tubo": "A2", "ph": "NaN", "pureza": "94%"},
            {"tubo": "A3", "ph": "6.8", "pureza": "NaN"},
        ],
        "codigo": [
            "df_limpo = df_amostras.___()",
            "print(len(df_limpo))",
        ],
        "opcoes": ["dropna", "remove_null", "clean_nan", "drop_empty"],
        "correta": 0,
        "dica": "O nome do metodo junta 'drop' (descartar) com 'na' (valores ausentes).",
        "explicacao": "Em pandas, df_amostras.dropna() descarta todas as linhas que contem valores nulos (NaN).",
    },
    {
        "id": 7,
        "personagem": "Amnesio",
        "tema": "df_.groupby()",
        "titulo": "Agrupando Estoque por Setor em df_estoque",
        "historia": (
            "Amnesio precisa somar a quantidade total de itens agrupando o DataFrame "
            "df_estoque pela coluna 'setor'."
        ),
        "dados": [
            {"setor": "Norte", "itens": "120", "status": "OK"},
            {"setor": "Sul", "itens": "85", "status": "Baixo"},
            {"setor": "Leste", "itens": "140", "status": "OK"},
        ],
        "codigo": [
            'resumo = df_estoque.___("setor")["qtd"].sum()',
            "print(resumo)",
        ],
        "opcoes": ["groupby", "group_by", "cluster", "splitby"],
        "correta": 0,
        "dica": "No pandas, o metodo de agrupamento escreve-se tudo junto: groupby.",
        "explicacao": 'O metodo df_estoque.groupby("setor") agrupa os registros por categoria antes de aplicar .sum().',
    },
    {
        "id": 8,
        "personagem": "Alipio",
        "tema": "df_.describe()",
        "titulo": "Resumo Estatistico Rapido de df_clima",
        "historia": (
            "Alipio quer calcular de uma so vez media, desvio padrao, minimo e maximo "
            "das temperaturas registradas em df_clima."
        ),
        "dados": [
            {"metrica": "media", "temp_c": "24.6C", "umidade": "71%"},
            {"metrica": "minimo", "temp_c": "16.0C", "umidade": "45%"},
            {"metrica": "maximo", "temp_c": "33.2C", "umidade": "92%"},
        ],
        "codigo": [
            "estatisticas = df_clima.___()",
            "print(estatisticas)",
        ],
        "opcoes": ["describe", "stats", "summary", "analyze"],
        "correta": 0,
        "dica": "Qual metodo em ingles 'descreve' estatisticamente todas as colunas numericas de um DataFrame?",
        "explicacao": "df_clima.describe() gera automaticamente contagem, media, desvio padrao, minimo e maximo.",
    },
    {
        "id": 9,
        "personagem": "Genesio",
        "tema": "print()",
        "titulo": "Painel de Ignicao do Foguete",
        "historia": (
            "Genesio esta na cabine e precisa exibir 'DECOLAR!' no terminal de controle "
            "para confirmar a ignicao."
        ),
        "codigo": [
            'status = "DECOLAR!"',
            "___ (status)",
        ],
        "opcoes": ["print", "show", "echo", "write"],
        "correta": 0,
        "dica": "E a funcao classica do Python para mostrar texto no console.",
        "explicacao": "A funcao padrao do Python para imprimir valores na tela e print().",
    },
    {
        "id": 10,
        "personagem": "Terturiano",
        "tema": "for / range",
        "titulo": "Ciclo de Compressoes de Emergencia",
        "historia": (
            "Para manter o ritmo, Terturiano programou um laco que repete exatamente "
            "3 vezes a contagem de compressoes."
        ),
        "codigo": [
            "for pulso in ___:",
            '    print("Compressao", pulso)',
        ],
        "opcoes": ["range(3)", "loop(3)", "repeat(3)", "3.times"],
        "correta": 0,
        "dica": "Em Python, geramos uma sequencia numerica de 3 passos com range(...).",
        "explicacao": "range(3) gera a sequencia 0, 1, 2 para executar o bloco 3 vezes no for.",
    },
    {
        "id": 11,
        "personagem": "Eber",
        "tema": "and",
        "titulo": "Dupla Trava de Seguranca do Eber",
        "historia": (
            "O cofre de Eber so abre se o cracha for valido E o PIN estiver correto "
            "ao mesmo tempo."
        ),
        "codigo": [
            "cracha_ok = True",
            "pin_ok = True",
            "if cracha_ok ___ pin_ok:",
            "    cofre_aberto = True",
        ],
        "opcoes": ["and", "or", "not", "&"],
        "correta": 0,
        "dica": "Traduza 'E' ao mesmo tempo para a palavra-chave booleana do Python.",
        "explicacao": "O operador logico and exige que ambas as condicoes sejam verdadeiras.",
    },
    {
        "id": 12,
        "personagem": "Genoveva",
        "tema": "list.append()",
        "titulo": "Adicionando Reagente na Lista",
        "historia": (
            'Genoveva criou a lista amostras = ["agua"] e quer adicionar "ferro" '
            "no final da lista."
        ),
        "codigo": [
            'amostras = ["agua"]',
            'amostras.___("ferro")',
        ],
        "opcoes": ["append", "push", "add_end", "insert_last"],
        "correta": 0,
        "dica": "Qual metodo de lista em Python anexa um elemento ao final?",
        "explicacao": "O metodo .append() adiciona um novo item ao final de uma lista em Python.",
    },
    {
        "id": 13,
        "personagem": "Percival",
        "tema": "dict",
        "titulo": "Dicionario de Tipos Sanguineos",
        "historia": (
            "Percival guardou os tipos sanguineos em um dicionario e quer acessar "
            'a chave "O+".'
        ),
        "codigo": [
            'sangue = {"O+": 12, "A-": 4}',
            "qtd = sangue[___]",
        ],
        "opcoes": ['"O+"', 'key("O+")', '.get("O+")', "O+"],
        "correta": 0,
        "dica": "A chave no dicionario e uma string exata que representa o tipo sanguineo.",
        "explicacao": 'Consultamos o valor de uma chave em um dicionario usando colchetes: sangue["O+"].',
    },
    {
        "id": 14,
        "personagem": "Francisnaldo",
        "tema": "while",
        "titulo": "Submersao ate a Profundidade Alvo",
        "historia": (
            "O submarino de Francisnaldo desce enquanto a profundidade atual for "
            "menor que 200 metros."
        ),
        "codigo": [
            "profundidade = 0",
            "___ profundidade < 200:",
            "    profundidade += 50",
        ],
        "opcoes": ["while", "until", "when", "repeat"],
        "correta": 0,
        "dica": "Qual comando repete o laco 'enquanto' uma condicao for verdadeira?",
        "explicacao": "O laco while repete o bloco enquanto a condicao profundidade < 200 for verdadeira.",
    },
    {
        "id": 15,
        "personagem": "Genoveva",
        "tema": "def",
        "titulo": "Declarando Funcao de Calculo",
        "historia": (
            "Genoveva quer definir uma funcao chamada calcular_dose que recebe "
            "o peso do paciente."
        ),
        "codigo": [
            "___ calcular_dose(peso):",
            "    return peso * 2",
        ],
        "opcoes": ["def", "function", "func", "criar"],
        "correta": 0,
        "dica": "E a palavra curta (3 letras) usada em Python para definir uma funcao.",
        "explicacao": "Em Python, funcoes sao declaradas com a palavra-chave def.",
    },
    {
        "id": 16,
        "personagem": "Percival",
        "tema": "try / except",
        "titulo": "Protecao contra Divisao por Zero",
        "historia": (
            "Percival tenta dividir energia por um sensor que pode valer zero "
            "sem derrubar o programa."
        ),
        "codigo": [
            "try:",
            "    taxa = 100 / sensor",
            "___ ZeroDivisionError:",
            "    taxa = 0",
        ],
        "opcoes": ["except", "catch", "rescue", "error"],
        "correta": 0,
        "dica": "Apos try:, o bloco que trata o erro em Python comeca com qual palavra?",
        "explicacao": "Para capturar excecoes em Python, usamos try: junto com except ...:.",
    },
    {
        "id": 17,
        "personagem": "Tibúrcio",
        "tema": "df_.shape",
        "titulo": "Dimensoes da Tabela df_log",
        "historia": (
            "Tibúrcio quer verificar rapidamente quantas linhas e colunas possui "
            "o DataFrame df_log."
        ),
        "dados": [
            {"evento": "login", "ip": "10.0.0.1", "ok": "True"},
            {"evento": "query", "ip": "10.0.0.2", "ok": "True"},
        ],
        "codigo": [
            "linhas, colunas = df_log.___",
            "print(linhas, colunas)",
        ],
        "opcoes": ["shape", "size_xy", "dims()", "count_rc"],
        "correta": 0,
        "dica": "E um atributo (sem parenteses) que retorna uma tupla (linhas, colunas).",
        "explicacao": "O atributo df_log.shape retorna uma tupla (numero_de_linhas, numero_de_colunas).",
    },
    {
        "id": 18,
        "personagem": "Amnésio",
        "tema": "df_.sort_values()",
        "titulo": "Ordenando df_ranking por Pontos",
        "historia": (
            "Amnésio quer ordenar o DataFrame df_ranking de acordo com os valores "
            "da coluna 'pontos'."
        ),
        "dados": [
            {"jogador": "Ana", "pontos": "900"},
            {"jogador": "Beto", "pontos": "1450"},
            {"jogador": "Caio", "pontos": "1100"},
        ],
        "codigo": [
            'ordenado = df_ranking.___("pontos", ascending=False)',
            "print(ordenado)",
        ],
        "opcoes": ["sort_values", "order_by", "sort_df", "rank_values"],
        "correta": 0,
        "dica": "No pandas, ordenamos um DataFrame pelos valores de uma coluna com sort_values.",
        "explicacao": 'df_ranking.sort_values("pontos", ascending=False) ordena do maior para o menor.',
    },
    {
        "id": 19,
        "personagem": "Eber",
        "tema": "len()",
        "titulo": "Contando Pacotes Interceptados",
        "historia": (
            "Eber armazenou os pacotes recebidos na lista pacotes e precisa saber "
            "quantos elementos existem nela."
        ),
        "codigo": [
            'pacotes = ["pkt1", "pkt2", "pkt3", "pkt4"]',
            "total = ___(pacotes)",
            "print(total)",
        ],
        "opcoes": ["len", "count", "size", "length"],
        "correta": 0,
        "dica": "E a funcao embutida do Python que retorna o tamanho de listas, strings ou colecoes.",
        "explicacao": "A funcao len(pacotes) retorna a quantidade total de itens na lista.",
    },
    {
        "id": 20,
        "personagem": "Francisnaldo",
        "tema": "elif",
        "titulo": "Faixas de Pressao no Sonar",
        "historia": (
            "Francisnaldo verifica se a pressao e 'alta'; se nao for, testa uma "
            "segunda condicao intermediaria 'media' antes do else."
        ),
        "codigo": [
            'if pressao == "alta":',
            '    alerta = "VERMELHO"',
            '___ pressao == "media":',
            '    alerta = "AMARELO"',
            "else:",
            '    alerta = "VERDE"',
        ],
        "opcoes": ["elif", "else if", "elseif", "when"],
        "correta": 0,
        "dica": "Em Python, 'senao se' escreve-se junto em quatro letras: elif.",
        "explicacao": "Usamos elif para adicionar condicoes intermediarias apos um if inicial.",
    },
    {
        "id": 21,
        "personagem": "Antéria",
        "tema": "str.upper()",
        "titulo": "Padronizando Codigos de Satelite com Antéria",
        "historia": (
            "Antéria recebeu o sinal 'sat_alfa' em letras minusculas e precisa "
            "converte-lo todo para MAIUSCULAS."
        ),
        "codigo": [
            'sinal = "sat_alfa"',
            "codigo = sinal.___()",
            "print(codigo)",
        ],
        "opcoes": ["upper", "capitalize", "to_upper", "caps"],
        "correta": 0,
        "dica": "Em ingles, letras maiusculas sao chamadas de 'upper case'.",
        "explicacao": "O metodo .upper() retorna uma nova string com todos os caracteres em maiusculas.",
    },
    {
        "id": 22,
        "personagem": "Girúndia",
        "tema": "sum()",
        "titulo": "Total de Pecas na Linha da Girúndia",
        "historia": (
            "Girúndia registrou os lotes produzidos na lista lotes = [12, 18, 25] "
            "e precisa somar todos os valores rapidamente."
        ),
        "codigo": [
            "lotes = [12, 18, 25]",
            "total = ___(lotes)",
            "print(total)",
        ],
        "opcoes": ["sum", "total", "add_all", "count"],
        "correta": 0,
        "dica": "E a funcao nativa de 3 letras do Python para somar os itens de uma lista.",
        "explicacao": "A funcao embutida sum(lotes) calcula a soma de todos os elementos da lista.",
    },
    {
        "id": 23,
        "personagem": "Arcídia",
        "tema": "return",
        "titulo": "Devolvendo o Resultado da Funcao da Arcídia",
        "historia": (
            "Arcídia escreveu uma funcao para calcular o dobro de uma chave, "
            "mas esqueceu a palavra que devolve o valor."
        ),
        "codigo": [
            "def dobrar(valor):",
            "    ___ valor * 2",
        ],
        "opcoes": ["return", "yields", "output", "send"],
        "correta": 0,
        "dica": "Qual palavra reservada encerra a funcao e retorna um resultado para quem a chamou?",
        "explicacao": "Usamos return para devolver o resultado calculado dentro de uma funcao em Python.",
    },
    {
        "id": 24,
        "personagem": "Esmeraldina",
        "tema": "df_.columns",
        "titulo": "Listando Nomes das Colunas de df_gemas",
        "historia": (
            "Esmeraldina abriu a tabela df_gemas e quer inspecionar os nomes "
            "de todas as colunas disponiveis."
        ),
        "dados": [
            {"pedra": "Esmeralda", "quilates": "4.2", "origem": "BA"},
            {"pedra": "Safira", "quilates": "3.1", "origem": "MG"},
            {"pedra": "Rubi", "quilates": "2.8", "origem": "GO"},
        ],
        "codigo": [
            "nomes_colunas = df_gemas.___",
            "print(nomes_colunas)",
        ],
        "opcoes": ["columns", "headers", "cols()", "fields"],
        "correta": 0,
        "dica": "E um atributo (sem parenteses) do DataFrame que guarda o indice de colunas.",
        "explicacao": "O atributo df_gemas.columns retorna os rotulos das colunas do DataFrame.",
    },
    {
        "id": 25,
        "personagem": "Porfília",
        "tema": "in",
        "titulo": "Rastreando Suspeito na Lista da Porfília",
        "historia": (
            "Porfília quer verificar se o codigo 'X99' esta presente dentro "
            "da lista de registros suspeitos."
        ),
        "codigo": [
            'suspeitos = ["A12", "X99", "B04"]',
            'if "X99" ___ suspeitos:',
            '    print("Alerta encontrado!")',
        ],
        "opcoes": ["in", "has", "inside", "contains"],
        "correta": 0,
        "dica": "Qual operador de 2 letras verifica pertinencia ('esta em') dentro de uma lista Python?",
        "explicacao": "O operador in verifica se um elemento pertence a uma lista, tupla, string ou dicionario.",
    },
]


def exibir_previa_dados(linhas: list[dict[str, str]]) -> None:
    """Imprime uma pequena tabela de amostra de dados no terminal."""
    if not linhas:
        return
    colunas = list(linhas[0].keys())
    larguras = {
        col: max(len(col), *(len(str(linha.get(col, ""))) for linha in linhas))
        for col in colunas
    }
    cabecalho = " | ".join(col.ljust(larguras[col]) for col in colunas)
    separador = "-+-".join("-" * larguras[col] for col in colunas)
    print("\n  [Previa de Dados]")
    print("  " + cabecalho)
    print("  " + separador)
    for linha in linhas:
        print("  " + " | ".join(str(linha.get(col, "")).ljust(larguras[col]) for col in colunas))


def jogar_pyquest() -> None:
    """Executa o loop principal do jogo no terminal com os 25 casos em ordem aleatoria."""
    print("=" * 64)
    print("           PYQUEST ARCADE — TREINO PYTHON (TERMINAL)")
    print("=" * 64)
    nome = input("Digite seu nome de jogador: ").strip() or "Jogador"
    print(f"\nBem-vindo, {nome}! Responda com 1-4 ou digite 'dica' (-100 pts).\n")

    pontuacao = 0
    sequencia = 0
    acertos = 0
    casos_sorteados = list(CASOS_PYTHON)
    random.shuffle(casos_sorteados)

    for idx, caso in enumerate(casos_sorteados, start=1):
        print("-" * 64)
        print(f"Questao {idx}/{len(casos_sorteados)} | Personagem: {caso['personagem']} | Tema: {caso['tema']}")
        print(f"Caso: {caso['titulo']}")
        print(f"Historia: {caso['historia']}")

        if "dados" in caso:
            exibir_previa_dados(caso["dados"])

        print("\n  [Codigo Python]")
        for num_linha, linha in enumerate(caso["codigo"], start=1):
            print(f"  {num_linha:2d} | {linha}")

        opcoes_embaralhadas = list(caso["opcoes"])
        correta_texto = caso["opcoes"][caso["correta"]]
        random.shuffle(opcoes_embaralhadas)
        indice_correto_rodada = opcoes_embaralhadas.index(correta_texto)

        print("\n  Opcoes:")
        for i, op in enumerate(opcoes_embaralhadas, start=1):
            print(f"    [{i}] {op}")

        inicio = time.monotonic()
        escolha_idx = -1

        while True:
            try:
                resposta = input("\nSua escolha (1-4 ou 'dica'): ").strip().lower()
            except (EOFError, KeyboardInterrupt):
                print("\nJogo encerrado pelo usuario.")
                return

            if resposta == "dica":
                pontuacao = max(0, pontuacao - 100)
                print(f"  >>> Dica (-100 pts | Pontos atuais: {pontuacao}): {caso['dica']}")
                continue

            if resposta in {"1", "2", "3", "4"}:
                escolha_idx = int(resposta) - 1
                break

            print("  Entrada invalida. Digite 1, 2, 3, 4 ou 'dica'.")

        decorrido = time.monotonic() - inicio
        if escolha_idx == indice_correto_rodada:
            acertos += 1
            sequencia += 1
            bonus_tempo = max(0, int((20 - decorrido) * 20))
            bonus_combo = (sequencia - 1) * 100
            ganho = 500 + bonus_tempo + bonus_combo
            pontuacao += ganho
            print(f"\n  [CORRETO!] +{ganho} pts (Combo: {sequencia}x | Total: {pontuacao} pts)")
        else:
            sequencia = 0
            print(f"\n  [INCORRETO] Resposta correta: {correta_texto} (Total: {pontuacao} pts)")

        print(f"  Explicacao: {caso['explicacao']}")

    print("\n" + "=" * 64)
    print(f"FIM DE JOGO — {nome}")
    print(f"Acertos: {acertos}/{len(casos_sorteados)} | Pontuacao Final: {pontuacao} pts")
    print("=" * 64)


if __name__ == "__main__":
    jogar_pyquest()