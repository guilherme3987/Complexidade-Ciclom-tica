import matplotlib.pyplot as plt

# Função para ler os dados do arquivo
def ler_dados(arquivo):
    with open(arquivo, 'r') as file:
        linhas = file.readlines()

    # Ignorar a primeira linha com o total
    linhas = linhas[1:]

    # Processar os dados
    quantidades = []
    arquivos = []
    for linha in linhas:
        partes = linha.strip().split(maxsplit=1)
        if len(partes) == 2:
            quantidades.append(int(partes[0]))
            arquivos.append(partes[1])

    return arquivos, quantidades

# Ler os dados do arquivo
arquivos, quantidades = ler_dados('C:/Users/guilh/OneDrive/Área de Trabalho/TELP/Complexidade Ciclomatica/Complexidade-Ciclom-tica/Info/Churn_Code/most_churn_files.txt')

# Criar o gráfico
plt.figure(figsize=(10, 8))
plt.barh(arquivos, quantidades, color='steelblue')
plt.xlabel('Quantidade')
plt.ylabel('Arquivo')
plt.title('Quantidade de Mudanças em Arquivos')
plt.gca().invert_yaxis()  # Inverter o eixo Y para mostrar o maior valor no topo
plt.tight_layout()
plt.show()
