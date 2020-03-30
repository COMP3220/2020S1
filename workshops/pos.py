from bottle import Bottle, route, post, run, request, template
from nltk import word_tokenize, sent_tokenize, pos_tag

import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

app = Bottle()

@app.route('/')
def root():
    return """
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <title>My Part of Speech Tagger</title>
</head>
<body>
<h1>My Part of Speech Tagger</h1>
<p>Type or paste your text below</p>
<form method="post">
<textarea name="text" rows="10" cols="50">
Type your text here
</textarea>
<input type="submit"/>
</form>
</body>
</html>
    """

@app.post('/')
def postroot():
    if 'text' in request.forms:
        text = request.forms['text']
        sentences = sent_tokenize(text)
        result = " ".join(w+'/'+t for s in sent_tokenize(text)
                          for (w,t) in pos_tag(word_tokenize(s)))
    else:
        text = 'Type your text here'
        result = ''
    return template("""
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <title>My Part of Speech Tagger</title>
</head>
<body>
<h1>My Part of Speech Tagger</h1>
<p>Type or paste your text below</p>
<form method="post">
<textarea name="text" rows="10" cols="50">
{{text}}
</textarea>
<input type="submit"/>
</form>
<hr>
<p>The tagged text is</p>
<p>{{tagged}}
</body>
</html>
    """, text=text, tagged=result)

if __name__ == "__main__":
    run(app, host='localhost', port=8080)
