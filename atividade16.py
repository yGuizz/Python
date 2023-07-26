import math

def calcular_latas_tinta(area):
    # Cada lata de tinta cobre 108 metros quadrados (18 litros * 6 metros quadrados por litro)
    metros_por_lata = 108
    # Adicionando 10% de folga e arredondando para cima a quantidade de latas necessárias
    latas_necessarias = math.ceil(area * 1.1 / metros_por_lata)
    return latas_necessarias

def calcular_galoes_tinta(area):
    # Cada galão de tinta cobre 21,6 metros quadrados (3,6 litros * 6 metros quadrados por litro)
    metros_por_galao = 21.6
    # Adicionando 10% de folga e arredondando para cima a quantidade de galões necessários
    galoes_necessarios = math.ceil(area * 1.1 / metros_por_galao)
    return galoes_necessarios

def calcular_combinacao_latas_galoes(area):
    # Quantidade de metros quadrados que uma lata comporta com 10% de folga
    metros_por_lata = 108 * 1.1
    # Quantidade de metros quadrados que um galão comporta com 10% de folga
    metros_por_galao = 21.6 * 1.1

    # Calcula a quantidade de latas necessárias
    latas_necessarias = area // metros_por_lata
    area_restante = area % metros_por_lata

    # Calcula a quantidade de galões necessários para a área restante
    galoes_necessarios = math.ceil(area_restante / metros_por_galao)

    return latas_necessarias, galoes_necessarios

def main():
    try:
        area_pintada = float(input("Digite o tamanho em metros quadrados da área a ser pintada: "))

        latas_necessarias = calcular_latas_tinta(area_pintada)
        preco_latas = latas_necessarias * 80.00

        galoes_necessarios = calcular_galoes_tinta(area_pintada)
        preco_galoes = galoes_necessarios * 25.00

        latas_combinacao, galoes_combinacao = calcular_combinacao_latas_galoes(area_pintada)
        preco_combinacao = latas_combinacao * 80.00 + galoes_combinacao * 25.00

        print(f"Quantidade de latas de tinta a serem compradas: {latas_necessarias}")
        print(f"Preço apenas com latas de 18 litros: R$ {preco_latas:.2f}")

        print(f"Quantidade de galões de tinta a serem comprados: {galoes_necessarios}")
        print(f"Preço apenas com galões de 3,6 litros: R$ {preco_galoes:.2f}")

        print(f"Quantidade de latas e galões combinados:")
        print(f"Latas: {latas_combinacao}, Galões: {galoes_combinacao}")
        print(f"Preço com combinação de latas e galões: R$ {preco_combinacao:.2f}")

    except ValueError:
        print("Valor inválido. Certifique-se de digitar um número válido para a área.")

if __name__ == "__main__":
    main()
