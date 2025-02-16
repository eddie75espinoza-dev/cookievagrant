# Plantilla para VagrantFile

> [Vagrant](https://www.vagrantup.com/) es una herramienta de código abierto que facilita la
creación, gestión y aprovisionamiento de máquinas virtuales para entornos de desarrollo y pruebas virtualizados.
Su objetivo principal es proporcionar un entorno de desarrollo consistente y reproducible, lo que lo hace
especialmente útil para equipos de desarrollo que trabajan en proyectos complejos con múltiples dependencias.

### Descripción

Este proyecto utiliza [Cookiecutter](https://cookiecutter.readthedocs.io/) para generar un archivo `Vagrantfile` que permite la creación de máquinas virtuales con Vagrant y VirtualBox.

## Requisitos

Antes de comenzar, asegúrate de tener instalados los siguientes requisitos:

- [Vagrant](https://developer.hashicorp.com/vagrant)
- [VirtualBox](https://www.virtualbox.org/wiki/Downloads)
- [Python](https://www.python.org/downloads/) (mínimo 3.10)
- [Cookiecutter](https://cookiecutter.readthedocs.io/en/stable/installation.html):

### ¿Cómo se instala Vagrant?

Para instalar Vagrant en Windows, se debe descargar el instalador desde el sitio web oficial de Vagrant. También
se necesitará un hipervisor como VirtualBox, Hyper-V o VMware para crear y ejecutar máquinas virtuales.

```http
https://developer.hashicorp.com/vagrant/downloads
```
#### - ¿Cómo se provisionan las máquinas?

Vagrant permite la provisión de máquinas virtuales mediante scripts de aprovisionamiento. Se puede usar
herramientas como Shell, Ansible, Puppet o Chef para configurar y personalizar la máquina virtual según las
necesidades.

- Ventajas de usar Vagrant:
  * Reproducibilidad: Vagrant garantiza que todos los miembros del equipo trabajen en el mismo entorno, lo que
  * reduce conflictos debido a diferencias en configuraciones.
  * Facilidad de uso: Vagrant simplifica la creación y gestión de máquinas virtuales, lo que ahorra tiempo y reduce la
  curva de aprendizaje.
  * Portabilidad: Los archivos de configuración de Vagrant (Vagrantfile) se pueden compartir fácilmente, lo que
  facilita la colaboración y la transferencia de entornos de desarrollo entre sistemas operativos.

- Desventajas de usar Vagrant en plataformas Windows:
  * Rendimiento: En comparación con sistemas basados en Linux, las máquinas virtuales de Vagrant en Windows
  pueden experimentar un rendimiento ligeramente inferior debido a la capa de virtualización adicional.
  * Requisitos de hardware: Algunas configuraciones pueden requerir recursos de hardware significativos, lo que
  podría afectar el rendimiento general de la máquina anfitriona en sistemas Windows.
  * Compatibilidad: Aunque Vagrant es compatible con Windows, algunas características pueden no ser tan fluidas o
  completas como en entornos basados en Unix.

#### - ¿Cómo se usa?

Para usar Vagrant, primero se debe definir un archivo de configuración (escrito en ruby) llamado &quot;Vagrantfile&quot;. En
este archivo, se puede especificar el sistema operativo base, las configuraciones de red, recursos de la máquina y
la provisión de software.
Una vez se tenga el Vagrantfile, se ejecuta el comando como ‘vagrant up’ para crear y encender la máquina
virtual, ‘vagrant ssh’ para acceder a la máquina virtual, ‘vagrant halt’ para detener la máquina y ‘vagrant destroy’
para eliminarla.

```http
https://developer.hashicorp.com/vagrant/tutorials/getting-started/getting-started-index
```

### ¿Cómo se instala cookiecutter?

  ```sh
  pip install cookiecutter
  ```

## Instalación y creación del archivo Vagrantfile

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
