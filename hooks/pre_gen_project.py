# pre_gen_project.py
UBUNTU_TO_BOX = {
    "20.04": "focal64",
    "22.04": "jammy64",
    "24.04": "noble64"
}

# Verificar si la versión de Ubuntu seleccionada es válida
if "{{ cookiecutter.ubuntu_version }}" not in UBUNTU_TO_BOX:
    raise ValueError("Versión de Ubuntu no soportada. Use 20.04, 22.04 o 24.04.")

# Asigna automáticamente el nombre de la caja basado en la versión
box_name = UBUNTU_TO_BOX["{{ cookiecutter.ubuntu_version }}"]

# Sobrescribir directamente el valor de `box_name` en el contexto
from cookiecutter.main import cookiecutter
cookiecutter.context['cookiecutter']['box_name'] = box_name
