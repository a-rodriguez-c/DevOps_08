import psycopg2
import time

connections = []
max_attempts = 30  # Número de conexiones a intentar (debe ser mayor que max_connections)

try:
    for i in range(1, max_attempts + 1):
        conn = psycopg2.connect(
            dbname='blacklist_db',
            user='postgres',
            password='postgres',  # Reemplaza con tu contraseña si es diferente
            host='blacklist_db',     # O el host adecuado según tu entorno
            port='5432'           # O el puerto correspondiente
        )
        connections.append(conn)
        print(f"Conexión #{i} abierta")
        time.sleep(0.1)  # Pausa breve para no saturar inmediatamente
except Exception as e:
    print(f"Error al abrir la conexión #{i}: {e}")
finally:
    input("Presiona Enter para cerrar todas las conexiones y salir...")
    # Cierra todas las conexiones
    print(f"cierro {len(connections)} conexiones")
    for conn in connections:
        conn.close()
        print("Conexión cerrada")

# python stress_test_connections.py