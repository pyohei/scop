from bottle import route, run, request
from converter import main as cnv


HTML_STRING = """
<html>
  <body>
    <form method="POST" action="/w">
      <div>
        <textarea name="base" cols=80 rows=40></textarea>
      </div>
      <input type="submit" value="convert">
    </form>
  </body>
</html>
"""


@route('/w', method=['GET', 'POST'])
def www():
    s = request.forms.get('base', '')
    if s:
        print cnv(s)
        return cnv(s)
    return HTML_STRING

run(host='127.0.9.9', port='11111', debug=True, reloader=True)
