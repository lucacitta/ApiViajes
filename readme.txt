Video Explicativo de funcionamiento:
    https://drive.google.com/drive/folders/1fyjZxAFPQpxN7RMlvXt-dpAXRq6bXl98?usp=sharing


# Usuarios: En caso de no querer crear un superusuario, esta subida la base de datos, donde hay superusuarios creados.
    username = luca
    password = 123456
    
    username = cami
    password = 123456

# Autenticacion: Actualmente, es necesario tener tokens para poder ingresar:
    Entrar a la ruta users/login/, en metodo POST pasando el usuario y la contraseña, esto obtener el token.
    Para ingresar a otras vistas pasar el token en el headers como Authorization.
    Si el token esta vencido en users/refresh-token se puede conseguir uno nuevo.

# Los endpoints estan realizados con distintas herramientas, como viewsets, @apiviews y generics.
    Principalmente esta echo de esta manera para mostrar distintas formas en las que se puede trabajar
    
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


