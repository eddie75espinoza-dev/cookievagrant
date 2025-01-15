import sys

# Mapeo de versiones de Ubuntu a nombres de caja
UBUNTU_TO_BOX = {
    "20.04": "focal64",
    "22.04": "jammy64",
    "24.04": "noble64"
}

# Obtener la versión seleccionada
ubuntu_version = "{{ cookiecutter.ubuntu_version }}"

# Validar que la versión de Ubuntu sea soportada
if ubuntu_version not in UBUNTU_TO_BOX:
    print("Error: Versión de Ubuntu no soportada. Use 20.04, 22.04 o 24.04.")
    sys.exit(1)

# Exponer el valor calculado para box_name
print(f"Seleccionando box: {UBUNTU_TO_BOX[ubuntu_version]} para Ubuntu {ubuntu_version}")
