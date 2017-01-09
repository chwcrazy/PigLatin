from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
    paragraph = "Hello World Allo"
    return 'PigLatin: ' + pigLatin(paragraph)

def pigLatin(paragraph):
    ''' 
    convert a paragraph string in pig latin
    '''

    if not isinstance(paragraph, basestring):
        raise ValueError("Input is not a string type")
    if paragraph == '':
        return ''
    arr = paragraph.split()
    res = []
    for s in arr:
        s = helper(s)
        res.append(s)
    return ' '.join(res)
        
def helper(s):
    ''' 
    convert a single-word string in pig latin
    '''
    
    if not s.isalpha():
        raise ValueError("Got a non-alpha string {}".format(s))
    if s[0].lower() in 'aeiou':
        return s + 'yay'
    if len(s) == 1:
        return s[0] + 'ay'
    return s[1:]+s[0]+'ay'

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)
