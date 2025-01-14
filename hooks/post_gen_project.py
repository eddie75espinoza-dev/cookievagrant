### 2. Archivo `hooks/post_gen_project.py`
# Este script ejecuta tareas adicionales después de generar el proyecto. Por ejemplo, valida configuraciones y prepara el entorno.

import os
import sys

def validate_configurations():
    """
    Valida configuraciones clave del proyecto generado.
    """
    memory = int('{{ cookiecutter.memory }}')
    if memory > 12288:
        print("Error: La memoria asignada supera el límite permitido de 12GB.")
        sys.exit(1)

    ubuntu_version = '{{ cookiecutter.ubuntu_version }}'
    if ubuntu_version not in ['22.04', '24.04']:
        print(f"Error: La versión de Ubuntu {ubuntu_version} no está soportada.")
        sys.exit(1)

    print("Validaciones completadas con éxito.")

def main():
    print("Iniciando post-generación...")
    validate_configurations()
    print("Post-generación finalizada. ¡Tu proyecto está listo!")

if __name__ == '__main__':
    main()
