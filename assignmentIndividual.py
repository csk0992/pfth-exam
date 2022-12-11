# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 15:07:06 2022

@author: fnatm
"""

import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt

'''
This script creates a class to split a dataset of tweets into two new datasets 
depending on the text in a given column with binary values or binary codifying. 
This part of the task is re-useable as is for future content analysis of tweets 
in my studies, but the following part about visualization as a wordcloud is 
intended specifically for the twitter dataset i have chosen as an example, so 
it is written into the main() function and not the class itself.

Of importance in the disaster tweets dataset are two columns, "_golden" and 
"text". The former is the binary column in this case, which either says "TRUE"
or "FALSE", depending on whether or not the actual contents of the tweet refer 
to disaster events or simply uses similar language.

With that in mind, the class needs values for the original .csv dataset, names
for the two files the output is split into, and the name of the column whose
binary cell values determine the split.

The function will read the original file into a dataframe, read the first cell
in the binary column, and then separate the dataframe into two new .csv files
depending on whether all the subsequent rows have the same value as that first
cell or not, since there are only two options.
'''

class binaryTweets:
    def __init__(self, filepath, outputA, outputB, binaryCol):
        self.filepath = filepath
        self.outputA = outputA
        self.outputB = outputB
        self.binaryCol = binaryCol
   
    def splitFile(self):
        df = pd.read_csv(self.filepath)
        
        df_filterA = df[df[self.binaryCol] == df.iloc[0][self.binaryCol]]
        df_filterA.to_csv(self.outputA)
        
        df_filterB = df[df[self.binaryCol] != df.iloc[0][self.binaryCol]]
        df_filterB.to_csv(self.outputB)

'''
Mentioned example dataset is added to main(), along with a stopword list and a
conversion to string variables so that WordCloud() will accept both of the
dataframes output by splitFile().
'''
        
def main():
    disasTwt = binaryTweets('disastertweets.csv', 'disastertweetsTrue.csv', 'disastertweetsFalse.csv', '_golden')
    binaryTweets.splitFile(disasTwt)
    
    stopwords_List = ["","a","about","above","after","again","against","ain","all","am","an","and","any","are","aren","aren't","as","at","be","because","been","before","being","below","between","both","but","by","can","couldn","couldn't","d","did","didn","didn't","do","does","doesn","doesn't","doing","don","don't","down","during","each","few","for","from","further","had","hadn","hadn't","has","hasn","hasn't","have","haven","haven't","having","he","her","here","hers","herself","him","himself","his","how","i","if","in","into","is","isn","isn't","it","it's","its","itself","just","ll","m","ma","me","mightn","mightn't","more","most","mustn","mustn't","my","myself","needn","needn't","no","nor","not","now","o","of","off","on","once","only","or","other","our","ours","ourselves","out","over","own","re","s","same","shan","shan't","she","she's","should","should've","shouldn","shouldn't","so","some","such","t","than","that","that'll","the","their","theirs","them","themselves","then","there","these","they","this","those","through","to","too","under","until","up","ve","very","was","wasn","wasn't","we","were","weren","weren't","what","when","where","which","while","who","whom","why","will","with","won","won't","wouldn","wouldn't","y","you","you'd","you'll","you're","you've","your","yours","yourself","yourselves","could","he'd","he'll","he's","here's","how's","i'd","i'll","i'm","i've","let's","ought","she'd","she'll","that's","there's","they'd","they'll","they're","they've","we'd","we'll","we're","we've","what's","when's","where's","who's","why's","would","able","abst","accordance","according","accordingly","across","act","actually","added","adj","affected","affecting","affects","afterwards","ah","almost","alone","along","already","also","although","always","among","amongst","announce","another","anybody","anyhow","anymore","anyone","anything","anyway","anyways","anywhere","apparently","approximately","arent","arise","around","aside","ask","asking","auth","available","away","awfully","b","back","became","become","becomes","becoming","beforehand","begin","beginning","beginnings","begins","behind","believe","beside","besides","beyond","biol","brief","briefly","c","ca","came","cannot","can't","cause","causes","certain","certainly","co","com","come","comes","contain","containing","contains","couldnt","date","different","done","downwards","due","e","ed","edu","effect","eg","eight","eighty","either","else","elsewhere","end","ending","enough","especially","et","etc","even","ever","every","everybody","everyone","everything","everywhere","ex","except","f","far","ff","fifth","first","five","fix","followed","following","follows","former","formerly","forth","found","four","furthermore","g","gave","get","gets","getting","give","given","gives","giving","go","goes","gone","got","gotten","h","happens","hardly","hed","hence","hereafter","hereby","herein","heres","hereupon","hes","hi","hid","hither","home","howbeit","however","hundred","id","ie","im","immediate","immediately","importance","important","inc","indeed","index","information","instead","invention","inward","itd","it'll","j","k","keep","keeps","kept","kg","km","know","known","knows","l","largely","last","lately","later","latter","latterly","least","less","lest","let","lets","like","liked","likely","line","little","'ll","look","looking","looks","ltd","made","mainly","make","makes","many","may","maybe","mean","means","meantime","meanwhile","merely","mg","might","million","miss","ml","moreover","mostly","mr","mrs","much","mug","must","n","na","name","namely","nay","nd","near","nearly","necessarily","necessary","need","needs","neither","never","nevertheless","new","next","nine","ninety","nobody","non","none","nonetheless","noone","normally","nos","noted","nothing","nowhere","obtain","obtained","obviously","often","oh","ok","okay","old","omitted","one","ones","onto","ord","others","otherwise","outside","overall","owing","p","page","pages","part","particular","particularly","past","per","perhaps","placed","please","plus","poorly","possible","possibly","potentially","pp","predominantly","present","previously","primarily","probably","promptly","proud","provides","put","q","que","quickly","quite","qv","r","ran","rather","rd","readily","really","recent","recently","ref","refs","regarding","regardless","regards","related","relatively","research","respectively","resulted","resulting","results","right","run","said","saw","say","saying","says","sec","section","see","seeing","seem","seemed","seeming","seems","seen","self","selves","sent","seven","several","shall","shed","shes","show","showed","shown","showns","shows","significant","significantly","similar","similarly","since","six","slightly","somebody","somehow","someone","somethan","something","sometime","sometimes","somewhat","somewhere","soon","sorry","specifically","specified","specify","specifying","still","stop","strongly","sub","substantially","successfully","sufficiently","suggest","sup","sure","take","taken","taking","tell","tends","th","thank","thanks","thanx","thats","that've","thence","thereafter","thereby","thered","therefore","therein","there'll","thereof","therere","theres","thereto","thereupon","there've","theyd","theyre","think","thou","though","thoughh","thousand","throug","throughout","thru","thus","til","tip","together","took","toward","towards","tried","tries","truly","try","trying","ts","twice","two","u","un","unfortunately","unless","unlike","unlikely","unto","upon","ups","us","use","used","useful","usefully","usefulness","uses","using","usually","v","value","various","'ve","via","viz","vol","vols","vs","w","want","wants","wasnt","way","wed","welcome","went","werent","whatever","what'll","whats","whence","whenever","whereafter","whereas","whereby","wherein","wheres","whereupon","wherever","whether","whim","whither","whod","whoever","whole","who'll","whomever","whos","whose","widely","willing","wish","within","without","wont","words","world","wouldnt","www","x","yes","yet","youd","youre","z","zero","a's","ain't","allow","allows","apart","appear","appreciate","appropriate","associated","best","better","c'mon","c's","cant","changes","clearly","concerning","consequently","consider","considering","corresponding","course","currently","definitely","described","despite","entirely","exactly","example","going","greetings","hello","help","hopefully","ignored","inasmuch","indicate","indicated","indicates","inner","insofar","it'd","keep","keeps","novel","presumably","reasonably","second","secondly","sensible","serious","seriously","sure","t's","third","thorough","thoroughly","three","well","wonder"]
    
    dfTrue = pd.read_csv('disastertweetsTrue.csv')
    dfFalse = pd.read_csv('disastertweetsFalse.csv')

    dfCloud1 = str(dfTrue['text'])
    dfCloud2 = str(dfFalse['text'])
    
    wordcloud1 = WordCloud(stopwords=stopwords_List,background_color="white").generate(dfCloud1)
    plt.imshow(wordcloud1, interpolation='bilinear')
    plt.axis("off")
    plt.tight_layout()
    plt.savefig('DTwordcloudTrue.png')
    plt.close()
    
    wordcloud2 = WordCloud(stopwords=stopwords_List,background_color="white").generate(dfCloud2)
    plt.imshow(wordcloud2, interpolation='bilinear')
    plt.axis("off")
    plt.tight_layout()
    plt.savefig('DTwordcloudFalse.png')
    plt.close()

if __name__=='__main__':
    main()

