from flask import Flask, render_template, request, redirect, url_for, flash
from database import db, init_db

app = Flask(__name__)
app.secret_key = 'clave_flash'

# Inicializamos la base de datos separada
init_db(app)

# Modelo de la base de datos mapeado a la tabla 
class AnimalModel(db.Model):
    __tablename__ = 'animales'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    color = db.Column(db.String(50), nullable=False)
    especie = db.Column(db.String(100), nullable=False)
    cuidador = db.Column(db.String(100), nullable=False)
    imagen = db.Column(db.String(255), nullable=True)

@app.route('/')
def index():
    todos_los_animales = AnimalModel.query.all()
    return render_template('index.html', animales=todos_los_animales)


@app.route('/add', methods=['POST'])
def add_animal():
    nombre = request.form['nombre']
    color = request.form['color']
    especie = request.form['especie']
    cuidador = request.form['cuidador']
    imagen = request.form['imagen']

    nuevo_animal = AnimalModel(
        nombre=nombre, 
        color=color, 
        especie=especie, 
        cuidador=cuidador, 
        imagen=imagen
    )
    
    db.session.add(nuevo_animal)
    db.session.commit()
    flash('Animal agregado con éxito :D', 'success')
    return redirect(url_for('index'))


@app.route('/edit/<int:id>', methods=['POST'])
def edit_animal(id):
    animal = AnimalModel.query.get_or_404(id)
    
    animal.nombre = request.form['nombre']
    animal.color = request.form['color']
    animal.especie = request.form['especie']
    animal.cuidador = request.form['cuidador']
    animal.imagen = request.form['imagen']

    db.session.commit()
    flash('Datos actualizados correctamente :S', 'success')
    return redirect(url_for('index'))


@app.route('/delete/<int:id>', methods=['POST'])
def delete_animal(id):
    animal = AnimalModel.query.get_or_404(id)
    db.session.delete(animal)
    db.session.commit()
    flash('Animal eliminado :O', 'info')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)