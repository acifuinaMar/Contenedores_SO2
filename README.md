# Sistema de Puntos de Interés Geoespaciales
## Descripción
Este proyecto consiste en una aplicación web que permite registrar y consultar puntos de interés con ubicación geográfica.
El sistema utiliza una arquitectura basada en contenedores, integrando una base de datos geoespacial, un backend con API REST y un proxy web.

## Arquitectura
El sistema está compuesto por:
- Base de datos: PostgreSQL + PostGIS
- Backend: FastAPI
- Proxy: Nginx
- Contenedores: Docker + Docker compose

Siguiendo el siguiente flujo:
Usuario -> Nginx -> Backend -> Base de datos

## Tecnologías utilizadas
- Python
- FastAPI
- PostgreSQL
- PostGIS
- Nginx
- Docker
- Docker Compose

## Requisitos del sistema
- Tener instalado Docker
- Tener instalado Docker compose

## ¿Cómo ejecutar el proyecto?
1. Clonar el repositorio.
```bash
git clone https://github.com/acifuinaMar/Contenedores_SO2.git
cd proyecto-poi
```
2. Levantar los contenedores.
```bash
docker-compose up --build
```
3. Acceder en el navegador a:
- Frontend: http://localhost/
- API Docs: http://localhost/docs

## Funcionalidades
- Registro de puntos de interés
- Listado de puntos
- Búsqueda por proximidad
- Filtro por categoría
- Interfaz web simple
- Persistencia de datos con volúmenes

## Endpoints principales
1. Obtener puntos
```bash
GET /puntos
```
2. Crear puntos
```bash
POST /puntos
```
3. Buscar por proximidad
```bash
GET /puntos/cercanos?lat=...&lon=...&radio=...
```
4. Filtrar por categoría
```bash
GET /puntos/categoria?categoria=...
```

## Persistencia
Se utiliza un volumen Docker (db_data) para almacenar los datos de la base de datos, garantizando que la información no se pierda al detener los contenedores.

## Observaciones importantes
- El sistema funciona de forma local
- No requiere servicios externos
- Los datos iniciales se cargan automáticamente
