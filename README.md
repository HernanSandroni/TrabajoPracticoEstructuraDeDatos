# Trabajo Practico EstructuraDeDatos
# Tecnicatura Universitaria en Programación 

# Grupo número 25

# Integrantes del grupo:
# -Mariano Hernan Berón- [porsiempreeshoy@gmail.com]
# -Hernan Sandroni- [hernansandroni@gmail.com]
# -Tomás Agustin Luna- [tomasluna399@gmail.com]

# Cliente de Correo Electrónico - Trabajo Práctico Final

##  Descripción General del Proyecto

Este repositorio contiene la implementación completa del Trabajo Práctico Final de la materia **Estructuras de Datos**, cuyo objetivo es desarrollar un **Cliente de Correo Electrónico** aplicando conceptos fundamentales de estructuras, algoritmos y modelado orientado a objetos.

El proyecto se divide en **cuatro entregas**, cada una incorporando nuevas funcionalidades y estructuras de datos más complejas.

---

## 🧩 Entrega 1 — Modelado y Clases Principales

En esta etapa se diseñaron las clases base del sistema:

* **Usuario**
* **Mensaje**
* **Carpeta**
* **ServidorCorreo**

Incluye:

* Encapsulamiento adecuado en cada clase
* Propiedades y métodos de acceso
* Diagramas UML del diseño
* Justificación de las decisiones de modelado
* Implementación de interfaces para enviar, recibir y listar mensajes

 *Ubicación:* `/usuario.py`, `/mensaje.py`, `/carpeta.py`, `/servidor_correo.py`.

---

##  Entrega 2 — Árbol General, Estructuras y Recursividad

En esta etapa se implementó:

* Un **árbol general** para administrar la estructura de carpetas del usuario
* Métodos recursivos para:

  * Buscar mensajes por **asunto** o **remitente**
  * Mover mensajes entre carpetas
* Análisis de eficiencia computacional
* Material adicional (infografía / video explicativo)

 Esta parte consolida el uso de recursión aplicada a estructuras jerárquicas.

---

##  Entrega 3 — Filtros, Diccionarios, Colas de Prioridad y Grafos

En esta entrega se desarrolló:

### ✔ Filtros Automáticos

Implementados con listas y diccionarios para organizar mensajes según reglas definidas por el usuario.

### ✔ Cola de Prioridades

* Para procesar mensajes **urgentes** primero.
* Implementada con `heapq` o estructura equivalente.

### ✔ Grafo de Servidores de Correo

* Modelado mediante nodos (servidores) y aristas (conexiones).
* Simulación del envío de mensajes entre servidores usando:

  * **BFS (Breadth-First Search)**
  * **DFS (Depth-First Search)**

### ✔ Material adicional

Incluye explicación o presentación de los algoritmos utilizados.

---

##  Entrega 4 — Programa Principal (main.py)

En esta etapa final se integran todas las funcionalidades anteriores en un programa ejecutable por consola.

El archivo `main.py` permite:

* Crear usuarios y sus carpetas
* Enviar y recibir correos
* Aplicar filtros automáticos
* Mostrar árbol de carpetas
* Procesar cola de prioridades
* Simular la ruta de servidores durante un envío

El objetivo es demostrar el correcto uso de:

* Listas
* Diccionarios
* Árboles
* Pilas y colas
* Grafos
* Algoritmos de búsqueda (BFS/DFS)

---

##  Cómo Ejecutar el Proyecto

1. Clonar el repositorio:

```bash
git clone https://github.com/HernanSandroni/TrabajoPracticoEstructuraDeDatos.git
```

2. Abrir la carpeta en Visual Studio Code
3. Ejecutar el archivo principal:

```bash
python main.py
```

---

##  Estructura del Repositorio

```
📦 TrabajoPracticoEstructuraDeDatos
├── usuario.py
├── mensaje.py
├── carpeta.py
├── servidor_correo.py
├── main.py
├── filtros.py (si aplica)
├── grafo_servidores.py (si aplica)
└── README.md
```

---

##  Tecnologías y Conceptos Utilizados

* Python 3
* Estructuras de datos:

  * Listas
  * Diccionarios
  * Árbol general
  * Cola de prioridad (heap)
  * Grafos
* Recursividad
* Algoritmos BFS y DFS
* Encapsulamiento y POO

---


Descripción General

Este proyecto implementa un cliente de correo electrónico completo, desarrollado como Trabajo Final integrador de la materia Estructuras de Datos de la UNaB.

A lo largo de cuatro entregas se construyó progresivamente un sistema que integra:

Modelado orientado a objetos.

Árbol general para carpetas y subcarpetas.

Filtros automáticos con listas y diccionarios.

Cola de prioridades para mensajes urgentes.

Grafo de servidores con envío simulado mediante BFS y DFS.

Interfaz de línea de comandos (CLI) para operar el sistema.

La Entrega Final reúne todas las funcionalidades y agrega documentación, materiales acumulados y la integración necesaria para la defensa grupal e individual.




