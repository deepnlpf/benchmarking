"""
    LinePlotly
    Generated Graphics Line Usigned Plot.Ly from Experience Profiling.
    Date: 17/07/2019
"""

import plotly.graph_objects as go


def runtime_all_tools():
    sentences_corpus = [0, 1000, 4000, 8000]

    stanford_corenlp = [0, 270, 776, 1630]
    spacy = [0, 12.3, 46.3, 91.2]
    semafor = [0, 87.3, 243, 448]
    cogcomp = [0, 1050, 5110, 9350]
    freeling = [0, 398, 1570, 4990]
    pywsd = [0, 1020, 3760, 7360]

    fig = go.Figure()
    # Create and style traces
    # dash options include 'dash', 'dot', and 'dashdot'
    """[color]
        aliceblue, antiquewhite, aqua, aquamarine, azure,
        beige, bisque, black, blanchedalmond, blue, blueviolet, 
            brown, burlywood, 
        cadetblue, chartreuse, chocolate, coral, cornflowerblue,
            cornsilk, crimson, cyan, 
        darkblue, darkcyan, darkgoldenrod, darkgray, darkgrey,
            darkgreen, darkkhaki, darkmagenta, darkolivegreen, darkorange, 
            darkorchid, darkred, darksalmon, darkseagreen, darkslateblue, 
            darkslategray, darkslategrey, darkturquoise, darkviolet, deeppink, 
            deepskyblue, dimgray, dimgrey, dodgerblue, firebrick,
        floralwhite, forestgreen, fuchsia, 
        gainsboro, ghostwhite, gold, goldenrod, gray, grey, green, 
            greenyellow, 
        honeydew, hotpink, 
        indianred, indigo, ivory, 
        khaki, 
        lavender, lavenderblush, lawngreen,lemonchiffon, 
            lightblue, lightcoral, lightcyan,
            lightgoldenrodyellow, lightgray, lightgrey,
            lightgreen, lightpink, lightsalmon, lightseagreen,
            lightskyblue, lightslategray, lightslategrey,
            lightsteelblue, lightyellow, lime, limegreen,
            linen, 
        magenta, maroon, mediumaquamarine,
            mediumblue, mediumorchid, mediumpurple,
            mediumseagreen, mediumslateblue, mediumspringgreen,
            mediumturquoise, mediumvioletred, midnightblue,
            mintcream, mistyrose, moccasin, 
        navajowhite, navy,
        oldlace, olive, olivedrab, orange, orangered,
            orchid, palegoldenrod, 
        palegreen, paleturquoise, palevioletred, papayawhip, 
            peachpuff, peru, pink, plum, powderblue, purple, 
        red, rosybrown, royalblue, rebeccapurple, 
        saddlebrown, salmon, sandybrown, seagreen, seashell, 
            sienna, silver, skyblue, slateblue, slategray, slategrey, 
            snow, springgreen, steelblue, 
        tan, teal, thistle, tomato, turquoise, 
        violet, 
        wheat, white, whitesmoke,
        yellow, yellowgreen
    """

    fig.add_trace(go.Scatter(x=stanford_corenlp, y=sentences_corpus, name='Stanford CoreNLP',
                             line=dict(color='red', width=2)))

    fig.add_trace(go.Scatter(x=spacy, y=sentences_corpus, name='SpaCy',
                             line=dict(color='blue', width=2)))

    fig.add_trace(go.Scatter(x=semafor, y=sentences_corpus, name='SEMAFOR',
                             line=dict(color='coral', width=2)))

    fig.add_trace(go.Scatter(x=cogcomp, y=sentences_corpus, name='CogComp',
                             line=dict(color='orange', width=2)))

    fig.add_trace(go.Scatter(x=freeling, y=sentences_corpus, name='FreeLing',
                             line=dict(color='green', width=2)))

    fig.add_trace(go.Scatter(x=pywsd, y=sentences_corpus, name='PyWSD',
                             line=dict(color='fuchsia', width=2)))

    # Edit the layout
    fig.update_layout(title='NLP Tool Processing Performance',
                      xaxis_title='Runtime(seconds)',
                      yaxis_title='Number of Sentences by Corpus')

    fig.show()


def runtime_comparaction():
    sentences_corpus = [0, 1000, 4000, 8000]

    all_tool = [0, 2439.6, 9935.3, 18879.2]
    deepnlpf = [0, 824, 3250, 6320]

    fig = go.Figure()

    fig.add_trace(go.Scatter(x=all_tool, y=sentences_corpus, name='Sequential Processing',
                             line=dict(color='red', width=2)))

    fig.add_trace(go.Scatter(x=deepnlpf, y=sentences_corpus, name='Parallel Processing (DeepNLPF)',
                             line=dict(color='blue', width=2)))

    # Edit the layout
    fig.update_layout(title='Processing Performance.',
                      xaxis_title='Runtime(seconds)',
                      yaxis_title='Corpus - Number Sentence')

    fig.show()


