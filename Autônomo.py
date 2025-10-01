# afd_qF.py
# AFD que reconhece L = { w in {a,b,c}* | w começa com 'a', contém >=1 'c' e termina com 'b' }
# qF Estado final 

from typing import Set

# Estados
Q = {"q0", "q1", "q2", "qF", "qd"}
Sigma = {"a", "b", "c"}
q0 = "q0"
F = {"qF"}  

# função de transição δ
delta = {
    ("q0", "a"): "q1",
    ("q0", "b"): "qd",
    ("q0", "c"): "qd",

    ("q1", "a"): "q1",
    ("q1", "b"): "q1",
    ("q1", "c"): "q2",

    ("q2", "a"): "q2",
    ("q2", "c"): "q2",
    ("q2", "b"): "qF",

    ("qF", "b"): "qF",
    ("qF", "a"): "q2",
    ("qF", "c"): "q2",

    ("qd", "a"): "qd",
    ("qd", "b"): "qd",
    ("qd", "c"): "qd",
}

def step(state: str, symbol: str) -> str:
    return delta.get((state, symbol), "qd")

def accepts(s: str) -> bool:
    state = q0
    for ch in s:
        if ch not in Sigma:
            return False
        state = step(state, ch)
    return state in F  # True apenas se state == "qF"

if __name__ == "__main__":
    positivos = ["acb", "accb", "aacb", "abcb", "acbb", "abacb", "abccab"]
    negativos = ["ab", "cab", "ac", "", "b", "c", "aa"]
    print("Testes positivos (devem ser True):")
    for w in positivos:
        print(f"{w:8} -> {accepts(w)}")
    print("\nTestes negativos (devem ser False):")
    for w in negativos:
        print(f"{w:8} -> {accepts(w)}")