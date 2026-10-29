import pytest
from app import app
from database import db
from app import AnimalModel

@pytest.fixture
def client():
    # Configuramos la app en modo de prueba
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    with app.test_client() as client:
        with app.app_context():
            # Crea las tablas en la base de datos de prueba antes de cada test
            db.create_all()
            yield client
            # Limpia y borra las tablas al terminar para mantener el entorno aislado
            db.session.remove()
            db.drop_all()

def test_index_route(client):
    """listado de animales correctamente (Código 200)"""
    response = client.get('/')
    assert response.status_code == 200
def test_add_animal(client):
    """Prueba(POST)"""
    response = client.post('/add', data={
        'nombre': '10.0',
        'color': 'Amarillo',
        'especie': 'Jirafa',
        'cuidador': 'Juan Perez',
        'imagen': 'jirafa.jpg'
    }, follow_redirects=True)
    
    assert response.status_code == 200
    
    # validación guardado
    with app.app_context():
        animal = AnimalModel.query.filter_by(nombre='10.0').first()
        assert animal is not None
        assert animal.especie == 'Jirafa'
        assert animal.cuidador == 'Juan Perez'

def test_delete_animal(client):
    """ Borrar (POST /delete/<id>)"""
    # Primero insertamos un animal directamente para asegurarnos de que exista
    with app.app_context():
        animal_prueba = AnimalModel(
            nombre='Simba', 
            color='Dorado', 
            especie='León', 
            cuidador='Carlos', 
            imagen='leon.jpg'
        )
        db.session.add(animal_prueba)
        db.session.commit()
        animal_id = animal_prueba.id

    # Ejecutamos la petición para eliminarlo mediante su ID
    response = client.post(f'/delete/{animal_id}', follow_redirects=True)
    assert response.status_code == 200

    # Comprobamos que el animal ya no existe en la base de datos
    with app.app_context():
        animal_eliminado = AnimalModel.query.get(animal_id)
        assert animal_eliminado is None