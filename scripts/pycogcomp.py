"""[PyCogComp]

    https://cogcomp.github.io/cogcomp-nlpy/
    https://github.com/CogComp/cogcomp-nlpy
    https://github.com/CogComp/cogcomp-nlp/tree/master/pipeline
"""
from ccg_nlpy import remote_pipeline

pipeline = remote_pipeline.RemotePipeline()
doc = pipeline.doc("Hello, how are you. I am doing fine")

# will produce (hello Hello) (, ,) (how how) (be are) (you you) (. .) (i I) (be am) (do doing) (fine fine)
print(doc.get_lemma)

# will produce (UH Hello) (, ,) (WRB how) (VBP are) (PRP you) (. .) (PRP I) (VBP am) (VBG doing) (JJ fine)
print(doc.get_pos)
