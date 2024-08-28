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
    'app/src/main/res/values-ar/strings.xml',
    'app/src/main/res/values-zh-rHK/strings.xml',
    'app/src/main/res/values-es/strings.xml',
    'app/src/main/res/values-pt-rBR/strings.xml',
    'app/src/main/res/values-cs/strings.xml',
    'app/src/main/res/values-ja/strings.xml',
    'app/src/main/res/values-it/strings.xml',
    'app/src/main/res/values-hu/strings.xml',
    'app/src/main/java/org/breezyweather/settings/activities/AboutActivity.kt',
    'app/src/main/res/values-uk/strings.xml',
    'app/src/main/AndroidManifest.xml'
]

alteracoes = [315, 304, 269, 228, 205, 200, 189, 187, 172, 156, 151, 145, 141, 139, 137, 131, 131, 123, 123]

# Criar o gráfico
plt.figure(figsize=(12, 10))
plt.barh(arquivos, alteracoes, color='skyblue')
plt.xlabel('Número de Alterações')
plt.ylabel('Arquivos')
plt.title('Arquivos Mais Alterados')
plt.gca().invert_yaxis()  # Inverte o eixo y para mostrar o arquivo mais alterado no topo
plt.tight_layout()  # Ajusta o layout para não cortar labels

# Exibir o gráfico
plt.show()
