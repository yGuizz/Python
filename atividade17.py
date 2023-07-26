def main():
    try:
        tamanho_arquivo_mb = float(input("Digite o tamanho do arquivo para download (em MB): "))
        velocidade_internet_mbps = float(input("Digite a velocidade do link de Internet (em Mbps): "))

        tempo_download_minutos = tamanho_arquivo_mb / (velocidade_internet_mbps / 8 * 60)

        print(f"Tempo aproximado de download: {tempo_download_minutos:.2f} minutos")

    except ValueError:
        print("Valores inválidos. Certifique-se de digitar números válidos.")

if __name__ == "__main__":
    main()

    