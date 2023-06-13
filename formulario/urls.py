from . import views
from django.urls import path

app_name = 'formulario'

urlpatterns = [
	  path('', views.enviar_mensagem, name = 'enviar_mensagem'),
	  path('projetos-python/', views.projetos_python, name = 'projetos_python'),
	  path('projetos-designer-grafico/', views.projetos_designer, name = 'projetos_designer'),
	  path('projetos-html-css-javascript/', views.projetos_web, name = 'projetos_web'),
      path('projetos-django.html/', views.projetos_django, name = 'projetos_django'),

	]