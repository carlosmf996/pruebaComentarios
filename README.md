Creo el entorno virtual en la carpeta de mi proyecto

```bash
mkvirtualenv taskDjango
```

Instalo y actualizo PIP

```bash
-m pip install --upgrade pip
```

Creo el archivo "requirements.txt" y lo instalo

    requirements.txt ---> Django~=4.2.7

```bash
pip install -r requirements.txt
```

Creo el proyecto en la carpeta que quiero

```bash
django-admin startproject comentarios .
```

Edito lo básico en "settings.py"

```python

TIME_ZONE = ‘Europe/Madrid’
LANGUAGE_CODE = ‘es-es’

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'static'

ALLOWED_HOSTS = ['127.0.0.1','localhost']

DATABASES = {
'default': {
'ENGINE': 'django.db.backends.sqlite3',
'NAME': BASE_DIR / 'db.sqlite3',
    }
}

```

Creo la base de datos y la inicio

```bash
python manage.py migrate
```

Compruebo que mi servidor funciona

```bash
python manage.py runserver
```

En web puedo acceder con cualquiera de las siguientes URLs

    ---> 127.0.0.1
    ---> localhost

Creo la aplicación (No puede tener el mismo nombre que el proyecto)

```bash
python manage.py startapp comentariosapp
```
En "settings.py" tenemos que registrar la apliación

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'comentariosapp',]
```

Creamos un modelo en "models.py". Debería de quedar así:

```python
from django.conf import settings
from django.db import models
from django.utils import timezone

class Comentario(models.Model):
    nombre = models.CharField(max_length=200)
    correo = models.TextField()
    comentario = models.TextField()
    published_date= models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.nombre
```

Aplicamos los cambios en los modelos para la Base de Datos

```bash
python manage.py makemigrations comentariosapp
```

```bash
python manage.py migrate comentariosapp
```

Modificamos el "admin.py" para crear un nuevo superusuario. Deberíamos tener algo así:

```python
from django.contrib import admin
from .models import Comentario

admin.site.register(Comentario)
```

Creamos el administrador. Necesitamos tener el servidor arrancado y ejecutar la siguiente orden en otra terminal

```bash
python manage.py createsuperuser
```
    Usuario ---> comentariosapp

Para acceder a la página del login:
    --->http://127.0.0.1:8000/admin/

Modificamos "views.py". Debería de quedar algo así:

```python
from django.utils import timezone
from django.shortcuts import render
from .models import Comentario

def comentario_list(request):

    comentario = Comentario.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'comentarios/comentario_list.html', {'comentario': comentario})

```

Modificamos el "urls.py", este archivo es el del SITIO, ya venía creado. Sin mostrar comentarios, debería quedar así:

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('comentariosapp.urls')),
]
```

En la aplicación, creamos un "urls.py" también, y debería quedar tal que así:

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.comentario_list, name='comentario_list'),
]
```

Creo la carpeta "Templates", y dentro de la misma creo la carpeta "comentarios". Finalmente creo dentro "comentario_list.html" y escribo el código

```html
<html>
<head>
    <title>ToDoList</title>    
</head>
<body>

    <h1>Completar formulario</h1>
    <form action="{% url 'comentario_list'%}" method="POST">
        {% csrf_token%}
        {{ form.as_p }}
        <button type="submit">Dale caña</button>
    </form>
</body>
</html>
```

Creo el archivo "forms.py" en el directorio "comentariosapp". Debería quedar así

```python
from .models import Comentario
from django import forms

class ComentarioForm(forms.ModelForm):

    class Meta:
        model = Comentario
        fields = ['nombre', 'correo', 'comentario']
```

En "views.py" modifico su contenido para que haga las acciones "GET" y "POST"

```python
class ComentarioList(View):

        
    def get(self, request):
        form=ComentarioForm()
        comentario = Comentario.objects.all()
        return render(request, 'comentarios/comentario_list.html', {'comentario': comentario, 'form': form})
    
    def post(self, request):
        form=ComentarioForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('comentario_list')
        comentario = Comentario.objects.all()
        return render(request, 'comentarios/comentario_list.html', {'comentario': comentario, 'form': form})
```

Con esto, ya podemos ver el formulario en su HTML nada mas cargar localhost.

Ahora, debemos crear las otras 2 URLs en "views.py", "urls.py" y sus propios HTMLs

Añadimos las clases extra en "views.py"

```python
class Confirmacion(View):

    def get(self, request):
        return render(request, 'comentarios/confirmacion.html')


class TodosComentarios(View):

    def get(self, request):
        comentarios = Comentario.objects.all()
        return render(request, 'comentarios/todos_comentarios.html', {'comentarios': comentarios})
```

Resultado final de "urls.py"

```python
from django.urls import path
from . import views
from .views import ComentarioList, Confirmacion, TodosComentarios

urlpatterns = [
    path('',ComentarioList.as_view(), name='comentario_list'),
    path('confirmacion', Confirmacion.as_view(), name='confirmacion'),
    path('todos_comentarios', TodosComentarios.as_view(), name='todos_comentarios'),
]
```

Solo nos falta crear los HTMLs de cada página con sus botones para una correcta navegación.

Código de "confirmacion.html"

```HTML
<body>
    <h1>
        ¡¡¡Comentario almacenado!!!
    </h1>
    <p>
        Gracias por enviarnos tu comentario, añade uno nuevo o revisa todos los anteriores
    </p>

    <form action = "{% url 'comentario_list' %}">
        <button type="submit">Añadir otro comentario</button>
    </form>

    <form action = "{% url 'todos_comentarios' %}">
        <button type="submit">Ver el resto de comentarios</button>
    </form>
    
</body>
```

Código de "todos_comentarios.html"

```HTML
<body>
    <h1>Lista de Comentarios</h1>
    <ul>
        {% for comentario in comentarios %}
        <li>{{ comentario.nombre }} - {{ comentario.correo }} ({{ comentario.comentario }})</li>
        {% empty %}
        <li>No hay comentarios que mostrar.</li>
        {% endfor %}
    </ul>

    <form action="{% url 'comentario_list' %}">
        <button type="submit">Añadir otro comentario</button>
    </form>
</body>
```