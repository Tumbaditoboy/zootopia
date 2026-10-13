class Animal:
    def __init__(self, id, nombre, color, especie, cuidador, imagen):
        self.id = id
        self.nombre = nombre
        self.color = color
        self.especie = especie
        self.cuidador = cuidador
        self.imagen = imagen

    def __repr__(self):
        return f"<Animal {self.nombre} ({self.especie})>"