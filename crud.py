# -*- coding: utf-8 -*-

import sqlite3

print('Bienvenu dans crud python')

conn = sqlite3.connect('crud_db.db')

cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS etudiants(
     id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
     nom TEXT,
     prenom TEXT,
     classe TEXT,
     age INTERGER
)
""")
conn.commit()


recommencer = True

while recommencer:

    print('1.Ajouter')
    print('2.modifier')
    print('3.supprimer')
    print('4.Afficher')


    # Opération
    choix = int(input('Veullez choisir une operation: '))

    while choix > 4 or choix < 1:
        choix = int(input('Veullez choisir un choix correct: '))

    if(choix == 1):
        
            prenom = str(input("Saisir le prenom de letudiant: "))
            nom = str(input("Saisir le nom de l'etudiant: "))
            classe = str(input("Saisir la classe de l'etudiant: "))
            age = int(input("Saisir l'age de l'etudiant: "))

#data = {"nom" : "tall, "prenom" : "mor", "classe" : "licence", "age" : 25}

            cursor.execute("""
            INSERT INTO etudiants(nom, prenom, classe, age) VALUES(?,?,?,?)""", (nom,prenom,age,classe)) 

    elif choix ==2:
            cursor.execute("""SELECT * FROM etudiants""")
            etudiant = cursor.fetchall()
            print(etudiant)

            recup = int(input("choisir l'étudiant à modifier "))
            cursor.execute("""SELECT * FROM etudiants WHERE id=?""", (recup,))
            modif = cursor.fetchone()
            print(modif)
            
            print('1-nom')
            print('2-prenom')
            print('3-age')
            print('4-classe')

            ch=int(input('veuillez choisir le champ à modifier: '))
            while ch > 4 or ch < 1:
                ch = int(input('Veullez faire un choix correct: '))

            
            if(ch==1):
                 nom = str(input("Saisir le bon nom l'etudiant: "))
                 cursor.execute("""UPDATE etudiants SET nom = ? WHERE id = ?""", (nom,recup,))

            if(ch==2):
                 prenom = str(input("Saisir le bon prenom de l'etudiant: "))
                 cursor.execute("""UPDATE etudiants SET prenom = ? WHERE id = ?""", (prenom,recup,))

            if(ch==3):
                 age = int(input("Saisir la bonne age de l'etudiant: "))
                 cursor.execute("""UPDATE etudiants SET age = ? WHERE id = ?""", (age,recup,))

            if(ch==4):
                 classe = str(input("Saisir la nouvelle classe de l'etudiant: "))
                 cursor.execute("""UPDATE etudiants SET classe = ? WHERE id = ?""", (classe,recup,))

            cursor.execute("""SELECT * FROM etudiants""")
            etudiant = cursor.fetchall()
            print(etudiant)

            

    elif choix == 3:
        cursor.execute("""SELECT * FROM etudiants""")
        etudiant = cursor.fetchall()
        print(etudiant)

        sup=int(input('veuillez choisir le numéro de létudiant à supprimer: '))
        cursor.execute("""DELETE FROM etudiants WHERE id = ?;""",(sup,))

    elif choix==4:
        cursor.execute("""SELECT * FROM etudiants""")
        etudiant = cursor.fetchall()
        print(etudiant)
        


    reponse =input('Voulez-faire une autre operation o/n: ')

    if(reponse == 'o'):
        recommencer = True
    else:
        recommencer = False