CREATE DATABASE IF NOT EXISTS TP_BACKEND;
USE TP_BACKEND;

CREATE TABLE  IF NOT EXISTS partidos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    equipo_local VARCHAR(100) NOT NULL,
    equipo_visitante VARCHAR(100) NOT NULL,
    fecha DATE NOT NULL,
    fase ENUM('grupos', 'dieciseisavos', 'octavos', 'cuartos', 'semis', 'final') NOT NULL,
    goles_local INT,
    goles_visitante INT
);

