import os

from flask import Flask
from flask import render_template
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['DEBUG'] = True

db = SQLAlchemy(app)
        
class Descargas(db.Model):
    id_dt = db.Column(db.Integer, primary_key=True)
    magnet_link = db.Column(db.String(100), unique=True)
    iniciada = db.Column(db.String(100), unique=True)
    estado_descarga = db.Column(db.String(100), unique=True)

    def __init__(self,magnet_link,iniciada,estado_descarga):
        self.magnet_link = magnet_link
        self.iniciada = iniciada
        self.estado_descarga = estado_descarga

    def __repr__(self):
        return "<Descargas(id_dt='%d', magnet_link='%s', iniciada='%s', estado_descarga='%s')>" % (
        self.id_dt, self.magnet_link, self.iniciada, self.estado_descarga)   

@app.route('/')
def index():
	return render_template('index.html')
     
@app.route('/machine/show')
def machineShow():
	machine = Maquina.query.filter(Maquina.id == 1).one()
	return render_template('machine.html',machine = machine)


@app.route('/download/show')
def downloadShow():
	download = Descargas.query.filter(Descargas.id == 1).one()
	return render_template('download.html',download = download)


@app.route('/robots.txt')
def robots():
	res = app.make_response('User-agent: *\nAllow: /')
	res.mimetype = 'text/plain'
	return res

if __name__ == '__main__':
	port = int(os.environ.get('PORT', 5000))
	app.run(host='0.0.0.0', port=port, debug=True)
if __name__ == '__main__':
	port = int(os.environ.get('PORT', 5000))
	app.run(host='0.0.0.0', port=port, debug=True)
