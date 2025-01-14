# pre_gen_project.py
UBUNTU_TO_BOX = {
    "20.04": "focal64",
    "22.04": "jammy64",
    "24.04": "noble64"
}

if "{{ cookiecutter.ubuntu_version }}" not in UBUNTU_TO_BOX:
    raise ValueError("Versión de Ubuntu no soportada. Use 20.04, 22.04 o 24.04.")

# Asigna automáticamente el nombre de la caja basado en la versión
cookiecutter_context = "{{ cookiecutter }}".replace(
    '"box_name": ""', 
    f'"box_name": "{UBUNTU_TO_BOX["{{ cookiecutter.ubuntu_version }}"]}"'
)
