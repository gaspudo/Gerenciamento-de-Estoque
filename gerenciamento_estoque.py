def armazenar_produto(lista, nome, preco):
    '''
    Docstring for armazenar_produto
    
    :param lista: list - Lista onde os produtos serão armazenados.
    :param nome: str - Nome do produto.
    :param preco: float - Preço Unitário do produto.
    '''
    lista.append((nome, preco))

def exibir_resultados(lista):
    '''
    Docstring for exibir_resultados
    
    :param lista: list - Nome da lista que deseja exibir.
    '''
    if not lista:
        print("\n[!] Estoque vazio. Nada a processar.")
        return

    # Ordenação única 
    lista.sort(key=lambda x: x[1])

    soma = sum(item[1] for item in lista)
    media = soma / len(lista)
    
    # definindo produto mais barato e o mais caro 
    p_barato, v_barato = lista[0] 
    p_caro, v_caro = lista[-1]

    print(f"\n--- Relatório ---")
    print(f"Média: R${media:.2f}")
    print(f"Mais Barato: {p_barato} (R${v_barato:.2f})")
    print(f"Mais Caro: {p_caro} (R${v_caro:.2f})")

# Bloco principal de execução
if __name__ == "__main__":
    lista_produtos = []
    print("--- Bem-vindo ao Sistema. ---")

    while True:
        nome = input("Digite o nome do Produto (ou 'SAIR'): ").strip().upper()
        if nome == "SAIR":
            break
        
        try:
            valor = float(input(f"Digite o preço de {nome}: "))
            armazenar_produto(lista_produtos, nome, valor)
        except ValueError:
            print("Erro!! Digite um número válido para o preço.")

    exibir_resultados(lista_produtos)
    print("Fim do programa.")
