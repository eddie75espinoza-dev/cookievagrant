import os
import sys
import re

def validate_configurations():
    """
    Valida configuraciones clave del proyecto generado.
    """
    # Validar memoria
    try:
        memory = int('{{ cookiecutter.memory }}')
        if memory > 12288:
            print("Error: La memoria asignada supera el límite permitido de 12GB.")
            sys.exit(1)
    except ValueError:
        print("Error: El valor de memoria no es un número válido.")
        sys.exit(1)

    # Validar versión de Ubuntu
    ubuntu_version = '{{ cookiecutter.ubuntu_version }}'
    if ubuntu_version not in ['20.04', '22.04', '24.04']:
        print(f"Error: La versión de Ubuntu {ubuntu_version} no está soportada.")
        sys.exit(1)

    # Validar tamaño del disco
    disk = '{{ cookiecutter.disk_size }}'
    match = re.match(r'(\d+)(GB|gb|Gb)', disk)
    if not match:
        print("Error: El tamaño de disco debe estar en formato numérico seguido de 'GB' (por ejemplo, '20GB').")
        sys.exit(1)
    disk_size = int(match.group(1))
    if disk_size < 10:
        print("Error: El tamaño de disco debe ser de al menos 10GB.")
        sys.exit(1)

    print("Validaciones completadas con éxito.")

def main():
    print("Iniciando post-generación...")
    validate_configurations()
    print("Post-generación finalizada. ¡Tu proyecto está listo!")

if __name__ == '__main__':
    main()
