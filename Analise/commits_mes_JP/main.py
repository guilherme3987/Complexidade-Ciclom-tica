import matplotlib.pyplot as plt

# Dados fornecidos
meses = [
    '2021-02', '2021-03', '2021-04', '2021-10',
    '2022-05', '2023-01', '2023-02', '2023-03',
    '2023-05', '2023-06', '2023-07', '2023-08',
    '2023-09', '2023-10', '2023-11', '2023-12',
    '2024-01', '2024-02', '2024-03', '2024-04',
    '2024-05', '2024-06', '2024-07', '2024-08'
]

commits = [
    1, 20, 7, 1,
    3, 19, 7, 1,
    22, 110, 150, 129,
    25, 18, 11, 6,
    51, 82, 153, 121,
    27, 38, 38, 22
]

# Criar o gráfico
plt.figure(figsize=(12, 6))
plt.bar(meses, commits, color='skyblue')
plt.xlabel('Meses')
plt.ylabel('Quantidade de Commits')
plt.title('Quantidade de Commits por Mês')
plt.xticks(rotation=45)
plt.tight_layout()  # Ajusta o layout para não cortar labels

# Exibir o gráfico
plt.show()
