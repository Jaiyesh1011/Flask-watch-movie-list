from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///chess.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Chess(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    color = db.Column(db.String(20), nullable=False)

    def __repr__(self) -> str:
        return f'<Chess {self.name}>'
    

@app.route("/")
def hello_world():
    chess = Chess(name = "Chess", color = "black")
    db.session.add(chess)
    db.session.commit()
    return render_template("index.html")

@app.route("/show")
def products():
    all_products = Chess.query.all()
    print(all_products)
    return "those are my products"


if __name__ == "__main__":
    app.run(debug=True, port = 8000)