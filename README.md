# Inventario VYP

## Requisitos
* Python
* VueJs
* MySQL

## Pasos para la ejecución
1. Clonar el repositorio
2. Acceder a la carpeta server
    ```
    cd server
    ```
3. Crear un entorno virtual de python
    ```
    python -m venv env
    ```
4. Instalar las dependencias necesarias que estan en el archivo "requierements.txt"
    ```
    pip install -r requirements.txt
    ```
5. Ir al archivo config.py ubicado en la carpeta database dentro de server y cambiar las credenciales de la base de datos ubicadas en la linea #4.
    ```
    "connections": {"default": "mysql://"nombre de usuario":"contraseña del usuario"@localhost:3306/gatewayti"},
    ```
6. Ejecuar los comando para las migraciones.
    ```
    aerich migrate
    aerich upgrade
    ```

7. Ejecutar el servidor con el siguiente comando:
    ```
    uvicorn app:app --reload
    ```

8. Ahora nos movemos a la carpeta "client".
    ```
    cd client
    ```
9. Ejecutamos npm install o yarn dependiendo el caso para instalar las dependencias de VueJs.

10. Corremos el cliente.
    ```
    npm run dev o yarn serve
    ```
11. Para accerder a la plataforma debera registrarse en el apartado correspondiente.