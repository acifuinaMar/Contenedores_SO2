CREATE EXTENSION IF NOT EXISTS postgis;

CREATE TABLE puntos (
    id SERIAL PRIMARY KEY,
    nombre TEXT,
    descripcion TEXT,
    categoria TEXT,
    ubicacion GEOGRAPHY(POINT)
);

INSERT INTO puntos (nombre, descripcion, categoria, ubicacion)
VALUES
('Parque Central', 'Lugar turístico', 'cultural', ST_GeogFromText('POINT(-90.5133 14.6349)')),
('Gasolinera Uno', 'Servicio 24h', 'servicio', ST_GeogFromText('POINT(-90.5 14.63)')),
('Museo Nacional', 'Historia del país', 'cultural', ST_GeogFromText('POINT(-90.52 14.62)')),
('Restaurante X', 'Comida típica', 'gastronomico', ST_GeogFromText('POINT(-90.51 14.63)')),
('Parque Natural', 'Área verde', 'natural', ST_GeogFromText('POINT(-90.49 14.61)'));
