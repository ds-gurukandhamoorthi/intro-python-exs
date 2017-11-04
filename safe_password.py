import re
from spellchecker import build_lexicon

def safe_password(text):
    if len(text)<8:
        return False
    if not re.search('[0-9]', text):
        return False
    if not re.search('[A-Z]', text):
        return False
    if not re.search('[a-z]', text):
        return False
    if not re.search('[^a-zA-Z0-9]', text):
        return False
    return True

def safe_password_2(text):
    def rev(string):
        return ''.join(reversed(string))
    if len(text) < 8:
        return False
    lexicon = build_lexicon('../words.utf-8.txt')
    if text in lexicon or rev(text) in lexicon:
        return False
    if text[:-1] in lexicon or rev(text[:-1]) in lexicon:
        return False
    for i in range(1, len(text)-1):
        word1, word2 = text[:i], text[i:]
        if word1 in lexicon and word2 in lexicon:
            return False
        if rev(word1) in lexicon and rev(word2) in lexicon:
            return False
    return True



if __name__ == "__main__":
    assert safe_password('A12a$567')
    assert not safe_password_2('anonymous3') 
    assert not safe_password_2('helloworld') 
    assert not safe_password_2('dlrowolleh') 

 

