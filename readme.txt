Video Explicativo de funcionamiento:
    https://drive.google.com/drive/folders/1fyjZxAFPQpxN7RMlvXt-dpAXRq6bXl98?usp=sharing


# Usuarios: En caso de no querer crear un superusuario, esta subida la base de datos, donde hay superusuarios creados.
    username = luca
    password = 123456
    
    username = cami
    password = 123456

# Autenticacion: Es necesario tener tokens para poder ingresar a los endpoints(expceto destinations):
    1) Entrar a la ruta users/login/, en metodo POST pasando el usuario y la contraseña, esto obtener el token.
    2) Para ingresar a otros endpoints pasar el token en el headers como Authorization.
    3) Si el token esta vencido en users/refresh-token se puede conseguir uno nuevo.

# Los endpoints estan realizados con distintas herramientas, como viewsets, @apiviews y generics.
    Principalmente esta hecho de esta manera para mostrar distintas formas en las que se puede trabajar
    
---------------------------------------------------------------------------------------------
Explanatory video:
    https://drive.google.com/drive/folders/1fyjZxAFPQpxN7RMlvXt-dpAXRq6bXl98?usp=sharing
    
 # Users: If you dont want to create the superusers, the database is in the git hub, and there is some superusers created.
    username = luca
    password = 123456
    
    username = cami
    password = 123456

#authentication: You need to authenticate to use the endpoints (except destinations):
    1) Go to users/login/ and sent in POST method the username and the password, the sistem should give you the token and information about the user
    2) You need to pass the token in the header of the request to see the endpoints. THIS NEED TO BE IN KEY, VALUE. 
        key = Autorization
        value = yourToken 
    3) If your token is expired, you need to get a new one from users/refresh-token.
    
# I create the endpoints with diferents tools, like viewsets, @apiviews decorators and generics.
    I do this to show some ways to do it, obviusly, in a professional project i whill select the better tool.
