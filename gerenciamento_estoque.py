'''O Enunciado: Escreva um programa que permita ao usuário gerenciar uma lista de preços de produtos. O programa deve:
Entrada em Laço: Permanecer em um laço while lendo nomes de produtos e seus respectivos preços (use input() e conversão para float).
Armazenamento: Armazenar os nomes em uma lista e os preços em outra (ou use uma lista de listas/tuplas se quiser arriscar).
Condição de Parada: O laço deve terminar quando o usuário digitar "SAIR" no nome do produto.
Processamento com for: Após sair do laço, use um comando for para percorrer as listas e calcular:
A média de preço dos produtos.
O nome do produto mais caro e do mais barato.
Tratamento de Erros: Use um bloco try-except para garantir que o programa não quebre caso o usuário digite um preço inválido (letras em vez de números).'''
def armazenar_produto(lista, nome, preco):
    lista.append((nome, preco))

def exibir_resultados(lista):
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