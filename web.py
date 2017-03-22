from bottle import route, run, request, template
from converter import main as cnv


HTML_STRING = """
<html>
  <head>
    <style type="text/css">
    <!--
      .box {display: inline;}
    -->
    </style>
  <body>
    <h1>Simple String Converter</h1>
    <form method="POST" action="/">
      <div>
        <div class="box">
            <textarea name="base" cols=50 rows=40>{{base}}</textarea>
        </div>
        <div class="box">
           <input type="submit" value="convert">
        </div>
        <div class="box">
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
    c_str = ''
    if s:
        c_str = cnv(s)
    embeded_texts = {'base': s,
                     'result': c_str}
    return template(HTML_STRING, embeded_texts)

run(host='127.0.0.1', port='9999', debug=True, reloader=True)
