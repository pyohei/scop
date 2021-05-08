"""Simple string converter main porcess."""
from bottle import route, run, request, template, static_file
from converter import load_choices
from converter import convert


HTML_STRING = """
<html>
  <head>
    <link rel="stylesheet" type="text/css" href="./static/milligram.min.css">
    <style type="text/css">
    <!--
      .box {display: inline-block;}
      .box-block {display: block;}
      .input-area {width: 300px; height: 600px;}
      .center {display: inline-block; text-align: center;}
    -->
    </style>
  <body>
    <form method="POST" action="/">
      <div class="container box-block center">
        <h1>Simple String Converter</h1>
        <div class="box">
            <select name="choice">
            % for c in choices:
                <option value="{{c}}">{{c}}</option>
            % end
            </select>
        </div>
        <div class="box">
            <input type="submit" value="convert">
        </div>
      </div>
      <div class="container box-block center">
        <div class="box">
          <div>
            Before
          </div>
          <div>
            <textarea name="base" class="input-area" cols=20 rows="50">{{base}}</textarea>
          </div>
        </div>
        <div class="box">
          <div>
            After
          </div>
          <div>
            <textarea class="input-area" name="result" cols=20 rows=50>{{result}}</textarea>
          </div>
        </div>
      </div>
    </form>
  </body>
</html>
"""


@route("/", method=["GET", "POST"])
def www():
    """Main page url process.

    This system pass only this url.
    """
    s = request.forms.get("base", "")
    c = request.forms.get("choice", "")
    c_str = ""
    if s:
        c_str = convert(s, c)
    embeded_texts = {"base": s, "result": c_str, "choices": load_choices()}
    return template(HTML_STRING, embeded_texts)


@route("/static/<file_path:path>")
def static(file_path):
    """Static file url setting.

    This route uses for static file(css).
    """
    return static_file(file_path, root="./static")


# Run
run(host="127.0.0.1", port="9999", debug=True, reloader=True)
