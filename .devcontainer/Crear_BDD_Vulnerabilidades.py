import psycopg2
import json
from datetime import datetime

# Paso 1: Crear la base de datos y la tabla desde Python
def create_database():
    try:
        # Conexión al servidor PostgreSQL (sin especificar una base de datos)
        conn = psycopg2.connect(
            user="postgres",  # Usuario predeterminado
            password="postgres",
            host="localhost",
            port="5432"
        )
        conn.autocommit = True  # Necesario para crear una base de datos
        cursor = conn.cursor()

        # Crear la base de datos "vulnerabilidades" si no existe
        cursor.execute("SELECT datname FROM pg_database WHERE datname='vulnerabilidades';")
        if not cursor.fetchone():
            cursor.execute("CREATE DATABASE vulnerabilidades;")
            print("Base de datos 'vulnerabilidades' creada correctamente.")
        else:
            print("La base de datos 'vulnerabilidades' ya existe.")
            # Conectar a la nueva base de datos
            conn = psycopg2.connect(database="vulnerabilidades",user="postgres",password="postgres",host="localhost",port="5432")
            cursor = conn.cursor()

            # Crear la tabla "NIST_CVEs" si no existe
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS NIST_CVEs (
                id SERIAL PRIMARY KEY,
                cve_id TEXT,
                Published TEXT,
                LastModified TEXT,
                Description TEXT,
                cvss_v31_score TEXT,
                attackVector TEXT,   
                attackComplexity TEXT,
                privilegesRequired TEXT,
                userInteraction TEXT,
                scope TEXT,
                confidentialityImpact TEXT,
                integrityImpact TEXT,
                availabilityImpact TEXT
            );
            """)
            print("Tabla 'NIST_CVEs' creada correctamente.")
            conn.commit()
            cursor.close()
            conn.close()  

        # Confirmar cambios y cerrar la conexión
        
    except Exception as e:
        print(f"Error al crear la tabla: {e}")

if __name__ == "__main__":
    create_database()  # Crear base de datos y tabla