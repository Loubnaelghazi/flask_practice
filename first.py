
#Ceci est notre premier programme ecrit en Flask 

from flask import Flask ,render_template



my_app=Flask(__name__)   #je vais donner un nom unique a mon app

#la creation de routes de mon app se fait comme ca :

@my_app.route("/") #indque ma page pricipale  avantr chaque fct qui v mwe definir son contenu 
def home_page():
    return "Home page "


#meme chose pour les autres pages 


@my_app.route("/contact")
def contact():
    return "Contact"

@my_app.route("/<name>") #ici 3la hsab user ina smeya ayktb ktsema had tag b  Variable
def name(name):
    return 'Hello %s' %name       #rdi trecupera hna 


#integration des pages html :
@my_app.route("/about")
def about():

    return render_template('about.html',pagetitle='About' ,custom_css=about)   #kn3ytu 3la pages dylna haka .n9dru nbdlu title d page mn hna bdak attribute 
 #note : druri les fichiers html bch et9raw khshum etdaru f dossier smetu tmeplates 
 ###############################################################################################3

#part 2 :

@my_app.route('/test')
def test():
    return render_template('test.html' , pagetitle='TEST') #hna rdi ntestiw le fait anaha t afficha  bla css 
















#pour executrer l application :
if __name__=='__main__': #y3ni ila kantt ktexecute hna fns fichier mchy knimportiwh f blasa khra 
        
    my_app.run(debug=True)

