#avaliação
class Node:
    def __init__(self, question, yes=None, no=None):
        self.question = question
        self.yes = yes
        self.no = no


def is_leaf(node):
    return node is not None and node.yes is None and node.no is None


def navigate_tree(node, answers):

    if node is None:
        raise ValueError("Árvore vazia (node é None).")

    current = node
    idx = 0

    while not is_leaf(current):
        # faltaram respostas para continuar
        if idx >= len(answers):
            raise ValueError("Faltam respostas para concluir a decisão.")

        raw = answers[idx]
        idx += 1

        if raw is None:
            raise ValueError(f"Resposta inválida: {raw!r}. Use 'sim' ou 'não'.")

        resp = str(raw).strip().lower()

        # aceitar 'nao' como 'não'
        if resp == "nao":
            resp = "não"

        if resp == "sim":
            next_node = current.yes
        elif resp == "não" or resp == "nao":  # 'nao' já normalizamos, mas mantemos por segurança
            next_node = current.no
        else:
            raise ValueError(f"Resposta inválida: {raw!r}. Use 'sim' ou 'não'.")

        if next_node is None:
            raise ValueError("A árvore contém ramificações incompletas.")

        current = next_node

    # quando chegar numa folha, question contém a decisão final
    return current.question

