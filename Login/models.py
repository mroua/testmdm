from django.contrib.auth.models import User
from django.db import models

# Create your models here.


typeUser= [
    ('Distributeur', 'Distributeur'),
    ('MDM', 'MDM')
]

Niveau=[
    ('ad', 'Admin'),
    ('res_region', 'Responsable_region'),
    ('res_dis', 'Responsable_distributeur'),
    ('dis', 'Distributeur')
]

typeShowroomDepot =[
    ('show', 'Showroom'),
    ('dep', 'Depot')
]

typeProduit = [
    ('O', 'Ouvrant'),
    ('C', 'Cadre'),
    ('E', 'Embrochure'),
    ('S', 'Serrure'),
    ('G', 'Grille')
]

typeAction = [
    ('E', 'Entree'),
    ('S', 'Sortie')
]

typePorte = [
    ('PP', 'Porte de passage'),
    ('PDV', 'Porte double vantaux'),
    ('PEM', "Porte d'entrée massive"),
    ('PTEC', 'Technique'),
    ('PCF30', 'Porte coupe-Feu 30mm'),
    ('PCF45', 'Porte coupe-Feu 45mm'),
    ('PCF60', 'Porte coupe-Feu 60mm')
]


modeleporte = (
      ('STAR', 'Star Massif'),
      ('2F', '2F'),
      ('4F', "4F"),
      ('6F', '6F'),
      ('4FL', '4FL'),
      ('EL1', 'EL1'),
      ('EL7', 'EL7'),
      ('Spéciale', "Spéciale")
   )

couleur = (
    ('FCH', 'Chêne'),
    ('FAC', 'Acajou'),
    ('FJP', 'Joplin'),
    ('FWE', 'Wengue'),
    ('BL', 'Blanc')
)

nombreventaux = (
    ('1', '1'),
    ('2', '2'),
)

mecaserrure = (
    ('SM', 'Sans mécanisation'),
    ('GC', 'Grande clé'),
    ('PC', 'Petite clé'),
    ('G', 'à gache'),
    ('C', 'Condamnation'),
    ('FELSI', '1 Point Sécurité'),
    ('FELDE', '3 Point Sécurité'),
    ('AP', 'Anti-Panique'),
    ('SCF', 'SERRURE COUPE FEU'),
    ('SCFDV', 'SERRURE COUPE FEU  DOUBLE VANTAUX'),
)

protecteur = (
    ('P1F', '1Face'),
    ('P2F', '2Faces'),
    ('SP', 'Sans protecteur')
)

sens = (
    ('D', 'Droite'),
    ('G', 'Gauche'),
    ('SS', 'Sans sens'),
)

vitrage = (
    ('SV', 'Sans vitre'),
    ('VB', 'Vitrage Bas'),
    ('VC', 'Vitrage Coté'),
    ('VH', 'Vitrage Haut'),
    ('VO', 'Vitrage Oculus'),
)

grille = (
    ('GA', "Mecanisation de grille et grille d'Airation"),
    ('GSA', "Mécanisation De Grille Sans grille d'Airation"),
    ('SM', "Sans Mécanisation"),
)

quincaillerie = (
    ('N', "Niquel"),
    ('SQ', "Sans quincaillerie"),
)

serrure=(
    ('Oui', 'Oui'),
    ('Non', 'Non'),
)


class Ville (models.Model) :
    id = models.AutoField(primary_key=True)
    designation = models.CharField(max_length=50)
    region = models.CharField(max_length=4, blank=True, null=True)

    def __str__(self):
        return self.designation

class Profile (models.Model ):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    typeUser = models.CharField(max_length=13, choices=typeUser, default='dis')
    niveau = models.CharField(max_length=30, choices=Niveau, default='dis')
    #pic = models.ImageField(upload_to=None)
    num = models.CharField(max_length=100, blank=True, null=True)
    addresse = models.CharField(max_length=300, blank=True, null=True)
    ville = models.ForeignKey(Ville, on_delete=models.CASCADE)
    tir_id_wave = models.CharField(max_length=20, blank=True, null=True)
    responsable = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    first_login = models.BooleanField(default=False)
    active = models.BooleanField(default=True)


    def __str__(self):
        return self.user.username


