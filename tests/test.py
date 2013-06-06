import petrarch.petrarch
import petrarch.parse
import pickle
from nltk.tree import Tree

def test_main():
    sent = """Arnor is about to restore full diplomatic ties with Gondor almost 
              five years after crowds trashed its embassy, a senior official 
              said on Saturday."""
    key = 'DEMO-01'
    chunker = petrarch.petrarch._get_data('ubt_chunker_trained.pickle')
    ubt_chunker = pickle.load(open(chunker))
    tag = petrarch.petrarch._get_data('maxent_treebank_pos_tagger.pickle')
    pos_tagger = pickle.load(open(tag))
    update = petrarch.parse.parse_call(sent, key, ubt_chunker, pos_tagger)
    actual = {'DEMO-01': {'noun_phrases': ['Arnor', 
              'restore full diplomatic ties',
              'Gondor almost five years', 'crowds', 'its embassy',
              'a senior official', 'Saturday'],
              'sent_tree': Tree('S', [Tree('NP', [('Arnor', 'NNP')]), 
              Tree('VP', [('is', 'VBZ')]), Tree('PP', [('about', 'IN')]), 
              Tree('PP', [('to', 'TO')]), Tree('NP', [('restore', 'VB'), 
                  ('full', 'JJ'), ('diplomatic', 'JJ'), ('ties', 'NNS')]), 
              Tree('PP', [('with', 'IN')]), Tree('NP', [('Gondor', 'NNP'), 
                  ('almost', 'RB'), ('five', 'CD'), ('years', 'NNS')]), 
              Tree('PP', [('after', 'IN')]), Tree('NP', [('crowds', 'NNS')]), 
              Tree('VP', [('trashed', 'VBD')]), Tree('NP', [('its', 'PRP$'),
                  ('embassy', 'NN')]), (',', ','), Tree('NP', [('a', 'DT'),
                      ('senior', 'JJ'), ('official', 'NN')]), 
              Tree('VP', [('said', 'VBD')]), Tree('PP', [('on', 'IN')]), 
              Tree('NP', [('Saturday', 'NNP')]), ('.', '.')]),
              'tagged': [('Arnor', 'NNP'), ('is', 'VBZ'), ('about', 'IN'),
                         ('to', 'TO'), ('restore', 'VB'), ('full', 'JJ'),
                         ('diplomatic', 'JJ'), ('ties', 'NNS'), ('with', 'IN'),
                         ('Gondor', 'NNP'), ('almost', 'RB'), ('five', 'CD'),
                         ('years', 'NNS'), ('after', 'IN'), ('crowds', 'NNS'),
                         ('trashed', 'VBD'), ('its', 'PRP$'), ('embassy', 'NN'),
                         (',', ','), ('a', 'DT'), ('senior', 'JJ'),
                         ('official', 'NN'), ('said', 'VBD'), ('on', 'IN'),
                         ('Saturday', 'NNP'), ('.', '.')],
              'verb_phrases': [('trashed', 'its embassy')]}}

    assert update == actual