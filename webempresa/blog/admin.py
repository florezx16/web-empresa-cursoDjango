from django.contrib import admin
from .models import Category,Post

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')

class PostAdmin(admin.ModelAdmin):
    #Debemos de recordar que la gran mayoria dep ropiedades aqui devueltas son tuplas, asi que al tener un solo elemento se debe terminar en coma(,)
    readonly_fields = ('created','updated')
    list_display = ('title','author','post_categories','published')#Columnas a mostrar 
    ordering = ('author','-published')#Orden de displiegue
    search_fields = ('title',)#Habilita la busqueda por X campos del modelo
    date_hierarchy = 'published' #Desplegamos un navegador de fechas
    list_filter = ('categories__name','author__username')#Desplega un widget de busqueda rapida por X campos

    #Podemos hacer nuestras columnas personalizadas
    @admin.display(description='categories')#Llamamos el decorador admin.display el cual nos permitira asignarle el nombre a la columna personalizada
    def post_categories(self,obj):#Siempre pasamos el self ya que es una clase y el obj(El cual es el contenido como tal de cada fila)
        categoriesContent = [category.name for category in obj.categories.all()]#Obtenemos las categorias a partir del modelo y las organizamos
        return categoriesContent
    

admin.site.register(Category,CategoryAdmin)
admin.site.register(Post,PostAdmin)