class DistributeurPot (models.Model) :
    id = models.AutoField(primary_key=True)
    designation= models.CharField(max_length=120)
    email = models.CharField(max_length=150, blank=True, null=True)
    num = models.CharField(max_length=100, blank=True, null=True)
    addresse = models.CharField(max_length=300, blank=True, null=True)
    ville = models.ForeignKey(Ville, on_delete=models.CASCADE)
    responsable = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    niveau = models.CharField(max_length=30, choices=Niveau, default='dis')
    tir_id_wave = models.CharField(max_length=20, blank=True, null=True)
    active = models.BooleanField(default=False)
    vue = models.BooleanField(default=False)

    def __str__(self):
        return self.designation


class ShowroomDepot (models.Model): #Showrooms et depot
    id = models.AutoField(primary_key=True)
    designation = models.CharField(max_length=120)
    num = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=150, blank=True, null=True)
    responsable = models.ForeignKey(Profile, on_delete=models.CASCADE)
    addresse = models.CharField(max_length=300)
    type = models.CharField(max_length=4, choices=typeShowroomDepot, default='show')
    ville = models.ForeignKey(Ville, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)  #............why active default True?

class ShowroomDepotRel(models.Model) :
    id = models.AutoField(primary_key=True)
    showroom = models.ForeignKey(ShowroomDepot, on_delete=models.CASCADE, related_name='Showroom')
    depot = models.ForeignKey(ShowroomDepot, on_delete=models.CASCADE, related_name='Depot')
    active = models.BooleanField(default=True)  #................... why active and and why True?

class Ouvrant(models.Model) :
    id = models.AutoField(primary_key=True)

    #.......why ?!




class Stock (models.Model):
    id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=1, choices=typeProduit, default='O')
    action = models.CharField(max_length=1, choices=typeAction, default='E')
    depot = models.ForeignKey(ShowroomDepot, on_delete=models.CASCADE)
    quantite = models.IntegerField()
    typePorte = models.CharField(max_length=7, choices=typePorte, default='pp')
    modelePorte = models.CharField(max_length=8, choices=modeleporte, default='STAR')
    couleur = models.CharField(max_length=5, choices=couleur, default='FCH')
    nombreVentaux = models.CharField(max_length=1, choices=nombreventaux, default='1')
    largeurPrecadre = models.CharField(max_length=10, blank=True, null=True)
    hauteur = models.CharField(max_length=10, blank=True, null=True)
    hauteurSup = models.CharField(max_length=10, blank=True, null=True)#.....................?!
    largeur1o = models.CharField(max_length=10, blank=True, null=True) #.....................?!
    largeur10sup = models.CharField(max_length=10, blank=True, null=True) #.....................?!
    mecaSerrure = models.CharField(max_length=6, choices=mecaserrure, default='GC')
    serrure = models.CharField(max_length=3, choices=serrure, default='Oui')
    protecteur = models.CharField(max_length=4, choices=protecteur, default='P1F')
    sens = models.CharField(max_length=2, choices=sens, default='D')
    vitrage = models.CharField(max_length=4, choices=vitrage, default='SV')
    grille = models.CharField(max_length=4, choices=grille, default='GA')
    quincaillerie = models.CharField(max_length=4, choices=quincaillerie, default='GA')
    epaisseurMur = models.CharField(max_length=10, blank=True, null=True)
    epaisseurMurSup = models.CharField(max_length=10, blank=True, null=True) #.....................?!
    cadreUtilise = models.CharField(max_length=10, blank=True, null=True)
    embrochure = models.CharField(max_length=10, blank=True, null=True)
    couvreJointHauteur = models.CharField(max_length=10, blank=True, null=True)
    couvreJointLargeur = models.CharField(max_length=10, blank=True, null=True)
    coupeCouvreJoint = models.CharField(max_length=10, blank=True, null=True)


