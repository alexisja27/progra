import mysql.connector


def connect():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="bd1"
    )
    return connection

def create_user(conn, nombre, edad):
    cursor = conn.cursor()
    query = 'insert into usuarios (nombre, edad) values (%s, %s)'
    data = (nombre, edad)
    cursor.execute(query, data)
    conn.commit()
    cursor.close()

def get_all_usuarios(conn):
    cursor = conn.cursor()
    cursor.execute('select * from usuarios')
    usuarios = cursor.fetchall()
    cursor.close()
    return usuarios

def delete_user(conn, id_usuario):
    cursor = conn.cursor()
    query = 'delete from usuarios where id_usuario = %s'
    data = (id_usuario,)
    cursor.execute(query, data)
    conn.commit()
    cursor.close()

def update_user(conn, id ,nombre, edad):
    cursor = conn.cursor()
    query = 'update usuarios set nombre=%s, edad=%s where id_usuario = %s'
    data = (nombre, edad, id )
    cursor.execute(query, data)
    conn.commit()
    cursor.close()

def mostrar_menu():
    print("\n--- Menú ---")
    print("1. Crear usuario")
    print("2. Leer usuarios")
    print("3. Actualizar usuario")
    print("4. Eliminar usuario")
    print("5. Salir")

def main():
    conn=connect()
    while True:
        mostrar_menu()
        opcion= input("seleccione una opción :")
        if opcion == "1":
            nombre=input("ingrese el nombre del usuario:")
            edad=int(input("ingrese la edad el usuario:"))
            create_user(conn,nombre,edad)
            print("usuario creado correctamente.")
        elif opcion == "2":
            usuarios=get_all_usuarios(conn)
            if usuarios:
                print("\n--- usuarios ---")
                for usuario in usuarios:
                    print(F"ID= {usuario[0]}, nombre: {usuario[1]}, edad: {usuario[2]}")
            else:
                print("no hay usuarios registrados")
        elif opcion == "3":
            id_usuario=int(input("ingrese el id del usuario a actualizar:"))
            nombre=input("ingrese el nuevo nombre del usuario:")
            edad=int(input("ingrese la edad nueva del usuario:"))
            update_user(conn, id_usuario, nombre, edad)
            print("usuario actualizado correctamente")
        elif opcion == "4":
            id_usuario=int(input("ingrese el ID del usuario a actualizar"))
            delete_user(conn, id_usuario)
            print("usuario eliminado correctamente")
        elif opcion == "5":
            print("¡hasta luego!")
            break
        else:
            print("opcion invalida, coloque una opcion valida")
    conn.close()
if __name__ == "__main__":
    main()



