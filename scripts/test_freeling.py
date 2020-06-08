"""[Test FreeLing]
"""
import load_file
from myfreeling.myfreeling import WrapperFreeLing


def run(corpus):
    pipeline = ['wsd', 'svo_triples_srl', 'wordnet_sumo']

    json_data = WrapperFreeLing(corpus, pipeline).run()

    return json_data


if __name__ == "__main__":
    path_corpus = '/home/fasr/Mestrado/Workspace/deepnlpf/deepnlpf/profile_analysis/data/in/corpus/semeval_2010/corpus8000sentences.txt'
    path_out = '/home/fasr/Mestrado/Workspace/deepnlpf/deepnlpf/profile_analysis/data/out/corpus8000sentences/freeling/corpus8000sentences.txt'
    
    corpus = load_file.load(path_corpus)
    
    result = run(corpus)

    load_file.save(path_out, str(result))

'''
    extrat svo triples srl
'''
'''
json_data = freeling.get_extrat_svo_triples_srl(freeling.analyze(sentence))

if json_data != None:
    for data in json_data['svo']:
        print data, json_data['svo'][data]['lemma'], json_data['svo'][data]['synset']
else:
    print json_data
'''

## Ontology
# print freeling.get_ontologia_class(freeling.analyze(sentence))