def experience_1_analise_lexica():
    sentences_corpus = [0, 1000, 4000, 8000]

    corenlp = [0, 73.6, 206, 379]
    spacy = [0, 15.3, 46.9, 93.3]
    cogcomp = [0, 286, 1370, 2280]

    fig = go.Figure()

    fig.add_trace(go.Scatter(x=corenlp, y=sentences_corpus, name='CoreNLP',
                             line=dict(color='red', width=2)))

    fig.add_trace(go.Scatter(x=spacy, y=sentences_corpus, name='SpaCy',
                             line=dict(color='blue', width=2)))

    fig.add_trace(go.Scatter(x=cogcomp, y=sentences_corpus, name='CogComp',
                             line=dict(color='orange', width=2)))

    fig.update_layout(title='Processing Performance.',
                      xaxis_title='Runtime(seconds)',
                      yaxis_title='Corpus - Number Sentence')

    fig.show()

def experience_3_analise_lexica():
    sentences_corpus = [0, 1000, 4000, 8000]

    corenlp = [0, 47.1, 113, 196]
    spacy = [0, 13.2, 49.2, 96.3]
    cogcomp = [0, 61.1, 287, 523]

    fig = go.Figure()

    fig.add_trace(go.Scatter(x=corenlp, y=sentences_corpus, name='CoreNLP - DeepNLPF',
                            line=dict(color='red', width=2)))

    fig.add_trace(go.Scatter(x=spacy, y=sentences_corpus, name='SpaCy - DeepNLPF',
                            line=dict(color='blue', width=2)))

    fig.add_trace(go.Scatter(x=cogcomp, y=sentences_corpus, name='CogComp - DeepNLPF',
                            line=dict(color='orange', width=2)))

    fig.update_layout(title='Processing Performance.',
                    xaxis_title='Runtime(seconds)',
                    yaxis_title='Corpus - Number Sentence')

    fig.show()

def experience_3_analise_lexica_coparation():
    sentences_corpus = [0, 1000, 4000, 8000]

    corenlp = [0, 73.6, 206, 379]
    spacy = [0, 15.3, 46.9, 93.3]
    cogcomp = [0, 286, 1370, 2280]

    corenlp_deepnlpf = [0, 47.1, 113, 196]
    spacy_deepnlpf = [0, 13.2, 49.2, 96.3]
    cogcomp_deepnlpf = [0, 61.1, 287, 523]

    fig = go.Figure()

    fig.add_trace(go.Scatter(x=corenlp, y=sentences_corpus, name='CoreNLP',
                            line=dict(color='red', width=2, dash='dot')))

    fig.add_trace(go.Scatter(x=spacy, y=sentences_corpus, name='SpaCy',
                            line=dict(color='blue', width=2, dash='dot')))

    fig.add_trace(go.Scatter(x=cogcomp, y=sentences_corpus, name='CogComp',
                            line=dict(color='orange', width=2, dash='dot')))


    fig.add_trace(go.Scatter(x=corenlp_deepnlpf, y=sentences_corpus, name='CoreNLP - DeepNLPF',
                            line=dict(color='red', width=2)))

    fig.add_trace(go.Scatter(x=spacy_deepnlpf, y=sentences_corpus, name='SpaCy - DeepNLPF',
                            line=dict(color='blue', width=2)))

    fig.add_trace(go.Scatter(x=cogcomp_deepnlpf, y=sentences_corpus, name='CogComp - DeepNLPF',
                            line=dict(color='orange', width=2)))

    fig.update_layout(title='Processing Performance.',
                    xaxis_title='Runtime(seconds)',
                    yaxis_title='Corpus - Number Sentence')

    fig.show()


def experience_1_analise_sintatica():

    sentences_corpus = [0, 1000, 4000, 8000]

    corenlp = [0, 234, 714, 1330]
    cogcomp = [0, 242, 1170, 2040]

    fig = go.Figure()

    fig.add_trace(go.Scatter(x=corenlp, y=sentences_corpus, name='CoreNLP',
                             line=dict(color='red', width=2)))

    fig.add_trace(go.Scatter(x=cogcomp, y=sentences_corpus, name='CogComp',
                             line=dict(color='orange', width=2)))

    fig.update_layout(title='Processing Performance.',
                      xaxis_title='Runtime(seconds)',
                      yaxis_title='Corpus - Number Sentence')

    fig.show()

