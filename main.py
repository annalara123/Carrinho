def criar_item(cod, desc, valor_base):
    return {
        'codigo': cod,
        'taxa_adicional': 0,
        'valor_desconto': 0,
        'descricao': desc,
        'preco': valor_base
    }

def incrementar_taxa(item, taxa):
    item['taxa_adicional'] += taxa

def aplicar_reducao(item, desconto):
    item['valor_desconto'] += desconto

def iniciar_lista_compras():
    return {
        'itens': []
    }

def adicionar_item(lista, item):
    if any(i['codigo'] == item['codigo'] for i in lista['itens']):
        print(f"O item {item['descricao']} já foi adicionado.")
    else:
        lista['itens'].append(item)
        print(f"{item['descricao']} foi incluído na lista de compras.")

def encontrar_item(lista, cod):
    return next((i for i in lista['itens'] if i['codigo'] == cod), None)

def ajustar_taxa_item(lista, cod, taxa):
    item = encontrar_item(lista, cod)
    if item:
        incrementar_taxa(item, taxa)
    else:
        print("Item não localizado.")

def ajustar_desconto_item(lista, cod, desconto):
    item = encontrar_item(lista, cod)
    if item:
        aplicar_reducao(item, desconto)
    else:
        print("Item não localizado.")

def aplicar_taxa_todos(lista, taxa_total):
    if lista['itens']:
        taxa_por_item = taxa_total / len(lista['itens'])
        for item in lista['itens']:
            incrementar_taxa(item, taxa_por_item)
    else:
        print("A lista de compras está vazia.")

def aplicar_desconto_todos(lista, desconto_total):
    if lista['itens']:
        desconto_por_item = desconto_total / len(lista['itens'])
        for item in lista['itens']:
            aplicar_reducao(item, desconto_por_item)
    else:
        print("A lista de compras está vazia.")

def finalizar_compra(lista):
    if not lista['itens']:
        print("Não há itens na lista de compras.")
        return

    total_taxas = sum(i['taxa_adicional'] for i in lista['itens'])
    total_descontos = sum(i['valor_desconto'] for i in lista['itens'])
    valor_final = sum(i['preco'] + i['taxa_adicional'] - i['valor_desconto'] for i in lista['itens'])

    print("\nResumo Final da Compra:")
    for item in lista['itens']:
        print(f"{item['descricao']} - Preço Original: R$ {item['preco']:.2f}, Taxa: R$ {item['taxa_adicional']:.2f}, Desconto: R$ {item['valor_desconto']:.2f}")

    print(f"\nTotal de Taxas: R$ {total_taxas:.2f}")
    print(f"Total de Descontos: R$ {total_descontos:.2f}")
    print(f"Valor a Pagar: R$ {valor_final:.2f}")

def exibir_catalogo(catalogo):
    print("\nItens Disponíveis:")
    for item in catalogo:
        print(f"Código: {item['codigo']} - {item['descricao']} - Preço: R$ {item['preco']:.2f}")

def iniciar_sistema():
    lista = iniciar_lista_compras()

    catalogo_itens = [
        criar_item(201, 'Celular', 1200.00),
        criar_item(202, 'Laptop', 3200.00),
        criar_item(203, 'TV 4K', 2700.00),
        criar_item(204, 'Fone de Ouvido', 180.00),
        criar_item(205, 'Kindle', 900.00),
    ]

    while True:
        print(
            "\n"
            "1 -> Adicionar item à lista de compras\n"
            "2 -> Adicionar taxa a um item\n"
            "3 -> Aplicar desconto a um item\n"
            "4 -> Adicionar taxa a todos os itens\n"
            "5 -> Aplicar desconto a todos os itens\n"
            "6 -> Finalizar compra\n"
            "0 -> Sair\n"
        )

        opcao = input("Escolha uma opção: ")

        if opcao == "0":
            break

        elif opcao == "1":
            exibir_catalogo(catalogo_itens)
            codigo = int(input("Informe o código do item: "))
            item = encontrar_item({'itens': catalogo_itens}, codigo)
            if item:
                adicionar_item(lista, item)
            else:
                print("Item não encontrado.")

        elif opcao == "2":
            codigo = int(input("Informe o código do item: "))
            taxa = float(input("Informe o valor da taxa: "))
            ajustar_taxa_item(lista, codigo, taxa)

        elif opcao == "3":
            codigo = int(input("Informe o código do item: "))
            desconto = float(input("Informe o valor do desconto: "))
            ajustar_desconto_item(lista, codigo, desconto)

        elif opcao == "4":
            taxa = float(input("Informe o valor total da taxa: "))
            aplicar_taxa_todos(lista, taxa)

        elif opcao == "5":
            desconto = float(input("Informe o valor total do desconto: "))
            aplicar_desconto_todos(lista, desconto)

        elif opcao == "6":
            finalizar_compra(lista)
            break

        else:
            print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    iniciar_sistema()
