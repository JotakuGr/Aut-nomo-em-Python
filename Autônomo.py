# afd_linguagem.py
def criar_automato_linguagem():
    # Estados
    estados = {'q0', 'q1', 'q2', 'qF', 'qd'}

    # Alfabeto
    alfabeto = {'a', 'b', 'c'}

    # Função de transição (delta) como dicionário (estado, símbolo) -> novo_estado
    transicoes = {
        # q0
        ('q0', 'a'): 'q1',
        ('q0', 'b'): 'qd',
        ('q0', 'c'): 'qd',
        # q1 (já começou com a, aguardando primeiro c)
        ('q1', 'a'): 'q1',
        ('q1', 'b'): 'q1',
        ('q1', 'c'): 'q2',
        # q2 (já vimos um c; último símbolo != b)
        ('q2', 'a'): 'q2',
        ('q2', 'c'): 'q2',
        ('q2', 'b'): 'qF',
        # qF (já vimos c e o último símbolo lido é b) - aceitação se terminar aqui
        ('qF', 'b'): 'qF',
        ('qF', 'a'): 'q2',
        ('qF', 'c'): 'q2',
        # qd (morto)
        ('qd', 'a'): 'qd',
        ('qd', 'b'): 'qd',
        ('qd', 'c'): 'qd',
    }

    estado_inicial = 'q0'
    estados_finais = {'qF'}

    return estados, alfabeto, transicoes, estado_inicial, estados_finais

def simular_cadeia(cadeia, automato, mostrar_passos=False):
    estados, alfabeto, transicoes, estado_inicial, estados_finais = automato
    estado_atual = estado_inicial

    if mostrar_passos:
        print(f"Estado inicial: {estado_atual}")

    for i, simbolo in enumerate(cadeia, start=1):
        if simbolo not in alfabeto:
            # símbolo inválido para o alfabeto
            if mostrar_passos:
                print(f"Símbolo inválido '{simbolo}' na posição {i}. Rejeitado.")
            return False, estado_atual
        # obtenha transição ou vá para estado morto se undefined (mas aqui já temos todas)
        estado_atual = transicoes.get((estado_atual, simbolo), 'qd')
        if mostrar_passos:
            print(f" Lê '{simbolo}' -> {estado_atual}")

    aceito = estado_atual in estados_finais
    if mostrar_passos:
        print(f"Estado final: {estado_atual} -> {'ACEITA' if aceito else 'REJEITADA'}")
    return aceito, estado_atual

def teste_cadeias(automato, cadeias, mostrar_passos=False):
    for s in cadeias:
        aceito, estado_final = simular_cadeia(s, automato, mostrar_passos=mostrar_passos)
        print(f"Cadeia '{s}': {'ACEITA' if aceito else 'REJEITADA'} (estado final: {estado_final})")

if __name__ == "__main__":
    automato = criar_automato_linguagem()

    # Leitura opcional do usuário
    entrada = input("Digite uma cadeia sobre {a,b,c} (ou pressione Enter para pular): ").strip()
    if entrada != "":
        aceito, estado_final = simular_cadeia(entrada, automato, mostrar_passos=True)
        print(f"Resultado: {'ACEITA' if aceito else 'REJEITADA'}\n")

    # Testes: todas as cadeias fornecidas na Fase 1
    cadeias_aceitas = ["acb", "accb", "aacb", "abcb", "acbb", "abacb", "abccab"]
    cadeias_rejeitadas = ["ab", "cab", "ac"]

    print("=== Testando cadeias que deveriam ser ACEITAS ===")
    teste_cadeias(automato, cadeias_aceitas)

    print("\n=== Testando cadeias que deveriam ser REJEITADAS ===")
    teste_cadeias(automato, cadeias_rejeitadas)
