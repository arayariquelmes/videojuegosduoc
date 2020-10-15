from django.shortcuts import render,HttpResponse
import random
class Producto:
    titulo = ''
    descripcion = ''
    imagen = ''
    precio = 0

# Create your views here.
def home(request):
    facebook_url = "http://www.facebook.com"
    twitter_url = "http://www.twitter.com"
    productos = []
    imagenes = ("https://store.nintendo.co/media/catalog/product/"
                "cache/1aff59ff6f21b2058ac5563c018426d7/z/e/zeldabow_hero_2.jpg", "https://cdn.vox-cdn.com/thumbor/"
                "Y_PzDNQ_5tVJOfGqjS5HhEUpKMM=/1400x1400/filters:format(jpeg)/cdn.vox-cdn.com/uploads/chorus_asset/file/20031517/PS5DigitalEdition_02.jpg" )
    for i in range(1,10):
        prod = Producto()
        prod.titulo = "Producto {}".format(i)
        prod.descripcion = "Descripcion entera pulenta de prod {}".format(i)
        prod.precio = random.randint(1000,100000)
        prod.imagen = imagenes[random.randint(0, len(imagenes) - 1)]
        productos.append(prod)
    return render(request, "home.html", {'productos':productos, 'facebook_url':facebook_url, 'twitter_url':twitter_url})

def contacto(request):

    return HttpResponse("<h1>Esto es contacto</h1>")

def admin(request):
    return HttpResponse("<h1>Esto es admin</h1>")