from unidecode import unidecode
import string
import re
import nltk
import pickle
import pandas as pd
nltk.download('stopwords')
nltk.download('wordnet')
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

stop_words = set(stopwords.words('english'))
df = pd.read_csv(r'tweets.csv')
text = df.text

model = pickle.load(open('model.pkl', 'rb'))

contractions = {
"ain't": "am not / are not",
"aren't": "are not / am not",
"can't": "cannot",
"can't've": "cannot have",
"'cause": "because",
"could've": "could have",
"couldn't": "could not",
"couldn't've": "could not have",
"didn't": "did not",
"doesn't": "does not",
"don't": "do not",
"hadn't": "had not",
"hadn't've": "had not have",
"hasn't": "has not",
"haven't": "have not",
"he'd": "he had / he would",
"he'd've": "he would have",
"he'll": "he shall / he will",
"he'll've": "he shall have / he will have",
"he's": "he has / he is",
"how'd": "how did",
"how'd'y": "how do you",
"how'll": "how will",
"how's": "how has / how is",
"i'd": "I had / I would",
"i'd've": "I would have",
"i'll": "I shall / I will",
"i'll've": "I shall have / I will have",
"i'm": "I am",
"i've": "I have",
"isn't": "is not",
"it'd": "it had / it would",
"it'd've": "it would have",
"it'll": "it shall / it will",
"it'll've": "it shall have / it will have",
"it's": "it has / it is",
"let's": "let us",
"ma'am": "madam",
"mayn't": "may not",
"might've": "might have",
"mightn't": "might not",
"mightn't've": "might not have",
"must've": "must have",
"mustn't": "must not",
"mustn't've": "must not have",
"needn't": "need not",
"needn't've": "need not have",
"o'clock": "of the clock",
"oughtn't": "ought not",
"oughtn't've": "ought not have",
"shan't": "shall not",
"sha'n't": "shall not",
"shan't've": "shall not have",
"she'd": "she had / she would",
"she'd've": "she would have",
"she'll": "she shall / she will",
"she'll've": "she shall have / she will have",
"she's": "she has / she is",
"should've": "should have",
"shouldn't": "should not",
"shouldn't've": "should not have",
"so've": "so have",
"so's": "so as / so is",
"that'd": "that would / that had",
"that'd've": "that would have",
"that's": "that has / that is",
"there'd": "there had / there would",
"there'd've": "there would have",
"there's": "there has / there is",
"they'd": "they had / they would",
"they'd've": "they would have",
"they'll": "they shall / they will",
"they'll've": "they shall have / they will have",
"they're": "they are",
"they've": "they have",
"to've": "to have",
"wasn't": "was not",
"we'd": "we had / we would",
"we'd've": "we would have",
"we'll": "we will",
"we'll've": "we will have",
"we're": "we are",
"we've": "we have",
"weren't": "were not",
"what'll": "what shall / what will",
"what'll've": "what shall have / what will have",
"what're": "what are",
"what's": "what has / what is",
"what've": "what have",
"when's": "when has / when is",
"when've": "when have",
"where'd": "where did",
"where's": "where has / where is",
"where've": "where have",
"who'll": "who shall / who will",
"who'll've": "who shall have / who will have",
"who's": "who has / who is",
"who've": "who have",
"why's": "why has / why is",
"why've": "why have",
"will've": "will have",
"won't": "will not",
"won't've": "will not have",
"would've": "would have",
"wouldn't": "would not",
"wouldn't've": "would not have",
"y'all": "you all",
"y'all'd": "you all would",
"y'all'd've": "you all would have",
"y'all're": "you all are",
"y'all've": "you all have",
"you'd": "you had / you would",
"you'd've": "you would have",
"you'll": "you shall / you will",
"you'll've": "you shall have / you will have",
"you're": "you are",
"you've": "you have"
}

def preprocess2(text):
    text2 = []
    #lower characters and put it 
    lowered_text = text.lower()
    text2.append(unidecode(lowered_text))
        
    #Contractions to original length
    i = -1
    for sent in text2:
        i+=1
        for word in sent.split():
            if word in contractions:
                text2[i] = text2[i].replace(word, contractions[word.lower()])

    #remove the twitter pictures links
    i = -1
    for sent in text2:
        i+=1
        for word in sent.split():
            if 'pic.' in word:
                #text2[i] = text2[i].replace(word, '')
                text2[i] = text2[i].replace(word[word.index("pic"):], '')

    #remove all others links that begin with http      
    i = -1
    for sent in text2:
        i+=1
        for word in sent.split():
            if 'http' in word:
                text2[i] = text2[i].replace(word, '')            

    #remove all special characters and punctuations
    i=0
    for sent in text2:
        #text2[i] = re.sub(r'\W+', ' ', text2[i])
        text2[i] = text2[i].translate(str.maketrans('', '', string.punctuation))
        i+=1    

    #remove stopwords
    def convert_list_to_string(org_list, seperator=' '):
        return seperator.join(org_list)

    i = -1
    for sent in text2:
        i+=1
        filtered_sentence = [w for w in sent.split() if not w in stop_words]
        full_str = convert_list_to_string(filtered_sentence)
        text2[i] = full_str

    #lemmatize with context (adverb, verb)
    wordnet_lemmatizer = WordNetLemmatizer()
    i=-1
    for sent in text2:
        i+=1
        token = sent.split()
        j=-1
        for word in token:
            j+=1
            if(word.endswith('ly')):
                token[j] = word[:-2]
            elif(word.endswith('ing')):
                token[j] = word[:-3]

        lemmatized_word = [wordnet_lemmatizer.lemmatize(word) for word in token]#first time to remove all the plurals
        lemmatized_word2 = [wordnet_lemmatizer.lemmatize(word, 'v') for word in lemmatized_word]#second time to transform all the verbs into their root
        full_str = convert_list_to_string(lemmatized_word2)
        text2[i] = full_str
    
    return text2[0].split()

def pipeline(string):
    txt = preprocess2(string)
    r = model.docvecs.most_similar(positive=[model.infer_vector(txt)],topn=20)
    result = []
    for i in range(20):
        result.append(text[r[i][0]])
    return result