from conexion import Conexion
from persona import Persona


class PersonaDAO:
    MOSTRAR = "SELECT * FROM users"
    REGISTRAR = "INSERT INTO users(no_colaborador, nombre, apellido_paterno, apellido_materno, fecha_ingreso) VALUES (%s. %s, %s, %s, %s)"
    ACTUALIZAR = "UPDATE users SET nombre = %s WHERE no_colaborador = %s"
    ELIMINAR = "DELETE FROM users WHERE no_colaborador = %s"

    @classmethod
    def mostrar(cls):
        
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            cursor.execute(cls.MOSTRAR)
            registros = cursor.fetchall()
            # Mapeo Clase-Tabla
            usuarios = []
            for registro in registros:
                usuario = Persona(registro[0],
                                  registro[1],
                                  registro[3],
                                  registro[4],
                                  registro[5]
                                  )
                usuarios.append(usuario)
            return usuarios

        except Exception as e:
            print(f'Ocurrio un error al mostrar usuarios: {e}')

        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

    @classmethod
    def insertar(cls):
        conexion = None
        
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            cursor.execute(cls.REGISTRAR)
            registros = cursor.fetchall()
            # Mapeo Clase-Tabla
            usuarios = []
            for registro in registros:
                usuario = Persona(registro[0],
                                  registro[1],
                                  registro[3],
                                  registro[4],
                                  registro[5]
                                  )
                usuarios.append(usuario)
            return usuarios
        
        except Exception as e:
            print(f'Ocurrio un error al mostrar usuarios: {e}')
        
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)
        

if __name__ == "__main__":
    usuarios = PersonaDAO.mostrar()
    for usuario in usuarios:
        print(usuario)
