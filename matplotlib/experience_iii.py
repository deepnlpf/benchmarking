"""
    Experimento III


    https://pydatascience.org/2017/11/24/plot-multiple-lines-in-one-chart-with-different-style-python-matplotlib/
"""
import matplotlib.pyplot as plt
import numpy as np
from collections import OrderedDict

linestyles = OrderedDict(
    [('solid',               (0, ())),
     ('loosely dotted',      (0, (1, 10))),
     ('dotted',              (0, (1, 5))),
     ('densely dotted',      (0, (1, 1))),

     ('loosely dashed',      (0, (5, 10))),
     ('dashed',              (0, (5, 5))),
     ('densely dashed',      (0, (5, 1))),

     ('loosely dashdotted',  (0, (3, 10, 1, 10))),
     ('dashdotted',          (0, (3, 5, 1, 5))),
     ('densely dashdotted',  (0, (3, 1, 1, 1))),

     ('loosely dashdotdotted', (0, (3, 10, 1, 10, 1, 10))),
     ('dashdotdotted',         (0, (3, 5, 1, 5, 1, 5))),
     ('densely dashdotdotted', (0, (3, 1, 1, 1, 1, 1)))])

sentences = [0, 1000, 4000, 8000]

fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(7, 7))

# LEXICON
axes[0, 0].set_title("Lexical Pipeline", fontsize=10)

corenlp_lexicon = [0, 73.6, 206, 379]
spacy_lexicon = [0, 15.3, 46.9, 93.3]
cogcomp_lexicon = [0, 286, 1370, 2280]

corenlp_lexicon_deepnlpf = [0, 47.1, 113, 196]
spacy_lexicon_deepnlpf = [0, 13.2, 49.2, 96.3]
cogcomp_lexicon_deepnlpf = [0, 61.1, 287, 523]

# CoreNLP
axes[0, 0].plot(corenlp_lexicon, sentences, color='C0', linestyle='solid', label="CoreNLP Default")
axes[0, 0].set_xlabel("Runtime(s)")
axes[0, 0].set_ylabel("#Sentences")

axes[0, 0].plot(corenlp_lexicon_deepnlpf, sentences, color='C1', linestyle="dashdot", label="CoreNLP DeepNLPF")
axes[0, 0].set_xlabel("Runtime(s)")
axes[0, 0].set_ylabel("#Sentences")

# SpaCy
axes[0, 0].plot(spacy_lexicon, sentences, color='C2', linestyle="dashed", label="SpaCy Default")
axes[0, 0].set_xlabel("Runtime(s)")
axes[0, 0].set_ylabel("#Sentences")

axes[0, 0].plot(spacy_lexicon_deepnlpf, sentences, color='C3', linestyle="dotted", label="SpaCy DeepNLPF")
axes[0, 0].set_xlabel("Runtime(s)")
axes[0, 0].set_ylabel("#Sentences")

axes[0, 0].plot(cogcomp_lexicon, sentences, color='C4', linestyle=linestyles['densely dashdotdotted'], label="CogComp Default")
axes[0, 0].set_xlabel("Runtime(s)")
axes[0, 0].set_ylabel("#Sentences")

axes[0, 0].plot(cogcomp_lexicon_deepnlpf, sentences, color='C5', linestyle=linestyles['loosely dashdotdotted'], label="CogComp DeepNLPF")
axes[0, 0].set_xlabel("Runtime(s)")
axes[0, 0].set_ylabel("#Sentences")

axes[0, 0].legend(loc=4, prop={'size': 6})

# SINTATIC
axes[0, 1].set_title("Syntactic Pipeline", fontsize=10)

corenlp_sintatic = [0, 234, 714, 1330]
cogcomp_sintatic = [0, 242, 1170, 2040]

corenlp_sintatic_deepnlpf = [0, 167, 525, 1180]
cogcomp_sintatic_deepnlpf = [0, 65.6, 258, 643]

# CoreNLP
axes[0, 1].plot(corenlp_sintatic, sentences, color='C0', linestyle='solid', label="CoreNLP Default")
axes[0, 1].set_xlabel("Runtime(s)")
axes[0, 1].set_ylabel("#Sentences")

axes[0, 1].plot(corenlp_sintatic_deepnlpf, sentences, color='C1', linestyle="dashdot", label="CoreNLP DeepNLPF")
axes[0, 1].set_xlabel("Runtime(s)")
axes[0, 1].set_ylabel("#Sentences")

# CogComp
axes[0, 1].plot(cogcomp_sintatic, sentences, color='C2', linestyle="dashed", label="CogComp Default")
axes[0, 1].set_xlabel("Runtime(s)")
axes[0, 1].set_ylabel("#Sentences")

axes[0, 1].plot(cogcomp_sintatic_deepnlpf, sentences, color='C3', linestyle="dotted", label="CogComp DeepNLPF")
axes[0, 1].set_xlabel("Runtime(s)")
axes[0, 1].set_ylabel("#Sentences")

axes[0, 1].legend(loc=4, prop={'size': 6})

# SEMANTIC
axes[1, 0].set_title("Semantic Pipeline", fontsize=10)

semafor_semantic = [0, 84.1, 234, 466]
cogcomp_semantic = [0, 1170, 4390, 9210]
pywsd_semantic = [0, 1000, 4070, 8220]

semafor_semantic_deepnlpf = [0, 86.4, 239, 445]
cogcomp_semantic_deepnlpf = [0, 839, 3190, 6370]
pywsd_semantic_deepnlpf = [0, 24.1, 51.7, 84.6]

# SEMAFOR
axes[1, 0].plot(semafor_semantic, sentences, color='C0', linestyle='solid', label="SEMAFOR Default")
axes[1, 0].set_xlabel("Runtime(s)")
axes[1, 0].set_ylabel("#Sentences")

axes[1, 0].plot(semafor_semantic_deepnlpf, sentences, color='C1', linestyle="dashdot", label="SEMAFOR DeepNLPF")
axes[1, 0].set_xlabel("Runtime(s)")
axes[1, 0].set_ylabel("#Sentences")

# PyWSD
axes[1, 0].plot(pywsd_semantic, sentences, color='C2', linestyle="dashed", label="PyWSD Default")
axes[1, 0].set_xlabel("Runtime(s)")
axes[1, 0].set_ylabel("#Sentences")

axes[1, 0].plot(pywsd_semantic_deepnlpf, sentences, color='C3', linestyle="dotted", label="PyWSD DeepNLPF")
axes[1, 0].set_xlabel("Runtime(s)")
axes[1, 0].set_ylabel("#Sentences")

# CogComp
axes[1, 0].plot(cogcomp_semantic, sentences, color='C4', linestyle=linestyles['densely dashdotdotted'], label="CogComp Default")
axes[1, 0].set_xlabel("Runtime(s)")
axes[1, 0].set_ylabel("#Sentences")

axes[1, 0].plot(cogcomp_semantic_deepnlpf, sentences, color='C5', linestyle=linestyles['loosely dashdotdotted'], label="CogComp DeepNLPF")
axes[1, 0].set_xlabel("Runtime(s)")
axes[1, 0].set_ylabel("#Sentences")

axes[1, 0].legend(loc=4, prop={'size': 6})

fig.tight_layout()
plt.savefig('/home/fasr/Mestrado/Workspace/benchmarking/matplotlib/img/experience_iii/experience_iii.png', format='png', dpi=300)
plt.show()
