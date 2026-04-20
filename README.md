# Smart Task Manager

Un gestor de tareas inteligente basado en línea de comandos que permite agregar, listar, completar y eliminar tareas. Incluye una función de IA para desglosar tareas complejas en subtareas accionables.

## Características

- **Agregar tareas simples**: Crea tareas básicas con una descripción.
- **Agregar tareas complejas con IA**: Usa OpenAI para desglosar tareas complejas en 3-5 subtareas simples.
- **Listar tareas**: Muestra todas las tareas pendientes y completadas.
- **Completar tareas**: Marca una tarea como completada.
- **Eliminar tareas**: Borra una tarea de la lista.
- **Almacenamiento persistente**: Las tareas se guardan en un archivo JSON (`tasks.json`).

## Requisitos

- Python 3.7 o superior
- Clave de API de OpenAI (para la función de IA)
- Dependencias listadas en `requirements.txt`

## Instalación

1. Clona el repositorio:
   ```
   git clone <url-del-repositorio>
   cd TaskManager
   ```

2. Crea un entorno virtual (opcional pero recomendado):
   ```
   python -m venv venv
   # En Windows:
   venv\Scripts\activate
   # En macOS/Linux:
   source venv/bin/activate
   ```

3. Instala las dependencias:
   ```
   pip install -r requirements.txt
   ```

4. Configura la clave de API de OpenAI:
   - Crea un archivo `.env` en la raíz del proyecto.
   - Agrega tu clave de API:
     ```
     OPENAI_API_KEY=tu_clave_aqui
     ```

## Uso

Ejecuta el programa principal:
```
python main.py
```

Sigue el menú interactivo para gestionar tus tareas.

### Opciones del menú:
1. **Agregar tarea**: Ingresa una descripción para una tarea simple.
2. **Agregar tarea compleja (con IA)**: Ingresa una descripción compleja; la IA la desglosará en subtareas.
3. **Listar tareas**: Muestra todas las tareas.
4. **Completar tarea**: Ingresa el ID de la tarea a marcar como completada.
5. **Eliminar tarea**: Ingresa el ID de la tarea a eliminar.
6. **Salir**: Cierra la aplicación.

## Estructura del proyecto

- `main.py`: Punto de entrada de la aplicación.
- `task_manager.py`: Clase `TaskManager` para gestionar tareas.
- `ai_service.py`: Servicio de IA para desglosar tareas complejas usando OpenAI.
- `tasks.json`: Archivo de almacenamiento persistente de tareas.
- `requirements.txt`: Dependencias del proyecto.
- `tests/`: Directorio con pruebas unitarias.

## Pruebas

Ejecuta las pruebas con pytest:
```
pytest tests/
```

## Contribución

1. Haz un fork del proyecto.
2. Crea una rama para tu feature (`git checkout -b feature/nueva-funcion`).
3. Haz commit de tus cambios (`git commit -am 'Agrega nueva función'`).
4. Haz push a la rama (`git push origin feature/nueva-funcion`).
5. Abre un Pull Request.

## Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

## Contacto

Si tienes preguntas o sugerencias, abre un issue en el repositorio.