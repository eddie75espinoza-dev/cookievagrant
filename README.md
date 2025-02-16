# Plantilla para VagrantFile

Este proyecto utiliza [Cookiecutter](https://cookiecutter.readthedocs.io/) para generar un archivo `Vagrantfile` que permite la creación de máquinas virtuales con Vagrant y VirtualBox.

## Requisitos

Antes de comenzar, asegúrate de tener instalados los siguientes requisitos:

- [Vagrant](https://developer.hashicorp.com/vagrant)
- [VirtualBox](https://www.virtualbox.org/wiki/Downloads)
- [Python](https://www.python.org/downloads/) (mínimo 3.10)
- [Cookiecutter](https://cookiecutter.readthedocs.io/en/stable/installation.html):
  
  ```sh
  pip install cookiecutter
  ```

## Instalación y Uso

Para generar un `Vagrantfile`, sigue los siguientes pasos:

1. Clona este repositorio o usa Cookiecutter directamente:
   
   ```sh
   cookiecutter https://github.com/eddie75espinoza-dev/cookievagrant.git
   ```

2. Se te solicitarán varias opciones de configuración, como la versión de Ubuntu, la cantidad de memoria RAM, procesadores y versiones de software adicionales.

3. Una vez completado el proceso, se generará un directorio con un `Vagrantfile` listo para ser utilizado.

   ```sh
    {{cookiecutter.project_name}}/
    ├── Vagrantfile          # Archivo con la configuración
    └── README.md            # Documentación sobre el uso y configuración
   ```

## Opciones de Configuración

Durante la ejecución de Cookiecutter, se podrán definir las siguientes opciones:

| Opción               | Descripción                                  | Valores Disponibles |
|----------------------|----------------------------------------------|---------------------|
| `provider`          | Proveedor de virtualización                  | `virtualbox`       |
| `ubuntu_version`    | Versión de Ubuntu a instalar                 | `20.04`, `22.04`, `24.04` |
| `vm_define`         | Identificador de la máquina virtual          | `ubuntu/{{ cookiecutter.ubuntu_version}}` |
| `hostname`          | Nombre de host de la máquina                 | `vagrant-host`     |
| `memory`           | Memoria RAM asignada a la VM                 | `1024`, `2048`, `4096`, `8192`, `12288` |
| `disk_size`        | Tamaño del disco                             | `40GB`            |
| `processors`       | Número de procesadores asignados             | `2`               |
| `python_versions`  | Versiones de Python a instalar               | `3.10`, `3.11`, `3.12`, `3.13` |
| `node_version`     | Versión de Node.js                           | `20`, `22`        |
| `docker_version`   | Versión de Docker                            | `latest`          |
| `postgres_version` | Versión de PostgreSQL                        | `14`              |

## Hooks

Este proyecto utiliza hooks pre y post generación:

- **Pre-hook:** Mapea la versión de Ubuntu seleccionada con la imagen correspondiente de [Vagrant](https://portal.cloud.hashicorp.com/vagrant/discover/ubuntu):
  
  ```json
  {
      "20.04": "focal64",
      "22.04": "jammy64",
      "24.04": "noble64"
  }
  ```
> Nota: Versión Ubuntu 24.04 LTS (Noble Numbat) disponible con proveedores distintos a 'virtualbox' para vagrant.

- **Post-hook:** Valida la configuración final antes de generar el archivo `Vagrantfile`.
