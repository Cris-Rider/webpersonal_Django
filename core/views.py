from django.shortcuts import render, HttpResponse

# Menu de paginas
html_base = """
<h1>WEB PERSONAL</h1>
<ul>
    <li><a href="/">Portada</a></li>
    <li><a href="/about-me">Acerca de</a></li>
    <li><a href="/portfolio">Portafolio</a></li>
    <li><a href="/contact">Contacto</a></li>
</ul>

"""

# Create your views here.


def home(request):
    return render(request, "core/home.html")


def about(request):
    return HttpResponse(html_base + """
        <h2> Acerca de: </h2>
        <p>Me llamo Criss </p>
    """)


def portfolio(request):
    return HttpResponse(html_base + """
        <h2> Portafolio </h2>
        <h3>Proyectos: </h3>
        <p>Proyecto 1 </p>
        <p>Proyecto 2 </p>
        <p>Proyecto 3 </p>
    """)


def contact(request):
    return HttpResponse(html_base + """
        <h2> Contacto </h2>
        <h3>Datos: </h3>
        <p>contacto 1 </p>
    """)
