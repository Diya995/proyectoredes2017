#KEY = postgresql-closed-81267
import os

from flask import Flask
from flask import render_template
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['DEBUG'] = True

db = SQLAlchemy(app)

class So(db.Model):
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
    

    def __init__(self, kernel, release, nodename, kernelv, machine, processor, so, hardware):
	self.kernel = kernel
	self.release = release
	self.nodename = nodename
	self.kernelv = kernelv
	self.machine = machine
	self.processor = processor
	self.so = so
	self.hardware = hardware
	self.usser_logged = user_logged
	self.cpu_us = cpu_us
	self.cpu_sy = cpu_sy
	self.cpu_id = cpu_id
	self.cpu_wa = cpu_wa
	self.cpu_st = cpu_st
	self.mem_swpd = mem_swpd
	self.mem_free = mem_free
	self.mem_buff = mem_buff
	self.cache = cache
	self. swap_si =  swap_si
	self.swap_so = swap_so

    def __repr__(self): 
        return "<Os(id='%d', kernel='%s', release='%s', nodename='%s', kernelv='%s', machine='%s', processor='%s', so='%s', hardware='%s', usser_logged='%s', cpu_us='%s', cpu_sy='%s',cpu_id='%s', cpu_wa='%s', cpu_st='%s',mem_swpd='%s', mem_free='%s',  mem_buff='%s', cache='%s', swap_si='%s',swap_so='%s')>" % (self.id, self.kernel, self.release, self.nodename, self.kernelv, self.machine, self.processor, self.so, self.hardware, self.usser_logged, self.cpu_usself.cpu_sy, self.cpu_id, self.cpu_wa, self.cpu_st, self.mem_swpd, self.mem_free, self.mem_buff, self.cache, self.swap_si, self.swap_so)

        
@app.route('/')
def index():
	return render_template('index.html')
     
@app.route('/consultarEstadoMaquina')
def soShow():
	so = So.query.filter(So.id == 1).one()
	return render_template('so.html',so = so)


@app.route('/consultarEstadosDescargas')
def memShow():
	careers = So.query.all()
	return render_template('mem.html',carreras = careers)


@app.route('/robots.txt')
def robots():
	res = app.make_response('User-agent: *\nAllow: /')
	res.mimetype = 'text/plain'
	return res

if __name__ == '__main__':
	port = int(os.environ.get('PORT', 5000))
	app.run(host='0.0.0.0', port=port, debug=True)
