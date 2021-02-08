from django.shortcuts import redirect, render, HttpResponse

# Create your views here.

# MVC - Modelo Vista Controlador -> Acciones (metodos)

# MVT - Modelo Template Vista -> Acciones (metodos)

layout = """
    
"""

def index(request):

    """
    html = ""
        <h1>Inicio</h1>
        <p>Años hasta el 2050:</p>
        <ul>
    ""

    while year <= 2050:

        if year % 2 == 0:
            html += f"<li>{str(year)}</li>"

        year += 1

    html += "</ul>"

    """

    year = 2021
    hasta = range(year, 2051)

    nombre = 'Carlos Subero'
    
    lenguajes = ['javascript', 'Python', 'C#', 'Java', 'C++']


    return render(request, 'index.html', {
        'title': 'Inicio',
        'mi_variable': 'Soy un dato que esta en la vista',
        'nombre': nombre,
        'lenguajes': lenguajes,
        'years': hasta,
    })

def hola_mundo(request):
    return render(request, 'hola_mundo.html')

def pagina(request, redirigir=0):

    if redirigir == 1:
        return redirect('contacto', nombre="carlos", apellido="subero")


    return render(request, 'pagina.html', {
        'texto': 'Este es mi texto',
        'lista': ['uno', 'dos', 'tres'],
    })

def contacto(request, nombre="", apellido=""):

    html = ""

    if nombre and apellido:
        html += "<p>El nombre completo es: </p>"
        html += f"<h3>{nombre} {apellido}</h3>"

    return HttpResponse(layout+f"<h2>Contacto</h2>"+html)