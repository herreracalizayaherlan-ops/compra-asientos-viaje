# Manual Técnico - Sistema de Compra de Asientos de Viaje

## 1. Descripción técnica
El programa es un script ejecutable por línea de comandos (CLI) desarrollado en Python para la gestión de ventas de pasajes de transporte terrestre. Implementa control de flujo estructurado, un diccionario de datos para la definición de rutas y tarifas, y manejo de excepciones durante la entrada de datos en la terminal.

## 2. Tecnología utilizada
- **Lenguaje de programación:** Python 3.8+
- **Paradigma:** programación estructurada.
- **Estructuras de datos:** diccionarios (`dict`) y tuplas (`tuple`).
- **Control de flujo:** bucles (`while`, `for`) y manejo de excepciones (`try-except`).

## 3. Requisitos técnicos
- **Sistema operativo:** Windows 10/11, GNU/Linux o macOS.
- **Intérprete:** Python 3.8 o superior, instalado y configurado en la variable de entorno del sistema (`PATH`).
- **Línea de comandos:** PowerShell, CMD o Bash.
- **Espacio en disco:** menos de 5 MB.

## 4. Estructura del proyecto
```text
compra-asientos/
├── README.md               # Presentación e información general del proyecto
├── viaje.py                # Código fuente principal de la aplicación
└── docs/                   # Documentación del proyecto
    ├── manual-usuario.md   # Guía paso a paso para el usuario final
    ├── manual-tecnico.md   # Especificaciones técnicas del sistema
    └── img/
        └── sistema.png     # Captura del sistema en ejecución
```

## 5. Preparación o instalación
1. Clonar o descargar el repositorio del proyecto en el equipo local.
2. Si se descargó como archivo comprimido (.zip), descomprimirlo en la ubicación deseada.
3. Abrir la terminal y navegar hasta el directorio raíz del proyecto: `cd ruta/hacia/compra-asientos`
4. No se requieren librerías ni dependencias externas (pip), ya que el sistema utiliza únicamente la biblioteca estándar de Python.

## 6. Forma de ejecución
- Desde la raíz del proyecto, en la consola de comandos, ejecutar la aplicación con el siguiente comando: `python viaje.py`

## 7. Explicación breve del funcionamiento
1. **Modelado de datos (destinos):** se utiliza un diccionario indexado numéricamente (1-8) donde cada elemento guarda una tupla con el nombre de la ruta y su costo unitario en bolivianos:

   ```python
   destinos = {
       1: ("Oruro - Colquiri", 20),
       2: ("La Paz - Colquiri", 60),
       ...
   }
   ```

2. **Validación de entradas:** los datos numéricos (asientos y selección de ruta) están protegidos mediante bucles `while True` combinados con bloques `try-except ValueError`, lo que evita que la aplicación falle si el usuario ingresa caracteres alfabéticos.

3. **Cálculo de la transacción:** el sistema multiplica la cantidad de asientos por la tarifa unitaria de la opción seleccionada:

   ```text
   Monto total = Cantidad de asientos * Precio unitario
   ```

4. **Despliegue:** se formatean y muestran en consola las variables procesadas, dando un reporte estructurado de la compra.
