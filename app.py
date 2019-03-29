from flask import Flask, render_template, url_for, request, session
from flask_bootstrap import Bootstrap
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# setup CORS
cors = CORS(app, resources={
  #r"/api/*": {"origin": "*"}
  r"/*": { "origin": "*" }
})

# setup Bootstrap
Bootstrap(app)

@app.route('/', methods=['GET', 'POST'])
def index():
  return render_template('index.htm')

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080, debug=True)
