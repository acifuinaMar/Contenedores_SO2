from fastapi import FastAPI
from fastapi import Query
from pydantic import BaseModel
import psycopg2

app = FastAPI()

def get_connection():
    return psycopg2.connect(
        host="db",
        database="poi_db",
        user="user",
        password="password"
    )

@app.get("/")
def home():
    return {"mensaje": "API funcionando :D"}

@app.get("/puntos")
def obtener_puntos():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT nombre, categoria FROM puntos;")
    resultados = cursor.fetchall()

    cursor.close()
    conn.close()

    return {"puntos": resultados}
@app.get("/puntos/cercanos")
def puntos_cercanos(lat: float = Query(...), lon: float = Query(...), radio: float = Query(...)):
    conn = get_connection()
    cursor = conn.cursor()

    query = """
    SELECT nombre, categoria
    FROM puntos
    WHERE ST_DWithin(
        ubicacion,
        ST_GeogFromText(%s),
        %s
    );
    """

    punto = f"POINT({lon} {lat})"

    cursor.execute(query, (punto, radio))
    resultados = cursor.fetchall()

    cursor.close()
    conn.close()

    return {"puntos_cercanos": resultados}

class Punto(BaseModel):
    nombre: str
    descripcion: str
    categoria: str
    lat: float
    lon: float

@app.post("/puntos")
def crear_punto(punto: Punto):
    conn = get_connection()
    cursor = conn.cursor()

    query = """
    INSERT INTO puntos (nombre, descripcion, categoria, ubicacion)
    VALUES (%s, %s, %s, ST_GeogFromText(%s));
    """

    ubicacion = f"POINT({punto.lon} {punto.lat})"

    cursor.execute(query, (punto.nombre, punto.descripcion, punto.categoria, ubicacion))
    conn.commit()

    cursor.close()
    conn.close()

    return {"mensaje": "Punto creado correctamente"}

@app.get("/puntos/categoria")
def puntos_por_categoria(categoria: str):
    conn = get_connection()
    cursor = conn.cursor()

    query = "SELECT nombre, categoria FROM puntos WHERE categoria = %s;"
    cursor.execute(query, (categoria,))
    resultados = cursor.fetchall()

    cursor.close()
    conn.close()

    return {"puntos": resultados}
