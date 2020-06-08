import matplotlib.pyplot as plt
import numpy as np

sentences = [0, 1000, 4000, 8000]
outher_tool = [0, 2439.6, 9935.3, 18879.2]
deepnlpf = [0, 824, 3250, 6320]

meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho']
valores = [105235, 107697, 110256, 109236, 108859, 109986]

plt.plot(outher_tool, sentences, label='Processing Default')
plt.plot(deepnlpf, sentences, label='Processing DeepNLPF')

plt.xlabel('Runtime (sec)')
plt.ylabel("Numbem sentence")
plt.title("")
plt.legend()
plt.show()