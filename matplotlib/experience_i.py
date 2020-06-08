"""
    Experimento I

    Objetivo - Verificar o tempo de processamento que cada ferramenta de PLN de terceiros
    necessita para processar os três corpus utilizando os pipelines de análises léxico, 
    sintático e semântico, cadá nível individualmente. 
"""
import matplotlib.pyplot as plt
import numpy as np

sentences = [0, 1000, 4000, 8000]

fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(7, 7))

# LEXICON
axes[0, 0].set_title("Pipeline Lexicon")

corenlp_lexicon = [0, 73.6, 206, 379]
spacy_lexicon = [0, 15.3, 46.9, 93.3]
cogcomp_lexicon = [0, 286, 1370, 2280]

# CoreNLP
axes[0, 0].plot(corenlp_lexicon, sentences, color='C0', linestyle='dashed', label="CoreNLP")
axes[0, 0].set_xlabel("Runtime(sec)")
axes[0, 0].set_ylabel("Sentences")

# SpaCy
axes[0, 0].plot(spacy_lexicon, sentences, color='C1', linestyle='dashdot', label="SpaCy")
axes[0, 0].set_xlabel("Runtime(sec)")
axes[0, 0].set_ylabel("Sentences")

axes[0, 0].plot(cogcomp_lexicon, sentences, color='C2', label="CogComp")
axes[0, 0].set_xlabel("Runtime(sec)")
axes[0, 0].set_ylabel("Sentences")

axes[0, 0].legend()

# SINTATIC
axes[0, 1].set_title("Pipeline Sintatic")

corenlp_sintatic = [0, 234, 714, 1330]
cogcomp_sintatic = [0, 242, 1170, 2040]

# CoreNLP
axes[0, 1].plot(corenlp_sintatic, sentences, color='C0', linestyle='dashdot', label="CoreNLP")
axes[0, 1].set_xlabel("Runtime(sec)")
axes[0, 1].set_ylabel("Sentences")

# CogComp
axes[0, 1].plot(cogcomp_sintatic, sentences, color='C2', linestyle='solid', label="CogComp")
axes[0, 1].set_xlabel("Runtime(sec)")
axes[0, 1].set_ylabel("Sentences")

axes[0, 1].legend()

# SEMANTIC
axes[1, 0].set_title("Pipeline Semantic")

semafor_semantic = [0, 84.1, 234, 466]
cogcomp_semantic = [0, 1170, 4390, 9210]
pywsd_semantic = [0, 1000, 4070, 8220]

# SEMAFOR
axes[1, 0].plot(semafor_semantic, sentences, color='C0', linestyle='dashdot', label="SEMAFOR")
axes[1, 0].set_xlabel("Runtime(sec)")
axes[1, 0].set_ylabel("Sentences")

# PyWSD
axes[1, 0].plot(pywsd_semantic, sentences, color='C1', linestyle='solid', label="PyWSD")
axes[1, 0].set_xlabel("Runtime(sec)")
axes[1, 0].set_ylabel("Sentences")

# CogComp
axes[1, 0].plot(cogcomp_semantic, sentences, color='C2', linestyle='dotted', label="CogComp")
axes[1, 0].set_xlabel("Runtime(sec)")
axes[1, 0].set_ylabel("Sentences")

axes[1, 0].legend()

fig.tight_layout()
plt.show()