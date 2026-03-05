# 📘 Glosario de Comandos Git y Entornos

Guía rápida de comandos esenciales para la gestión de proyectos, resolución de conflictos de versiones y sincronización con GitHub.

## 🐍 Gestión de Entornos Virtuales (Python)
*Aislar las librerías para evitar conflictos entre proyectos (como Flet vs Open-WebUI).*

- `python -m venv .venv`: Crea un nuevo entorno virtual en la carpeta actual llamado `.venv`.
- `.\.venv\Scripts\Activate.ps1`: **(Windows PowerShell)** Activa el entorno virtual. Aparecerá `(.venv)` en la terminal.
- `deactivate`: Sale del entorno virtual actual y vuelve al Python global de Windows.
- `pip list`: Muestra todos los paquetes instalados en el entorno activo.
- `pip install -r requirements.txt`: Instala todas las dependencias listadas en un archivo de texto.

## 📂 Configuración Inicial y Exclusión
- `git init`: Inicializa la carpeta actual como un repositorio local de Git.
- `.gitignore`: Archivo de texto donde se listan carpetas y archivos que **no** deben subirse a GitHub (ej: `.venv/`, `__pycache__/`, `.env`).
- `git add .`: Prepara todos los archivos nuevos o modificados para el siguiente commit.

## 🌿 Gestión de Ramas (Branches)
- `git branch`: Lista las ramas locales. La que tiene el `*` es la activa.
- `git branch -m Vieja Nueva`: Renombra la rama actual (ej: de `Main` a `main`).
- `git branch -M main`: Fuerza el renombrado de la rama actual a `main` y la establece como principal.
- `git checkout nombre-rama`: Cambia de una rama a otra.
- `git merge nombre-rama`: Fusiona el contenido de "nombre-rama" dentro de la rama donde estás parado.
- `git branch -d nombre-rama`: Borra una rama localmente (solo si ya fusionaste sus cambios).

## 🚀 Sincronización con GitHub
- `git remote add origin URL`: Vincula tu repositorio local con el repositorio remoto en GitHub.
- `git commit -m "mensaje"`: Crea un punto de guardado con una descripción de los cambios.
- `git push -u origin main`: Sube los cambios a GitHub y vincula la rama local con la remota.
- `git push origin --delete nombre-rama`: Elimina una rama directamente del servidor de GitHub.
- `git pull`: Descarga y fusiona los cambios más recientes desde GitHub a tu PC.

## 🧹 Limpieza y Caché
- `git rm -r --cached archivo/carpeta`: Elimina un archivo del rastreo de Git (se borra de GitHub) pero **lo mantiene intacto** en tu computadora. Útil si subiste el `.venv` o archivos `.env` por error.
- `git status`: Muestra el estado actual: archivos modificados, nuevos o listos para el commit.

## 🛠️ Comandos de Terminal Útiles
- `cd "ruta/de/carpeta"`: Cambia el directorio de trabajo.
- `ls` o `dir`: Lista los archivos dentro de la carpeta actual.
- `where.exe pip`: Muestra la ruta del ejecutable de pip activo (útil para verificar si estás dentro o fuera de un entorno).

## 🔍 Diagnóstico: ¿Dónde estoy parado?
- `git status`: El comando más importante. Te dice en qué rama estás, qué archivos han cambiado y si hay algo pendiente por subir.
- `git log --oneline -n 5`: Muestra los últimos 5 puntos de guardado (commits) para saber qué es lo último que hiciste.
- `git remote -v`: Muestra a qué URL de GitHub está conectado tu proyecto local.

## 🔀 Flujo de Ramas y Fusión
- `git checkout nombre-rama`: Salta de la rama actual a la rama especificada.
- `git checkout -b nueva-rama`: Crea una rama nueva y salta a ella automáticamente en un solo paso.
- `git merge nombre-rama`: Trae los cambios de "nombre-rama" a la rama donde estás parado actualmente.

## 📥 Pull y Actualización (Traer de GitHub)
- `git pull origin main`: Descarga los cambios de GitHub y los mezcla con tu código local.
- `git fetch --all`: Descarga la información de GitHub pero **no** toca tu código; solo te avisa si hay cambios nuevos.
- `git reset --hard origin/main`: **¡CUIDADO! (Pull Forzado)** Borra todo lo que tengas en tu PC y lo deja exactamente igual a lo que hay en GitHub. Útil si arruinaste tu código local y quieres empezar desde la última versión que subiste.

## 📤 Push y Pull Requests (Subir a GitHub)
- `git push origin main`: Sube tus cambios normales a la rama principal.
- `git push -f origin main`: **¡CUIDADO! (Push Forzado)** Sobrescribe GitHub con lo que tienes en tu PC. Se usa para arreglar errores graves de historial, pero puede borrar el trabajo de otros.
- **Pull Request (PR):** No es un comando de consola, se hace en la web de GitHub. Es la petición formal para que tus cambios en una rama (ej. `rama-flet-1`) se acepten y se unan a la rama `main`.

## 🛠️ Corrección de Errores Rápidos
- `git checkout -- archivo.py`: Deshace los cambios que hiciste en un archivo y lo devuelve a como estaba en el último commit (ideal si borraste algo sin querer).
- `git commit --amend -m "Nuevo mensaje"`: Cambia el mensaje del último commit que hiciste (siempre que no lo hayas subido aún).