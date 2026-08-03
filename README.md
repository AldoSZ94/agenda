# Agenda 📋

Aplicación web desarrollada con **Django** para la gestión de actividades personales. Permite crear, consultar, actualizar y eliminar tareas mediante operaciones CRUD, incorporando niveles de prioridad, estado de completado y una interfaz responsive desarrollada con Tailwind CSS.

El proyecto aplica conceptos fundamentales del desarrollo web con Django como arquitectura MVT, modelos, formularios personalizados, manejo de templates, validación de datos y paginación.

---

## ✨ Demo

👉 https://agenda-django-w4hw.onrender.com

---

## 🚀 Características

* Crear nuevas actividades.
* Visualizar lista de actividades registradas.
* Editar actividades existentes.
* Eliminar actividades mediante confirmación.
* Clasificar actividades por nivel de prioridad:

  * Baja
  * Media
  * Alta
* Marcar actividades como completadas.
* Paginación del listado de actividades.
* Formularios personalizados con estilos propios.
* Diseño responsive adaptable a diferentes tamaños de pantalla.
* Manejo de estados vacíos cuando no existen actividades.

---

## 🛠️ Tecnologías utilizadas

### Backend

* Python
* Django

### Frontend

* HTML5
* CSS3
* Tailwind CSS

---

## 📝 Modelo principal

El modelo principal de la aplicación es `Tarea`.

Cada tarea contiene:

| Campo             | Descripción                           |
| ----------------- | ------------------------------------- |
| titulo            | Nombre de la actividad                |
| descripcion       | Información detallada de la tarea     |
| prioridad         | Nivel de prioridad asignado           |
| fecha_creada      | Fecha en la que fue creada            |
| fecha_actualizada | Fecha de la última modificación       |
| completada        | Indica si la actividad fue finalizada |

---

## 🖥️ Interfaz

La aplicación cuenta con:

* Diseño responsive.
* Layout base reutilizable mediante templates de Django.
* Formularios personalizados con estilos Tailwind CSS.
* Indicadores visuales para niveles de prioridad.
* Confirmación antes de eliminar actividades.
* Estado vacío cuando no existen registros.
* Navegación mediante paginación.

---

## 📚 Conceptos aplicados

Durante el desarrollo se implementaron los siguientes conceptos:

* Arquitectura MVT de Django.
* Creación y modificación de modelos.
* Migraciones.
* Vistas basadas en funciones.
* Formularios ModelForm.
* Validación de formularios.
* Renderizado dinámico con Django Templates.
* Manejo de archivos estáticos.
* Paginación con `Paginator`.
* Integración de Tailwind CSS.

---

## 👨‍💻 Autor

**Aldo Sandoval Zepeda**

Proyecto desarrollado como práctica de desarrollo web utilizando Django.