def experience_3_analise_sintatica():
    sentences_corpus = [0, 1000, 4000, 8000]

    corenlp = [0, 167, 525, 1180]
    cogcomp = [0, 65.6, 258, 643]

    fig = go.Figure()

    fig.add_trace(go.Scatter(x=corenlp, y=sentences_corpus, name='CoreNLP',
                             line=dict(color='red', width=2)))

    fig.add_trace(go.Scatter(x=cogcomp, y=sentences_corpus, name='CogComp',
                             line=dict(color='orange', width=2)))

    fig.update_layout(title='Processing Performance.',
                      xaxis_title='Runtime(seconds)',
                      yaxis_title='Corpus - Number Sentence')

    fig.show()

def experience_3_analise_sintatica_comparation():
    sentences_corpus = [0, 1000, 4000, 8000]

    corenlp = [0, 234, 714, 1330]
    cogcomp = [0, 242, 1170, 2040]

    corenlp_deepnlpf = [0, 167, 525, 1180]
    cogcomp_deepnlpf = [0, 65.6, 258, 643]

    fig = go.Figure()

    fig.add_trace(go.Scatter(x=corenlp, y=sentences_corpus, name='CoreNLP',
                             line=dict(color='red', width=2, dash='dot')))

    fig.add_trace(go.Scatter(x=cogcomp, y=sentences_corpus, name='CogComp',
                             line=dict(color='orange', width=2, dash='dot')))

    fig.add_trace(go.Scatter(x=corenlp_deepnlpf, y=sentences_corpus, name='CoreNLP - DeepNLPF',
                             line=dict(color='red', width=2)))

    fig.add_trace(go.Scatter(x=cogcomp_deepnlpf, y=sentences_corpus, name='CogComp - DeepNLPF',
                             line=dict(color='orange', width=2)))

    fig.update_layout(title='Processing Performance.',
                      xaxis_title='Runtime(seconds)',
                      yaxis_title='Corpus - Number Sentence')

    fig.show()

def experience_1_analise_semantica():
    sentences_corpus = [0, 1000, 4000, 8000]

    semafor = [0, 84.1, 234, 466]
    cogcomp = [0, 1170, 4390, 9210]
    pywsd = [0, 1000, 4070, 8220]

    fig = go.Figure()

    fig.add_trace(go.Scatter(x=semafor, y=sentences_corpus, name='SEMAFOR',
                             line=dict(color='red', width=2)))

    fig.add_trace(go.Scatter(x=cogcomp, y=sentences_corpus, name='CogComp',
                             line=dict(color='orange', width=2)))

    fig.add_trace(go.Scatter(x=pywsd, y=sentences_corpus, name='PyWSD',
                             line=dict(color='blue', width=2)))

    fig.update_layout(title='Processing Performance.',
                      xaxis_title='Runtime(seconds)',
                      yaxis_title='Corpus - Number Sentence')

    fig.show()


def experience_3_analise_semantica_comparation():
    sentences_corpus = [0, 1000, 4000, 8000]

    semafor = [0, 84.1, 234, 466]
    cogcomp = [0, 1170, 4390, 9210]
    pywsd = [0, 1000, 4070, 8220]

    semafor_deepnlpf = [0, 86.4, 239, 445]
    cogcomp_deepnlpf = [0, 839, 3190, 6370]
    pywsd_deepnlpf = [0, 24.1, 51.7, 84.6]

    fig = go.Figure()

    fig.add_trace(go.Scatter(x=semafor, y=sentences_corpus, name='SEMAFOR',
                             line=dict(color='red', width=2, dash='dot')))

    fig.add_trace(go.Scatter(x=cogcomp, y=sentences_corpus, name='CogComp',
                             line=dict(color='orange', width=2, dash='dot')))

    fig.add_trace(go.Scatter(x=pywsd, y=sentences_corpus, name='PyWSD',
                             line=dict(color='blue', width=2, dash='dot')))

    fig.add_trace(go.Scatter(x=semafor_deepnlpf, y=sentences_corpus, name='SEMAFOR - DeepNLPF',
                             line=dict(color='red', width=2)))

    fig.add_trace(go.Scatter(x=cogcomp_deepnlpf, y=sentences_corpus, name='CogComp - DeepNLPF',
                             line=dict(color='orange', width=2)))

    fig.add_trace(go.Scatter(x=pywsd_deepnlpf, y=sentences_corpus, name='PyWSD - DeepNLPF',
                             line=dict(color='blue', width=2)))

    fig.update_layout(title='Processing Performance.',
                      xaxis_title='Runtime(seconds)',
                      yaxis_title='Corpus - Number Sentence')

    fig.show()


if __name__ == "__main__":
    runtime_all_tools()
    runtime_comparaction()
    
    experience_1_analise_lexica()
    experience_1_analise_sintatica()
    experience_1_analise_semantica()

    experience_3_analise_lexica()
    experience_3_analise_lexica_coparation()

    experience_3_analise_sintatica()
    experience_3_analise_sintatica_comparation()

    experience_3_analise_semantica_comparation()