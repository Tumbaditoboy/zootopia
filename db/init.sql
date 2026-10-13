-- Crear la base de datos si no existe
CREATE DATABASE IF NOT EXISTS zoologico_db;
USE zoologico_db;

-- Crear la tabla de animales 
CREATE TABLE IF NOT EXISTS animales (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    color VARCHAR(50) NOT NULL,
    especie VARCHAR(100) NOT NULL,
    cuidador VARCHAR(100) NOT NULL,
    imagen VARCHAR(255) DEFAULT NULL
);