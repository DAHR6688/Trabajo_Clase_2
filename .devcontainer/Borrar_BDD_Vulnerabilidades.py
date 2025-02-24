import psycopg2
from psycopg2 import sql

# Configuración de la conexión
host = 'localhost'  # Cambia esto a tu host de PostgreSQL
database = 'vulnerabilidades'  # Nombre de la base de datos
user = 'postgres'  # Nombre de usuario
password = 'postgres'  # Contraseña del usuario

# Conectar a la base de datos
try:
    connection = psycopg2.connect(
        host=host,
        database=database,
        user=user,
        password=password
    )

    cursor = connection.cursor()
    
    # Nombre de la tabla que deseas borrar
    table_name = 'nist_cves'

    # Crear la sentencia SQL para borrar la tabla
    drop_table_query = sql.SQL("DROP TABLE IF EXISTS {}").format(sql.Identifier(table_name))
    
    # Ejecutar la consulta
    cursor.execute(drop_table_query)
    
    # Confirmar los cambios
    connection.commit()
    print(f"Tabla '{table_name}' eliminada exitosamente.")

except Exception as e:
    print("Ocurrió un error:", e)

finally:
    # Cerrar la conexión y el cursor
    if cursor:
        cursor.close()
    if connection:
        connection.close()
