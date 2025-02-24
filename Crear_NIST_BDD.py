import psycopg2
import json
from datetime import datetime

# Paso 1: Crear la base de datos y la tabla desde Python
def create_database_and_table():
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

        # Crear la base de datos "Vulnerabilidades" si no existe
        cursor.execute("SELECT datname FROM pg_database WHERE datname='Vulnerabilidades';")
        if not cursor.fetchone():
            cursor.execute("CREATE DATABASE Vulnerabilidades;")
            print("Base de datos 'Vulnerabilidades' creada correctamente.")
        else:
            print("La base de datos 'Vulnerabilidades' ya existe.")

        # Cerrar la conexión inicial
        cursor.close()
        conn.close()

        # Conectar a la nueva base de datos
        conn = psycopg2.connect(
            database="Vulnerabilidades",
            user="postgres",
            password="postgres",
            host="localhost",
            port="5432"
        )
        cursor = conn.cursor()

        # Crear la tabla "NIST_CVEs" si no existe
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS NIST_CVEs (
            cve_id SERIAL PRIMARY KEY,
            Published TIMESTAMP,
            LastModified TIMESTAMP,
            Description TEXT,
            cvss_v31_score VARCHAR(15),
            attackVector VARCHAR(15),               
            attackComplexity VARCHAR(15),
            privilegesRequired VARCHAR(15),
            userInteraction VARCHAR(15),
            scope VARCHAR(15),
            confidentialityImpact VARCHAR(15),
            integrityImpact VARCHAR(15),
            availabilityImpact VARCHAR(15)
        );
        """)
        print("Tabla 'NIST_CVEs' creada correctamente.")

        # Confirmar cambios y cerrar la conexión
        conn.commit()
        cursor.close()
        conn.close()

    except Exception as e:
        print(f"Error al crear la base de datos o la tabla: {e}")

# Paso 2: Insertar datos estructurados en la tabla
def insert_NIST_CVEs():
    try:
        # Conectar a la base de datos
        conn = psycopg2.connect(
            database="Vulnerabilidades",
            user="postgres",
            password="postgres",
            host="localhost",
            port="5432"
        )
        cursor = conn.cursor()

        # Insertar registros en la tabla
        cursor.executemany("""
        INSERT INTO NIST_CVEs (timestamp, ip_address, event_type, description)
        VALUES (%s, %s, %s, %s);
        """, logs)

        # Confirmar cambios y cerrar la conexión
        conn.commit()
        print("Datos estructurados insertados correctamente.")
        cursor.close()
        conn.close()

    except Exception as e:
        print(f"Error al insertar datos estructurados: {e}")

# Ejecutar todas las funciones
if __name__ == "__main__":
    create_database_and_table()  # Crear base de datos y tabla
    insert_NIST_CVEs()     # Insertar datos estructurados