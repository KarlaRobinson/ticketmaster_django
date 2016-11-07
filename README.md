# ticketmaster_django

El proyecto es un sistema de asignación de tickets, donde hay 2 usuarios, un supervisor y un agente.
El supervisor tiene una pantalla para asignar tickets y ver una lista de tickets abiertos.
El agente tiene una vista tickets que tiene asignados donde puede cambiarles el status a pendiente o a cerrar.
Los tickets que se cierran desaparecen del dashboard del agente y del supervisor.



Features que faltan:
1. Agregar sistema de autenticación de Django.

2. Implementar CSRF tokens.

3. Agregar RegExs a los validaciones del modelo para obligar los usuarios a crear una contraseña segura y fijar que el email es un formato valido.

4. Usar AJAX para explicar a el usuario porque la información ingresada fue rechazada sin recargar la pagina, o avisar que la acción resulto exitoso.

6. Acceder y desplegar la informacion de ticket_set en el template agentes.html

7. Usar helpers y before_action equivalentes de Django.

8. Crear un solo modelo Usuario con distintos permisos en vez de Supervisores y Agentes.
