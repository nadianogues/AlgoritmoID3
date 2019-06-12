import pandas as ps
import matplotlib.pyplot as plt

dadosTeste = ps.read_csv('teste.csv', header=None)
dadosTeste = dadosTeste.values
documentoTreinamento = ps.read_csv('iris.csv', header=None)
documentoTreinamento = documentoTreinamento.values

print(documentoTreinamento)

dadosTreinamento = documentoTreinamento[:, :-1]
classes = documentoTreinamento[:, -1:]

#plt.plot(dados[:, 0], dados[:, 1], 'ro')
#plt.show()
