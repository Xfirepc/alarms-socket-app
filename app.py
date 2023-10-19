from flask import Flask, render_template, request
from flask_socketio import SocketIO
from random import random
from threading import Lock
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = '5p1d3rc0d3'
socketio = SocketIO(app, cors_allowed_origins='*')


def get_current_datetime():
    now = datetime.now()
    return now.strftime("%m/%d/%Y %H:%M:%S")

@socketio.on('connect', namespace='/')
def connect():
    print('Cliente conectado')

@socketio.on('disconnect', namespace='/')
def disconnect():
    print('Cliente desconectado', request.sid)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hook', methods=['POST'])
def hook():
    value = round(random() * 100, 3)
    socketio.emit('updateSensorData', {
        'value': value, 
        "date": get_current_datetime(), 
        "alarma": "Alerta ROJA"
    }, namespace='/')
    return 'Proceso de generación de datos iniciado'




if __name__ == '__main__':
    socketio.run(app)
