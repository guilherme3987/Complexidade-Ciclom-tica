import matplotlib.pyplot as plt

# Dados fornecidos
arquivos = [
    'app/src/main/res/values/strings.xml',
    'CHANGELOG.md',
    'app/build.gradle',
    'app/src/main/res/values-zh-rCN/strings.xml',
    'app/src/main/res/values-de/strings.xml',
    'app/src/main/res/values-ru/strings.xml',
    'app/src/main/res/values-zh-rTW/strings.xml',
    'app/src/main/res/values-fr/strings.xml',
    'app/src/main/res/values-ar/strings.xml'
]

alteracoes = [315, 304, 269, 228, 205, 200, 189, 187, 172]

# Criar o gráfico
plt.figure(figsize=(12, 8))
plt.barh(arquivos, alteracoes, color='skyblue')
plt.xlabel('Número de Alterações')
plt.ylabel('Arquivos')
plt.title('Arquivos Mais Alterados')
plt.gca().invert_yaxis()  # Inverte o eixo y para mostrar o arquivo mais alterado no topo
plt.tight_layout()  # Ajusta o layout para não cortar labels

# Exibir o gráfico
plt.show()
