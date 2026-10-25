# Sistema de Compra de Asientos de Viaje

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Estado](https://img.shields.io/badge/Estado-En%20desarrollo-yellow)
![Documentación](https://img.shields.io/badge/Documentación-Completa-green)

## Contenido
- [Sistema de Compra de Asientos de Viaje](#sistema-de-compra-de-asientos-de-viaje)
  - [Contenido](#contenido)
  - [Descripción](#descripción)
  - [Objetivo](#objetivo)
  - [Funciones principales](#funciones-principales)
  - [Requisitos del sistema](#requisitos-del-sistema)
  - [Instrucciones de ejecución](#instrucciones-de-ejecución)
    - [Windows](#windows)
    - [Linux](#linux)
  - [Documentación](#documentación)
  - [Estado del proyecto](#estado-del-proyecto)
  - [Autor](#autor)

## Descripción
Proyecto en consola desarrollado en Python para gestionar la compra de asientos de viaje hacia y desde Colquiri, calculando automáticamente el monto total según la ruta y la cantidad de asientos seleccionados.

## Objetivo
Proporcionar una herramienta accesible e interactiva para registrar compradores y calcular el costo de los pasajes de transporte terrestre de manera automatizada.

## Funciones principales
- Registro del nombre del comprador.
- Selección y validación del número de asientos a comprar.
- Menú interactivo con 8 rutas de viaje disponibles.
- Cálculo automático de la tarifa unitaria y el monto total a pagar en bolivianos (Bs.).
- Despliegue de un resumen estructurado con el recibo de compra.

## Requisitos del sistema
- **Lenguaje:** Python 3.8 o superior.
- **Entorno:** consola de comandos o terminal (CMD, PowerShell o Bash).

## Instrucciones de ejecución
1. Clonar o descargar la carpeta del proyecto.
2. Abrir la terminal en la raíz del directorio `compra-asientos`.
3. Ejecutar el programa según el sistema operativo:

### Windows
```powershell
python viaje.py
```

### Linux
```bash
python3 viaje.py
```

## Documentación
- [Manual de Usuario](docs/manual-usuario.md)
- [Manual Técnico](docs/manual-tecnico.md)

## Estado del proyecto
- [x] Programa principal
- [x] README
- [x] Manual de usuario
- [x] Manual técnico
- [x] Evidencia del funcionamiento
- [ ] Validar que el nombre del comprador no esté vacío
- [ ] Guardar las compras realizadas

## Autor
- **Nombre:** Herlan Erwin Herrera Calizaya
- **Carrera:** Ingeniería Informática
- **Materia:** Actualización Tecnológica
- **Fecha:** 03/10/2026
