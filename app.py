import os

from flask import Flask
from flask import render_template
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['DEBUG'] = True

db = SQLAlchemy(app)

class Maquina(db.Model):
	id_so = db.Column(db.Integer, primary_key=True)
	kernel = db.Column(db.String(100), unique=True)
	release = db.Column(db.String(100), unique=True)
	nodename = db.Column(db.String(100), unique=True)
	kernelv = db.Column(db.String(100), unique=True)
	machine = db.Column(db.String(100), unique=True)
	processor = db.Column(db.String(100), unique=True)
	so = db.Column(db.String(100), unique=True)
	hardware = db.Column(db.String(100), unique=True)
	user_logged = db.Column(db.String(100), unique=True)
	cpu_us = db.Column(db.String(100), unique=True)
	cpu_sy  = db.Column(db.String(100), unique=True)
	cpu_id = db.Column(db.String(100), unique=True)
	cpu_wa = db.Column(db.String(100), unique=True)
	cpu_st = db.Column(db.String(100), unique=True)
	mem_swpd = db.Column(db.String(100), unique=True)
	mem_free = db.Column(db.String(100), unique=True)
	mem_buff  = db.Column(db.String(100), unique=True)
	cache = db.Column(db.String(100), unique=True)
	swap_si = db.Column(db.String(100), unique=True)
	swap_so  = db.Column(db.String(100), unique=True)
    

	def __init__(self, kernel, release, nodename, kernelv, machine, processor, so, hardware, user_logged, cpu_us, cpu_us, cpu_sy, cpu_id, cpu_wa, cpu_st, mem_swpd, mem_free, mem_buff, cache, swap_si, swap_s0):
		self.kernel = kernel
		self.release = release
		self.nodename = nodename
		self.kernelv = kernelv
		self.machine = machine
		self.processor = processor
		self.so = so
		self.hardware = hardware
		self.user_logged = user_logged
		self.cpu_us = cpu_us
		self.cpu_sy = cpu_sy
		self.cache = cache
		self. swap_si =  swap_si
		self.swap_so = swap_so


	def __repr__(self): 
    	return "<Maquina(id='%d', kernel='%s', release='%s', nodename='%s', kernelv='%s', machine='%s', processor='%s', so='%s', hardware='%s', user_logged='%s', cpu_us='%s', cpu_sy='%s',cpu_id='%s', cpu_wa='%s', cpu_st='%s',mem_swpd='%s', mem_free='%s',  mem_buff='%s', cache='%s', swap_si='%s',swap_so='%s')>" % (
		self.id, self.kernel, self.release, self.nodename, self.kernelv, self.machine, self.processor, self.so, self.hardware, self.user_logged, self.cpu_us, self.cpu_sy, self.cpu_id, self.cpu_wa, self.cpu_st, self.mem_swpd, self.mem_free, self.mem_buff, self.cache, self.swap_si, self.swap_so)

        
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
