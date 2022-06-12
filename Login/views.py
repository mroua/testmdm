from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

vente = []
dernierevente = ''
choix_porte = ''
choix_couleur = ''
choix_dimension = ''
choix_serigraphie = ''
choix_serrure = ''
choix_oeil = ''
choix_client = ''
choix_informationclient = ''
choix_ventail = ''
choix_vitrage = ''

def Choix(request, pk, pk2):

    global vente,dernierevente,choix_porte,choix_couleur,choix_dimension,choix_serigraphie,choix_serrure,choix_oeil,choix_client,choix_informationclient, choix_ventail, choix_vitrage

    print(choix_porte)
    val = int(pk)
    if(val==1):
        if(pk2 == '1'):
            choix_porte = "Portes d'entrée massive"
        elif(pk2 == '2'):
            choix_porte = "Portes de passage âme pleine"
        else:
            choix_porte = "Portes de passage tubulaire"
    elif(val==2):
        if(pk2 == '1'):
            choix_couleur = "Azabache"
        elif(pk2 == '2'):
            choix_couleur = "Chene"
        if(pk2 == '3'):
            choix_couleur = "Joplin"
        elif(pk2 == '4'):
            choix_couleur = "Stella"
        if(pk2 == '5'):
            choix_couleur = "Tostado"
        else:
            choix_couleur = "Wenge"
    elif (val == 3):
        if(pk2 == '1'):
            choix_serigraphie = "Sans"
        elif(pk2 == '2'):
            choix_serigraphie = "2F"
        if(pk2 == '3'):
            choix_serigraphie = "4FL"
        elif(pk2 == '4'):
            choix_serigraphie = "4F"
        if(pk2 == '5'):
            choix_serigraphie = "6F"
        else:
            choix_serigraphie = "Spécial"
    elif (val == 4):
        if(pk2 == '1'):
            choix_dimension = "2090 x 923"
        elif(pk2 == '3'):
            choix_dimension = "2090x(400+723)"
        elif(pk2 == '4'):
            choix_dimension = "2090x(723+723)"
        elif(pk2 == '5'):
            choix_dimension = "2090x(400+823)"
        elif(pk2 == '6'):
            choix_dimension = "2090x(823+823)"
        elif(pk2 == '7'):
            choix_dimension = "2090x(400+923)"
        elif(pk2 == '8'):
            choix_dimension = "2090x(923+923)"
        elif(pk2 == '9'):
            choix_dimension = "2090x(823+823)"
        elif(pk2 == '10'):
            choix_dimension = "2090x(923+723)"
        elif(pk2 == '11'):
            choix_dimension = "2090x(723+823)"
        elif(pk2 == '12'):
            choix_dimension = "2090x723"
        elif(pk2 == '13'):
            choix_dimension = "2090x823"
        else:
            choix_dimension = "2090 x 1023"
    elif (val == 5):
        if(pk2 == '1'):
            choix_serrure = "1 Point de sécurité"
        elif(pk2 == '3'):
            choix_serrure = "Petite Clé"
        elif(pk2 == '4'):
            choix_serrure = "Comdanation"
        else:
            choix_serrure = "3 Point de sécurité"
    elif (val == 6):
        if(pk2 == '1'):
            choix_oeil = "Avec oeils de bœuf"
        else:
            choix_oeil = "Sans oeils de bœuf"
    elif (val == 7):
        if(pk2 == '1'):
            choix_client = "Particulier"
        else:
            choix_client = "Société"
    elif (val == 8):
        data= pk2.split('&')
        choix_informationclient = {
            'nom': data[0],
            'prenom': data[1],
            'adr': data[2],
            'num': data[3],
            'email': data[4],
            'matri': data[5],
            'age': data[6],
            'sexe': data[7]

        }

        dernierevente={
            'type':choix_porte,
            'couleur':choix_couleur,
            'dimension':choix_dimension,
            'serigraphie':choix_serigraphie,
            'serrure':choix_serrure,
            'oeil':choix_oeil,
            'ventail': choix_ventail,
            'vitrage': choix_vitrage,
            'client':choix_client,
            'info':choix_informationclient
        }
        vente.append(dernierevente)
    elif (val == 9):
        if(pk2 == '1'):
            choix_ventail = "Simple ventail"
        else:
            choix_ventail = "Double ventaux"
    elif (val == 10):
        if (pk2 == '1'):
            choix_vitrage = "Sans"
        elif (pk2 == '2'):
            choix_vitrage = "Coté"
        if (pk2 == '3'):
            choix_vitrage = "Haut"
        elif (pk2 == '4'):
            choix_vitrage = "Occulus"
        if (pk2 == '5'):
            choix_vitrage = "Dimension varié"
        else:
            choix_vitrage = "Spécial"





    return HttpResponse('done')

def Index(request):
    return render(request, 'Login/login.html')


def distributeur(request):
    return render(request, 'home/distributeur.html')

def disvente_1(request):
    return render(request, 'home/disvente_1.html')

def disvente_2(request):
    return render(request, 'home/disvente_2.html')

def disvente_3(request):
    return render(request, 'home/disvente_3.html')

def disvente_4(request):
    return render(request, 'home/disvente_4.html')

def disvente_5(request):
    return render(request, 'home/disvente_5.html')

def disvente_6(request):
    return render(request, 'home/disvente_6.html')

def disvente_7(request):
    return render(request, 'home/disvente_7.html')

def disvente_8(request):
    return render(request, 'home/disvente_8.html')

def disvente_9(request):
    return render(request, 'home/disvente_9.html')

def disvente_10(request):
    return render(request, 'home/disvente_10.html')

def disvente_11(request):
    return render(request, 'home/disvente_11.html')

def disvente_12(request):
    return render(request, 'home/disvente_12.html')

def disvente_13(request):
    return render(request, 'home/disvente_13.html')

def disvente_14(request):
    return render(request, 'home/disvente_14.html')

def disvente_15(request):
    return render(request, 'home/disvente_15.html')

def final_vente(request):
    global dernierevente, choix_porte
    print("ici")
    print(choix_porte)
    print(dernierevente)
    return render(request, 'home/disvente_final.html', {'dernierevente': dernierevente})
