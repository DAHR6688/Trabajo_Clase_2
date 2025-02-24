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

        # Crear la base de datos "Data_Malware" si no existe
        cursor.execute("SELECT datname FROM pg_database WHERE datname='Data_Malware';")
        if not cursor.fetchone():
            cursor.execute("CREATE DATABASE Data_Malware;")
            print("Base de datos 'Data_Malware' creada correctamente.")
        else:
            print("La base de datos 'Data_Malware' ya existe.")

        # Cerrar la conexión inicial
        cursor.close()
        conn.close()

        # Conectar a la nueva base de datos
        conn = psycopg2.connect(
            database="Data_Malware",
            user="postgres",
            password="postgres",
            host="localhost",
            port="5432"
        )
        cursor = conn.cursor()

        # Crear la tabla "Tarea_malware" si no existe
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Tarea_malware (
            id SERIAL PRIMARY KEY,
            timestamp TIMESTAMP NOT NULL,
            ip_address VARCHAR(15),
            event_type VARCHAR(50),
            description TEXT
        );
        """)
        print("Tabla 'Tarea_malware' creada correctamente.")

        # Confirmar cambios y cerrar la conexión
        conn.commit()
        cursor.close()
        conn.close()

    except Exception as e:
        print(f"Error al crear la base de datos o la tabla: {e}")

# Paso 2: Insertar datos estructurados en la tabla
def insert_Tarea_malware():
    try:
        # Conectar a la base de datos
        conn = psycopg2.connect(
            database="Data_Malware",
            user="postgres",
            password="postgres",
            host="localhost",
            port="5432"
        )
        cursor = conn.cursor()

        # Datos de ejemplo para insertar
        logs = [
            (datetime(2025, 2, 22, 10, 0, 0), "192.168.1.10", "login_failed", "Intento de inicio de sesión fallido desde IP 192.168.1.10"),
            (datetime(2025, 2, 22, 10, 5, 0), "192.168.1.15", "access_denied", "Acceso denegado a recurso crítico")
        ]

        # Insertar registros en la tabla
        cursor.executemany("""
        INSERT INTO Tarea_malware (timestamp, ip_address, event_type, description)
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
    insert_Tarea_malware()     # Insertar datos estructurados