# FASTAPI
Requisitos:
- Python 3.10+
- fastapi
- sqlmodel
- uvicorn


Usuarios de prueba 1:
usuario: admin contraseña: admin

{
  "success": true,
  "message": "Bienvenido, admin"
}

Usuarios de prueba 2:
usuario: admin contraseña: admin123

Salida:
{
  "success": false,
  "message": "Usuario o contraseña incorrectos"
}
