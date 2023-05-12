#FULL_CONCORDANCE
import re
import sys
import itertools
class concord:
    def __init__(self, input=None, output=None):
        self.input = input
        self.output = output
        if output!=None:
            self.__toOut()
            
    def __toOut(self):
        '''
        DESCRIPTION:
           Only called when the output file is given
        '''
        f = open(self.output, "w")
        outside = self.full_concordance()
        f.write('\n'.join(outside))       
    def __Exclusion(file):
        '''
        DESCRIPTION: 
           Removes the exclusion words from the file content and returns all the exclusion words in a string format      
        '''
        return "".join(list(itertools.takewhile(lambda line : not re.match("\"\"\"\"", line), file)))
    
    def __TupleCreater(capi_word, sente):
        '''
        DESCRIPTION: 
           Creates a tuple of (Key_word, start_of_index_of_keyword, sentence) and returns a list of tuples
        '''
        return [(capi_word, (re.search(r'\b' + capi_word + r'\b',s,re.IGNORECASE)).start(), s) for s in sente if(re.search(r'\b' + capi_word + r'\b', s ,re.IGNORECASE))]
    
    def __getSentences(file) -> list:
        '''
        DESCRIPTION: 
           Extracts the sentences from the file_content using list comprehensions and returns it
        '''
        return [line2.rstrip() for line2 in file]
    
    def __getKeys(s, excl):
        '''
        DESCRIPTION: 
           Extracts the keys from the file_content using list comprehensions and returns it
        '''
        return [x.upper() for i, x in enumerate(s.split()) if not re.search(r'\b' + x + r'\b', excl, re.IGNORECASE)]
    def __appendright(word, i, sentence):
        '''
        DESCRIPTION: 
           returns the sentence that fits in within the range of 30 by checking possible conditions
        '''
        String = ""
        i = i + len(word)-1
        rightout = (i+1) + (29-(len(word)-1))        
        if rightout+1>=len(sentence[i+1:]): #if the right of the sentence is within the range, we just append to the string
            String = sentence[i+1:]
        elif sentence[rightout]==' ': #if the rightout index is a space, append the right part of the sentence to the string 
            String = sentence[i+1:rightout]
        elif sentence[rightout+1]!=' ' and sentence[rightout]!=' ' and sentence[rightout-1]!=' ': #if the we are between the word then we are out of bounds
            sentence = sentence[i+1: rightout] #slice the sentence upto the rightout 
            index_of_space = sentence.rfind(" ")#find the last occurrence of space in the sliced sentence
            String = sentence[0:index_of_space]#append the sentence upto that last occurrence of space to get rid of the word that is out of range
        elif sentence[rightout]!=' ' and sentence[rightout+1]==' ':#if we reach the last character of the word in the sentence then that word should be appended
            String = sentence[i+1:rightout+1]
        elif sentence[rightout]!=' ' and sentence[rightout-1]==' ':#if we reach the beginning of a word and that goes out of bounds, should not be appended
            rightout-=1
            String = sentence[i+1: rightout]
        return String
    
    def __appendleft(word, i, sentence):
        '''
        DESCRIPTION: 
           returns the sentence that fits in within the range of 20 by checking possible conditions
        '''
        leftout = i-20
        String = ""
        if(leftout<=0): #if leftout goes too far left, then the left is within the range of the output
            String = sentence[0:i]
        elif(sentence[leftout]==' '): #if the leftout index is a space, append the left part of the sentence to the string
            String = sentence[leftout:i]
        elif sentence[leftout]!=' ' and sentence[leftout+1]==' ' and sentence[leftout-1]!=' ': #if we are at the beginning of the word in the sentence, then it's out of bounds
            String = sentence[leftout+2:i] #do not include that word
        elif sentence[leftout+1]!=' ' and sentence[leftout]!=' ' and sentence[leftout-1]!=' ':  #if the we are between the word then we are out of bounds
            sentence = sentence[leftout:i]#slice the sentence beginning from leftout
            index_of_space = sentence.index(" ")#index of the first occurence of space
            String = sentence[index_of_space+1: i]# start appending from that space
        elif sentence[leftout]!=' ' and sentence[leftout-1]==' ':#if leftout is not a space and leftout-1 is a space then we start appending from that index
            String = sentence[leftout:i]
        return " "*((30-len(String))-1) + String + word #append the spaces in the beginning of the sentences
    def __concordance_output(word, index, sent):
        return concord.__appendleft(word, index, sent) + concord.__appendright(word, index, sent) 
    
    def full_concordance():
        '''
        DESCRIPTION:
           calls all the helper functions present in the description
        '''
        if self.input!=None:
            f_contents = open(self.input, "r")
        else:
            f_contents = sys.stdin
        version = f_contents.readline()
        if(f_contents==None):
            print("file not found")
            quit()
        f_contents.readline()
        exclusion = concord.__Exclusion(f_contents)
        sentences = concord.__getSentences(f_contents)
        capitalize = list(map(lambda x: concord.__getKeys(x,exclusion), sentences))
        capitalize = list(dict.fromkeys(list(itertools.chain.from_iterable(capitalize))))
        capitalize.sort()
        new = list(map(lambda x: concord.__TupleCreater(x, sentences), capitalize))
        new = list(itertools.chain.from_iterable(new))
        return list(itertools.starmap(concord.__concordance_output, new))
