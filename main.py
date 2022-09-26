# -----------------------------------------------------------------------------
# BIBLIOTECAS
# -----------------------------------------------------------------------------
from flask import Flask, render_template, request, Response, g
import sqlite3

# -----------------------------------------------------------------------------
# VARIÁVEIS
# -----------------------------------------------------------------------------

DB_URL = "enterprise.db"
users = [{"username":"Francine","secret":"admin1234"}]

# -----------------------------------------------------------------------------
# FUNÇÕES
# -----------------------------------------------------------------------------

@app.before_request
def before_request():
    conn = sqlite3.connect(DB_URL)
    g.conn = conn

@app.teardown_request
def after_request(exception):
    if g.conn is not None:
        g.conn.close()

def query_employers_to_dict(conn,query):
    cursor = conn.cursor()
    conn.execute(query)
    employers_dict = [{'titulo':row[0],'link':row[2]}
                      for row in cursor.fetchall()]
    return employers_dict

def check_user(username,secret):
    for user in users:
        if (user["username"]==username) and (user["secret"]==secret):
            return True
    return False

# -----------------------------------------------------------------------------
# PRINCIPAL FUNÇÃO DO PROJETO
# -----------------------------------------------------------------------------

app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/links")
def get_links():
    query = """
        SELECT titulo, link
        FROM lista;
    """
    employers_dict = query_employers_to_dict(g.conn,query)
    return {"lista": employers_dict}

@app.route("/meuslinks")
def meuslinks():
    return render_template("meuslinks.html")

#----colocar o site no ar
if __name__ == "__main__":
    app.run(debug=True)
