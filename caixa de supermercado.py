prod1 = "Arroz Tio João 1kg"
codprod1 = 501
valprod1 = 7.95

prod2 = 'Feijão Kicaldo 1kg'
codprod2 = 502
valprod2 = 4.65

prod3 = 'Aguardente Velho Barreiro 910ml'
codprod3 = 503
valprod3 = 2.98

prod4 = 'Fio Dental Reach Essencial Menta 100m'
codprod4 = 504
valprod4 = 9.85

prod5 = 'Fralda Huggies G Turma da Mônica Tripla Proteção Mega - 48 Unidades'
codprod5 = 505
valprod5 = 29.90

prod6 = 'Bebida à Base de Soja Sabor Maçã Ades 1 Litro'
codprod6 = 506
valprod6 = 5.95

print("Código do Produto\t Nome do produto\t Preço Unitário")
print("")  # \t é a msm coisa que um tab
print(f"{codprod1:^17}\t {prod1[:20]:<13}\t  R${valprod1}")  # ^ centraliza, <> alinhaa esquerda ou a direita
print(f"{codprod2:^17}\t {prod2[:20]:<13}\t  R${valprod2}")  # O número é referente ao tamanho da célula
print(f"{codprod3:^17}\t {prod3[:20]:<13}\t  R${valprod3}")  # [:20] Limita a exibição de caracteres na lista
print(f"{codprod4:^17}\t {prod4[:20]:<13}\t  R${valprod4}")
print(f"{codprod5:^17}\t {prod5[:20]:<13}\t  R${valprod5}")
print(f"{codprod6:^17}\t {prod6[:20]:<13}\t  R${valprod6}")

prod = 1
valortotal = 0

while prod != 0:

    prod = int(input("Digite o código do produto: "))

    if 501 <= prod <= 506:
        qnt = int(input("Digite a quantidade de produtos comprados: "))

        if prod == 501:
            print(
                f"Você comprou {qnt} unidades de {prod1}, que custam: R$ {valprod1} a unidade."
                "Total: R$ {valprod1 * qnt:.2f}")
            valortotal = valortotal + valprod1 * qnt

        if prod == 502:
            print(
                f"Você comprou {qnt} unidades de {prod2}, que custam: R$ {valprod2} a unidade."
                "Total: R$ {valprod2 * qnt:.2f}")
            valortotal += valprod2 * qnt

        if prod == 503:
            print(
                f"Você comprou {qnt} unidades de {prod3}, que custam: R$ {valprod3} a unidade."
                "Total: R$ {valprod3 * qnt:.2f}")
            valortotal += valprod3 * qnt

        if prod == 504:
            print(
                f"Você comprou {qnt} unidades de {prod4}, que custam: R$ {valprod4} a unidade."
                "Total: R$ {valprod4 * qnt:.2f}")
            valortotal += valprod4 * qnt

        if prod == 505:
            print(
                f"Você comprou {qnt} unidades de {prod5}, que custam: R$ {valprod5} a unidade."
                "Total: R$ {valprod5 * qnt:.2f}")
            valortotal += valprod5 * qnt

        if prod == 506:
            print(
                f"Você comprou {qnt} unidades de {prod6}, que custam: R$ {valprod6} a unidade."
                "Total: R$ {valprod6 * qnt:.2f}")
            valortotal += valprod6 * qnt

    else:

        if prod == 0:
            print(f"O valor total da compra é: R$ {valortotal:.2f}")

        else:
            print("Código do produto inexistente, por favor digite novamente.")
