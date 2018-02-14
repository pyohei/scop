"""Simple string converter main porcess."""
from bottle import route, run, request, template, static_file
from converter import load_choices
from converter import convert


HTML_STRING = """
<html>
  <head>
    <link rel="stylesheet" type="text/css" href="./static/milligram.min.css">
  <body>
    <h1>Simple String Converter</h1>
    <form method="POST" action="/">
      <div>
        <div>
            Before
            <textarea name="base" cols=50 rows=40>{{base}}</textarea>
        </div>
        <div>
            <select name="choice">
            % for c in choices:
                <option value="{{c}}">{{c}}</option>
            % end
            </select>
            <input type="submit" value="convert">
        </div>
        <div>
            After
            <textarea name="result" cols=50 rows=40>{{result}}</textarea>
        </div>
      </div>
    </form>
  </body>
</html>
"""


@route('/', method=['GET', 'POST'])
def www():
    s = request.forms.get('base', '')
    c = request.forms.get('choice', '')
    c_str = ''
    if s:
        c_str = convert(s, c)
    embeded_texts = {'base': s,
                     'result': c_str,
                     'choices': load_choices()}
    return template(HTML_STRING, embeded_texts)


@route('/static/<file_path:path>')
def static(file_path):
    return static_file(file_path, root='./static')

run(host='127.0.0.1', port='9999', debug=True, reloader=True)
