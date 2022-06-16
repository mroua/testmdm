from django.urls import path

from Login import views

urlpatterns = [
    path('', views.Index),
    path('login', views.Login),
    path('distributeur', views.distributeur),
    path('disvente_1', views.disvente_1),
    path('disvente_2', views.disvente_2),
    path('disvente_3', views.disvente_3),
    path('disvente_4', views.disvente_4),
    path('disvente_5', views.disvente_5),
    path('disvente_6', views.disvente_6),
    path('disvente_7', views.disvente_7),
    path('disvente_8', views.disvente_8),
    path('disvente_8', views.disvente_8),
    path('disvente_9', views.disvente_9),
    path('disvente_10', views.disvente_10),
    path('disvente_11', views.disvente_11),
    path('disvente_12', views.disvente_12),
    path('disvente_13', views.disvente_13),
    path('disvente_14', views.disvente_14),
    path('disvente_15', views.disvente_15),
    path('final_vente', views.final_vente),

    path('choix/<int:pk>/<str:pk2>', views.Choix)

]
