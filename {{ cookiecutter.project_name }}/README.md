# Entorno de desarrollo con Vagrant

![Static Badge](https://img.shields.io/badge/Estatus-En%20Producción-green)
![Static Badge](https://img.shields.io/badge/Lenguaje-Ruby-red)
![Static Badge](https://img.shields.io/badge/Versi%C3%B3n-1.0.0-blue)

#### Índice

* [Vagrant](#vagrant)
* [Instalación](#instalación)
* [Cómo se provisionan las máquinas?](#cómo-se-provisionan-las-máquinas)
* [Cómo se usa?](#cómo-se-usa)
* [Configuración en VsCode](#configuración-en-vscode)
* [Configuración en Git](#configuración-en-git)
* [Configuración en Postgres](#configuración-en-postgres)


## Vagrant

[Vagrant](https://www.vagrantup.com/) es una herramienta de código abierto que facilita la creación, gestión y aprovisionamiento de máquinas virtuales para entornos de desarrollo y pruebas virtualizados. Su objetivo principal es proporcionar un entorno de desarrollo consistente y reproducible, lo que lo hace especialmente útil para equipos de desarrollo que trabajan en proyectos complejos con múltiples dependencias.
To make it easy for you to get started with GitLab, here's a list of recommended next steps.


## Instalación

Para instalar Vagrant en Windows, se debe descargar el instalador desde el sitio web oficial de Vagrant. También se necesitará un hipervisor como VirtualBox, Hyper-V o VMware para crear y ejecutar máquinas virtuales.

- [vagrant](https://developer.hashicorp.com/vagrant/downloads)
- [virtualbox](https://www.virtualbox.org/wiki/Downloads)

## Cómo se provisionan las máquinas?

Vagrant permite la provisión de máquinas virtuales mediante scripts de aprovisionamiento. Se puede usar herramientas como Shell, Ansible, Puppet o Chef para configurar y personalizar la máquina virtual según las necesidades.

## Cómo se usa?
Antes de iniciar el proceso, debe considerar que sistema operativo usar, cada archivo **vagrantfile** hace referencia a un SO ubuntu.

## Vagrantfiles Disponibles

| Archivo            | Versión de Ubuntu LTS      | Nombre Clave        | Python version |
|--------------------|----------------------------|---------------------|----------------|
| `vagrantfile_22`   | 22.04 LTS                  | Jammy Jellyfish     | 3.10           |
| `vagrantfile_20`   | 20.04 LTS                  | Focal Fossa         | 3.8            |
| `vagrantfile`      | 18.04 LTS                  | Bionic Beaver       | 3.8            |

> ⚠️ **Nota importante:** Una vez seleccionado el archivo deberá cambiar su nombre a **vagrantfile**


Para usar Vagrant, primero defina la ruta desde donde se ejecutará el archivo de configuración **"vagrantfile"**.

Una vez que tenga el archivo *Vagrantfile* en la ruta especificada, abra una terminal con permisos de administrador (puede utilizar Git Bash o PowerShell) y podrá ejecutar los comandos de *Vagrant* para crear, conectar, apagar o destruir la máquina virtual, como sigue:

Para validar la sintaxis del archivo de configuración, use:

```bash
vagrant validate
```
Verifica que el _Vagrantfile_ no contenga errores de sintaxis antes de ejecutar la máquina virtual.

Para provisionar y levantar la máquina virtual, use:

```bash
vagrant up
```
Crea y configura la máquina virtual según las especificaciones del _Vagrantfile_.

Si desea ingresar a la máquina virtual por consola, use:

```bash
vagrant ssh
```
Accede a la máquina virtual mediante una conexión SSH.

Puede suspender de la máquina virtual, esto la detendrá y guardará el estado de ejecución actual.

```bash
vagrant suspend
```
Este comando detiene la ejecución de la máquina sin apagarla por completo, permitiendo reanudarla más rápido.

Para reanudar la máquina virtual desde el estado suspendido, use:

```bash
vagrant resume
```
Restablece la ejecución de la máquina desde el estado en que fue suspendida, sin necesidad de un arranque completo.

Para detener y cerrar la máquina virtual de manera segura, use:

```bash
vagrant halt
```
Apaga la máquina virtual correctamente sin eliminarla.

Si desea eliminar la máquina virtual (esto borrará todos sus datos y configuraciones no persistentes), use:

```bash
vagrant destroy
```
Elimina completamente la máquina virtual y su almacenamiento asociado.

Para saber más, visite los [tutoriales de Vagrant](https://developer.hashicorp.com/vagrant/tutorials/getting-started/getting-started-index)


## Configuración en VsCode

Abra VsCode y habilite la extensión **Remote - SSH**

Siga los siguientes pasos:

 - En la terminal donde ejecutó los comandos de *vagrant*, ejecute y copie en el portapapeles el resultado del comando:
 ```bash
 vagrant ssh-config
 ```
 ejemplo:
 ```
 Host default
    HostName 127.0.0.1
    User vagrant
    Port 2222
    UserKnownHostsFile /dev/null
    StrictHostKeyChecking no
    PasswordAuthentication no
    IdentityFile C:/<ruta_a_vagrantfile/.vagrant/machines/default/virtualbox/private_key
    IdentitiesOnly yes
    LogLevel FATAL
    PubkeyAcceptedKeyTypes +ssh-rsa
    HostKeyAlgorithms +ssh-rsa
 ```
 - En VsCode, presione F1, 
 - Seleccione  ```Remote-SSH: Connect to Host...```
 - Seleccione  ```Configure SSH Host...```
 - Seleccione la ruta donde se encuentre '.../ssh/config', por ejemplo: *'C:\Users\usuario\.ssh\config'*
 - Copie el script en el archivo.

Esto habilitará el host para la conexión vía SSH. Puede actualizar _'Remote Explorer'_ en la barra de actividades para conectarse.

## Configuración en Git
Una vez conectado host, en la terminal de VsCode podrá realizar las configuraciones habituales de SSH en [gitlab](https://docs.gitlab.com/ee/user/ssh.html) y suministrar la configuración para cada repositorio o de forma global con comandos como:

#### Generación de SSH key

Generación de clave *ssh* y lectura del archivo.
_Nota: Cambiar el comentario al generar la clave ssh_
```bash
ssh-keygen -t ed25519 -C "<comentario>"
cat /home/vagrant/.ssh/id_ed25519.pub
```
#### Configuración de usuario en GIT
```
git config --global user.email "you@example.com"
git config --global user.name "Your Name"
```

Verifique la conexion a **GitLab** con:

```bash
ssh -T git@gitlab.com
```
Presione 'yes' en el CLI para autorizar el nuevo host.

## Configuración en Postgres

Dado que la instación de Postgres fue realizada de forma automática no se registró una clave para el usuario. Para ello, ejecute:

```bash
sudo -u postgres psql
```
luego, en la línea de comandos de postgres

```psql
ALTER USER postgres PASSWORD 'postgres';
```
