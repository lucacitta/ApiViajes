# Usuarios: En caso de no querer crear un superusuario, esta subida la base de datos, donde hay superusuarios creados.
    username = luca
    password = 123456

    username = cami
    password = 123456

# Autenticacion: Actualmente, es necesario tener tokens para poder ingresar:
    Entrar a la ruta users/login/, en metodo POST pasando el usuario y la contraseña, esto obtener el token.
    Para ingresar a otras vistas pasar el token en el headers como Authorization.
    Si el token esta vencido en users/refresh-token se puede conseguir uno nuevo.

# Vistas:
    Las vista users esta echa con decorador @api_view

    Las vistas trips estan echas con generics

    Las vistas de destinations estan echas con ModelViewSet
