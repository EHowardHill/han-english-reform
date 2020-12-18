# import these modules 
import nltk, pprint, hgtk
nltk.download('wordnet')
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('cmudict')

import pyphen

from nltk.stem import WordNetLemmatizer 
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer 
from nltk.corpus import wordnet
from nltk.corpus import cmudict
from google_trans_new import google_translator  

characters = {
    "a":"丨",
    "b":"口",
    "c":"干",
    "d":"冂",
    "e":"人",
    "f":"㇆",
    "g":"工",
    "h":"木",
    "i":"㇒",
    "j":"巴",
    "k":"扌",
    "l":"凵",
    "m":"㇇",
    "n":"匕",
    "o":"目",
    "p":"⺈",
    "q":"十",
    "r":"⺀",
    "s":"大",
    "t":"匚",
    "u":"又",
    "v":"亅",
    "w":"㇗",
    "x":"己",
    "y":"里",
    "z":"刀"
}

# Convert latin characters to alternative script
def han(x):
    if x in [',','.','(',')','\'']: return x
    try:
        fs = ''.join([characters[xx] for xx in x.lower()])
        try:
            return hgtk.text.compose(fs)
        except:
            return fs
    except:
        return x

d = cmudict.dict()
ps = PorterStemmer() 
translator = google_translator()  

# Function lovingly borrowed from stackoverflow.com/questions/14541303/count-the-number-of-syllables-in-a-word
def syllables(word):
    count = 0
    vowels = 'aeiouy'
    word = word.lower()
    if word[0] in vowels:
        count +=1
    for index in range(1,len(word)):
        if word[index] in vowels and word[index-1] not in vowels:
            count +=1
    if word.endswith('e'):
        count -= 1
    if word.endswith('le'):
        count += 1
    if count == 0:
        count += 1
    return count

# Number of syllables
def nsyl(word):
    try:
        return [len(list(y for y in x if y[-1].isdigit())) for x in d[word.lower()]]
    except KeyError:
        #if word not found in cmudict
        return syllables(word)

def get_wordnet_pos(treebank_tag):
    if treebank_tag.startswith('J'):
        return wordnet.ADJ
    elif treebank_tag.startswith('V'):
        return wordnet.VERB
    elif treebank_tag.startswith('N'):
        return wordnet.NOUN
    elif treebank_tag.startswith('R'):
        return wordnet.ADV
    else:
        return wordnet.NOUN

lemmatizer = WordNetLemmatizer() 
  
text = input("Sentence: ")
bun = nltk.pos_tag(word_tokenize(text))

kan = ['NN','NNS','JJ','JJR','RB','PRP','VB','VBD']

saishuu = []

for b in bun:
    kaki = lemmatizer.lemmatize(b[0],pos=get_wordnet_pos(b[1]))

    if kaki == b[0] and b[1] in kan:
        saishuu.append(translator.translate(kaki,lang_tgt='zh-CN'))
    elif kaki != b[0]:
        ikko = ps.stem(b[0])
        saishuu.append(translator.translate(kaki,lang_tgt='zh-CN')+han(b[0][len(ikko):]))
    else:
        saishuu.append(han(b[0]))

print(''.join(saishuu).replace(' ',''))