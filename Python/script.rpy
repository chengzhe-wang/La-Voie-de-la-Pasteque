# Vous pouvez placer le script de votre jeu dans ce fichier.

# Déclarez sous cette ligne les images, avec l'instruction 'image'
# ex: image eileen heureuse = "eileen_heureuse.png"

python hide:
     import os

transform alpha_dissolve:
    alpha 0.0
    linear 0.5 alpha 1.0
    on hide:
        linear 0.5 alpha 0
    # This is to fade the bar in and out, and is only required once in your script

### Compte à rebours ###
screen countdown:
    timer 1 repeat True action If(time > 0, true=SetVariable('time', time - 1), false=[Hide('countdown'), Jump(timer_jump)])
    if time <= 1:
        text str(time) xpos .47 ypos .816 color "#FF0000" at alpha_dissolve
    else:
        text str(time) xpos .47 ypos .816 color "#202C3D" at alpha_dissolve

init :
    $ import time
    $ year, month, day, hour, minute, second, dow, doy, dst = time.localtime()
    $ timer_range = 0
    $ timer_jump = 0

# Déclarez les personnages utilisés dans le jeu.
define vide = Character(None, window_background = None, what_color = "#202C3D", what_size = 27)
define dp = Character('Dieu Pastèque', color="#E9383F")
define moi = Character('Moi', color="#c0c0c0")
define flash = Fade(0.2, 0.0, 0.8, color="#FFF")
define lflash = Fade(0.8, 0.0, 0.2, color="#FFF")
define bflash = Fade(0.8, 0.0, 0.8, color="#000000")
define ombre = Character('???', color='#6C655E')
define mc = Character('[nom]', color="#2C76FF")
define a3t = Character('A3T', color='#FEA2A2')
define ch = Character('Charlie', color='#3AD514')
define gnome = Character('Gnome', color="#39A81E")
define cailloux = Character("Cailloux magique")
define singe = Character("Singe??")
define vpyramide = False
define vpyramidein = False
define vintpyramide = False
define vlaby = False
define vlaser = False
define vtour = False
define vporte = False
define vtemps = False
define clef = False

define A = Character('Angel', color="#023ff7")
define me = Character('[nomduheros]', color="#023ff7")
define ki = Character('Kirumi',color="#1DB400")
define ma = Character('Maki', color="#00e9ff")
define D = Character('Roi Démon', color="#ff0000")
define H = Character('Héros', color="#1dff00")


define prologue = "Chapitre 1"
define Chapt1 = "Chapitre 2"
define Pass = "Dans le passé"
define Chapt2 = "Chapitre 3"
define Chapt3 = "Chapitre 4"

# Le jeu commence ici
label start:

    scene bg paradis
    play music "paradis_musique.mp3" fadeout 1
    moi "Où suis-je ?"

    show aura
    with dissolve

    moi "Un ange ? Dieu ?"

    hide aura

    show dp_smile
    with dissolve

    moi "Une... pastèque ???"

    show dp_talk

    dp "Bienvenue au Paradis des Pastèques."

    moi "Je... Je suis mort ?"

    hide dp_smile
    hide dp_talk
    scene bg tunnel
    with lflash
    stop music fadeout 1

    moi "Mes... souvenirs ?"
    play music "Treize.mp3"
    ombre "Vite ! Il faut s'enfuir !"


    show ombre:
        xalign 0.0
        yalign 1.0
    with dissolve

    ombre "Il arrive !"

    show ombre at center
    with move
    ombre "Par ici !"

    scene bg tunnel cote
    with flash
    show ombre at left

    ombre "Dis-moi... c'est quoi ton nom ?"
    $ nom = renpy.input("Entrez votre nom.")
    $ nom = nom.strip()
    if not nom:
        $ nom = "Moi"

    ombre "[nom] ? Très charmant...\nDépêche-toi on n'a plus le temps !
    \nIl va nous rattraper."

    show ombre at right
    with move

    ombre "Viens vite !"

    scene bg tunnel fin
    with dissolve

    ombre "On y est presque !"
    scene bg portails
    with lflash

    ombre "Mince, il n'est plus là..."
    ombre "Choisis un portail rapidement, on doit s'enfuir d'ici !"
    mc "Des portails ? Mais où-suis je ?"
    ombre "Si t'as le temps de parler, alors t'as le temps de courir, vite prends un portail !
    \nChaque portail mène à un monde différent."
    jump portails

label portails :
    menu :
        ombre "Lequel veux-tu prendre ?"
        "Vert" :
            ombre "Le vert c'est bien ça ? Je suis juste derrière toi, rentre vite !"
            stop music
            jump hakim
        "Bleu" :
            ombre "Le bleu c'est bien ça ? Je suis juste derrière toi, rentre vite !"
            stop music
            jump chen
        "Rouge" :
            ombre "Le rouge c'est bien ça ? Je suis juste derrière toi, rentre vite !"
            stop music
            jump fred

###############################################
################# Hakim #######################
###############################################

label hakim:
    #$inventory.append(sword_item)
    #$inventory.append(pie_item)
    #$inventory.append(cauldron_item)
    #$inventory.append(shield_item)
    scene black
    with dissolve
    $ renpy.movie_cutscene("teleportation.webm")
    scene black
    $ msg = renpy.notify (prologue)
    play music "m.mp3" fadeout 1
    "Que s'est-il passé ?"
    "Cet endroit, je ne le reconnais pas..."
    "Je ne me souviens plus de rien..."
    scene 1
    with dissolve
    moi "Où suis-je ?"
    moi "Il n'y avait pas quelqu'un avec moi ?"
    with flash
    scene angel
    with dissolve


    A "Héros, bienvenue à toi dans ce monde."
    A "Je suis Angel, un esprit."
    A "Je suis ici pour te guider."
    A "Comment vous appelez-vous?"

    $ nomduheros = renpy.input("Entrez un nom.")
    $ nomduheros = nomduheros.strip()
    if not nomduheros:
        $ nomduheros = "Kinori"


    me "Je sais plus, je crois que je m'appelle [nomduheros]."

    A "Comme je le disais il y a peu, je suis là pour te guider [nomduheros]."
    A "Tu es donc réincarné."
    me "Réincarné !?"
    A "Oui, tu as été tué dans ton monde."
    A "Ce monde..."
    A "est séparé en plusieurs royaumes."
    A 'Le royaume "Hommes" et "Démons."'
    A "Ces deux royaumes sont en guerre depuis plusieurs siècles."
    A "Voilà les grandes lignes."
    A 'Donc tu seras réincarné dans le royaume des "Hommes."'
    me "Mmmh... Intéressant."
    A "Prépares-toi à l'?."
    me "Euhhh...Comment !?"
    me "Que se passe t-il !?"

    stop music

    $ renpy.movie_cutscene("TP.ogv")



    with flash
    scene party1
    with dissolve

    $ msg = renpy.notify (Chapt1)
    play music "sekai.mp3"
    me "Où suis-je?"
    show stand7
    with dissolve

    "???" "Bonjour..."
    hide stand7
    with dissolve

    me "Bon...jour."
    show stand1
    with dissolve

    "???" "Qui êtes-vous?"
    hide stand1
    with dissolve

    me "Je suis [nomduheros] et vous ?"
    hide stand1
    with dissolve

    show stand7
    with dissolve
    '???' "Je m'appelle Kirumi Toujo."
    hide stand7

    show stand3
    with dissolve
    me "Désolé, mais où sommes-nous."
    ki "Vous êtes perdu?"
    me "Oui, plus ou moins."
    ki "Comment cela ?"
    hide stand3
    me "Je ne m'en rappelle plus..."

    with flash
    with vpunch
    with flash
    scene interieur
    with dissolve

    me "Que s'est-il passé ?"
    me "Où suis-je encore ?"
    show stand4
    ki "Tu t'es évanoui."
    me "J'ai un mal de tête."
    "Cela me paraît très bizarre."
    ki "Allons dehors."
    hide stand4
    scene grotte
    with dissolve
    me "Tu vis ici ?"
    show stand10
    with dissolve
    ki "Oui."

    ki "Que fais-tu ici dans le coin ?"
    me "Je ne sais pas."
    ki " ... ??"
    hide stand10
    with dissolve
    me "Désolé mais je ne m'en rappelle vraiment plus."
    me "Je me rappelle juste d'une personne... \"Angel\"."
    me "Mais pas plus."

    show stand8
    with dissolve
    "???" "Ahhhhhh!!..."
    me "D'où vient ce cri ?"
    me "Allons voir."
    ki "D'accord."
    hide stand8

    scene party1
    show maki7
    "???" "À l'aide..!"
    hide maki7

    menu:
        ki "Aidons-la."

        "Oui":
            ki "Vas-y."
            jump qte

        "Laisse-moi faire.":
            ki "D'accord."
            jump qte

    label qte:

    show latest

    $ cont = 0
    $ arr_keys = ["K_SPACE"]
    call qte_setup(0.5, 0.5, 0.01, renpy.random.choice(arr_keys), renpy.random.randint(1, 9) * 0.1, renpy.random.randint(1, 9) * 0.1) from _call_qte_setup

    $ counter = 0
    while cont == 1 and counter < 10:
        call qte_setup(0.5, 0.5, 0.01, renpy.random.choice(arr_keys), renpy.random.randint(1, 9) * 0.1, renpy.random.randint(1, 9) * 0.1) from _call_qte_setup_1
        $ counter = counter + 1

    if counter == 10:

        "Réussi"
    else:
        "{b}Game Over{/b}"
        "On recommence"

        jump qte




    label suit2:

    me "Euh...hmm, un peu d'aide."
    with vpunch
    with vpunch
    with flash
    hide latest
    me "Bon bah..."
    show maki13

    "???" "Merci."
    me "De rien."
    hide maki13

    show stand12
    with dissolve
    ki "Maki..!"
    show maki15:
        xalign 0.9
        yalign 1.0
    with dissolve

    hide stand12
    show stand7
    ma "Kirumi, qui est-ce?"
    ki "C'est [nomduheros]."
    mc "Enchanté."
    hide maki15
    hide stand7
    me "Qui sont-ils, pourquoi vous ont-ils attaqué ?"
    show stand2
    with dissolve
    ki "Tu vis dans quel monde ? C'est des démons..."
    ki "Mais... Que font-ils ici ? Nous sommes pourtant loin de leur royaume..."
    ki "De plus nous sommes dans un coin très reclus."
    me "Un démon !?"
    ki "Oui..."
    hide stand2

    show maki11
    with dissolve
    ma "Je vais te raconter une petite histoire."
    ma "Il fut un temps, un héros était dans le village à côté."
    ma "Il paraît que ce héros est parti combattre le Roi Démon."
    ma "Mais depuis on....."


    scene angel
    with lflash

    A " [nomduheros], je te transporte dans le corps du héros."
    me "Qui êtes-vous..?"
    A "Tu m'as déjà oublié."
    A "Bon pas grave."

    scene party4

    show heros
    with dissolve
    $ msg = renpy.notify (Pass)

    play sound "epee.mp3"
    H "Roi Démon, je suis là pour te combattre."

    hide heros

    play music "battle.mp3"


    show monster
    D "GRHhaaaaah!!!"

    scene party5
    with dissolve

    show heros
    with dissolve
    H "On continue. Ahhhh...!!"
    hide heros
    with dissolve

    show monster
    with dissolve

    label qte1:

    $ cont = 0
    $ arr_keys = ["K_SPACE","K_UP","K_DOWN","K_LEFT","K_RIGHT"]

    call qte_setup(0.5, 0.5, 0.01, renpy.random.choice(arr_keys), renpy.random.randint(1, 9) * 0.1, renpy.random.randint(1, 9) * 0.1) from _call_qte_setup_2

    while cont == 1 and counter < 10:
        call qte_setup(0.5, 0.5, 0.01, renpy.random.choice(arr_keys), renpy.random.randint(1, 9) * 0.1, renpy.random.randint(1, 9) * 0.1) from _call_qte_setup_3
        $ counter = counter + 1

    if counter == 10:

        "Réussi"
    else:
        "{b}Game Over{/b}"
        "On recommence"

        jump qte1

    label suit3:

    with flash
    with vpunch
    with flash

    scene party6

    show monster
    with dissolve
    D "ARGHHhhhh..!!"
    hide monster

    show heros
    with dissolve
    H "Il a encore disparu."
    hide heros

    stop music
    $ msg = renpy.notify (Chapt2)

    scene party2
    with dissolve

    show stand4
    with dissolve
    ki "Que se passe-t-il ? Le temps..."

    show maki1:
        xalign 0.9
        yalign 1.0
    ma "L'apparition du Roi démon..?"
    me "..."
    me "Allons-y."
    ma "Quoi !!!"
    ki "Nous n'avons pas le choix."
    hide stand4
    hide maki1

    scene party7

    me "Nous y voilà."
    show stand9
    with dissolve
    ki "Prépare-toi, Roi démon."
    hide stand9

    show monster
    with dissolve
    play music "battle.mp3"

    D "GRHhaaaaah!!!"


    label qte2:

    $ cont = 0
    $ arr_keys = ["K_SPACE"]

    call qte_setup1(0.5, 0.5, 0.01, renpy.random.choice(arr_keys), renpy.random.randint(1, 9) * 0.1, renpy.random.randint(1, 9) * 0.1) from _call_qte_setup1

    while cont == 1 and counter < 10:
        call qte_setup1(0.5, 0.5, 0.01, renpy.random.choice(arr_keys), renpy.random.randint(1, 9) * 0.1, renpy.random.randint(1, 9) * 0.1) from _call_qte_setup1_1
        $ counter = counter + 1

    if counter == 10:

        "Réussi"
    else:
        "{b}Game Over{/b}"
        "On recommence"

        jump qte2

    me "Finissons-le."

    with flash
    with vpunch
    with vpunch

    hide monster
    stop music

    show stand1
    with dissolve
    ki "Nous avons réussi."

    show maki12:
        xalign 0.9
        yalign 1.0

    with dissolve

    ma "Trop fort."
    play music "F.mp3"

    show fin
    with dissolve

    me "Bien que je me rappelle de plus rien, je suis bien content de les avoir connues."


label restart2 :
    scene bg paradis
    with lflash
    show dp_talk
    dp"Fini de rêver ?"
    scene bg portails
    with lflash
    jump portails

###############################################
################ Frédéric #####################
###############################################

label fred:
    scene black
    with dissolve
    $ renpy.movie_cutscene("teleportation.webm")

    scene arr
    play music "m.mp3"
    mc" ...."
    mc" Je rêve ?"
    mc "L'enflure, il m'a abandonné..."
    "Vous avez soudainement une irrésistible envie de dormir..."

    scene black
    with dissolve
    mc"..."
    mc"....."

    scene chemin
    with dissolve
    show oie_transparent:
        xalign .3 yalign .7
        linear 1.0 xalign .7 yalign .7

    singe " Wow toi t'as pris des champis chelous."
    singe " Bon allez, je te montre les alentours."

    menu:
        "Ok":
            jump C11
        "Mais tu t'es pris pour qui ? Comme si j'allais suivre un singe mal dessiné sur paint":
            jump C12

label C11:
    $ menu_flag = True
    singe "Cool, suis-moi !"
    jump B1

label C12:
    $ menu_flag = False
    singe "Bah débrouille-toi."
    jump B2

label B2:
    show chemin
    hide oie_transparent
    mc  "Bon je vais où, moi?"
    mc  "À droite !"
    jump CD

label CD:
    show grotte2
    with dissolve
    mc"OK...."
    mc"En même temps, le jeu est nul alors...."
    show th
    mc"Whattt !?"
    show dragon
    with flash
    mc ".... Bon allez, j'ai pas d'idée de suite donc..."
    mc "Jouons à un minijeux !"
    jump start111

label  B1:
    hide oie_transparent
    show black
    with dissolve
    mc "Mec c'est sombre..."
    singe "Tu es vraiment naïf !"
    mc "Whaaa---"
    "..."
    "Vous ne voyez rien..."
    mc"(CHU devenu aveugle !!?)"
    mc"(Je ne vois qu'une seule conclusion logique)"
    mc"À l'aide ! Le singe m'a kidnappé pour vendre mes yeux à ses potes pour guérir leur impuissance."
    singe "Mais qu'est-ce que tu racontes ?"
    show chateau
    with dissolve
    show oie_transparent
    singe "Bon je vais te jeter à un dragon pour te tuer "
    hide oie_transparent
    show dragon
    with dissolve
    singe "Et ne t'en fais pas ces dessins seront bientôt finis."


    jump start111


label qte_setup(time_start, time_max, interval, trigger_key, x_align, y_align):

    $ time_start = time_start
    $ time_max = time_max
    $ interval = interval
    $ trigger_key = trigger_key
    $ x_align = x_align
    $ y_align = y_align

    call screen qte_simple
    $ cont = _return
    return

screen qte_simple:
    timer interval repeat True action If(time_start > 0.0, true=SetVariable('time_start', time_start - interval), false=[Return(0), Hide('qte_simple')])

    key trigger_key action ( Return(1) )

    vbox:
        xalign x_align
        yalign y_align
        spacing 25

        text trigger_key:
            xalign 0.5
            color "#fff"
            size 36

        bar:
            value time_start
            range time_max
            xalign 0.5
            xmaximum 300
            if time_start < (time_max * 0.25):
                left_bar "#f00"

label start111:

    $ cont = 0
    $ arr_keys = ["e", "s", "q", "u","i","v", "K_SPACE"]
    play music "mha.mp3"

    call qte_setup(0.5, 0.5, 0.01, renpy.random.choice(arr_keys), renpy.random.randint(1, 9) * 0.1, renpy.random.randint(1, 9) * 0.1) from _call_qte_setup_4

    while cont == 1:
        call qte_setup(0.5, 0.5, 0.01, renpy.random.choice(arr_keys), renpy.random.randint(1, 9) * 0.1, renpy.random.randint(1, 9) * 0.1) from _call_qte_setup_5

    "{b}VOUS ÊTES MORT.{/b}"
    stop music fadeout 1
    jump restart

label restart :
    scene bg paradis
    show dp_talk
    play music "paradis_musique.mp3" fadeout 1
    dp"Bon, tu ne peux pas battre un dragon de toute façon..."
    dp"Je t'avoue que tu as fait un mauvais choix."
    dp"Je te renvoie dans le passé."
    scene bg portails
    with lflash
    jump portails

###############################################
################ Chengzhe #####################
###############################################

label chen:
    scene black
    with dissolve
    $ renpy.movie_cutscene("teleportation.webm")

    scene bg desert
    with dissolve
    play music "game_music.mp3" fadeout 1
    ombre "On est dans un monde désertique."
    show a3t
    with dissolve
    ombre "On doit trouver un moyen de retourner dans mon monde d'origine."
    mc "AAAAAH !!! Mais t'es qui toi !?"
    a3t "Tu ne te souviens pas de moi ? J'ai pris le portail avec toi.
    \nAh oui ! Je ne me suis pas présenté, je m'appelle A3T."
    a3t "Les portails font perdre la mémoire, je me souviens presque que de mon nom.
    \nTu as peut-être perdu la mémoire ?"
    mc "Non non pas du tout, je me souviens de tout...
    \nDans l'autre monde, tu avais l'air beaucoup plus... humain. Qu'est-ce qui s'est passé ?"
    a3t "Ah oui, c'est parce que lorsqu'on change de monde, notre apparence change aussi."
    mc "Tu... tu veux dire que je suis comme toi actuellement !?"
    a3t "Haha, mais non. Je blaguais, je suis le seul à qui ça fait ça.
    \nJe ne comprends pas d'ailleurs..."
    mc "Attends.. attends... je ne comprends rien à ce qu'il se passe...
    Il existe plusieurs mondes ou dimensions différentes ?"
    a3t "C'est bien ça. Et je suis ce qu'on appelle un PITRE, je voyage à travers les dimensions."
    mc "Un pitre !?"
    a3t "Il s'agit du sigle pour Portal Initiated Travelling Recognized Explorer.
    \nJe sais à quoi tu pensais..."
    mc "Je suis perdu... pourquoi est-ce que j'étais enfermé dans cette maison ?"
    a3t "Je ne sais pas trop... Je ne sais même pas si c'était ton monde ou pas.
    Dès que je suis arrivé dans ce monde, on m'a directement capturé et emprisonné.
    Je ne suis pas humain donc je n'ai pas les mêmes besoins que vous... "
    a3t "Ah ! Mais t'es humain toi. C'était très probablement ton monde alors.
    Heureusement que t'étais là, sinon je ne saurais combien de temps je serais resté enfermé là-bas.
    Je ne sais pas trop ce qu'il se passe dans ton monde."
    mc "Pourquoi est-ce qu'on a pas pris le portail de ton monde ? On serait déjà en sécurité non ?"
    a3t "Ah... il a disparu je crois. Il n'était plus là lorsqu'on est arrivé dans la salle des portails.
    Notre assaillant était à nos trousses, il fallait choisir un monde au hasard et vite."
    mc "D'ailleurs, de quel monde viens-tu ?"
    a3t "Je viens d'un monde qui s'appelle le Paradis des Pastèques, on est tous des pastèques là-bas.
    Mais étrangement, je ne suis plus ce que j'étais. Ça me trouble énormément. J'ai l'impression de prendre
    une forme qui s'adapte au monde. Non... ce n'est pas juste une impression, c'est un fait."
    mc "Le Paradis des Pastèques !? C'est quoi ce délire ? Depuis quand les pastèques sont des êtres vivants ?"
    a3t "Ça peut paraître bizarre pour un humain comme toi, mais nous sommes bel et bien vivants.
    Que faites-vous des pastèques dans votre monde ?"
    mc "On les mange..."
    a3t "COMMENT ? Quelle honte, comment pouvez-vous faire ça ?"
    mc "Bah... je sais pas, c'est comme ça."
    play sound "portail.mp3"
    "*bruit de portail*"
    a3t "Mais non, c'est pas possible ! Il nous a suivi... Vite, il faut repartir ! \nPar ici !"
    show a3t at right
    with move
    a3t "Allez viens vite !"
    scene bg pyramide loin
    with lflash
    show a3t at left
    with dissolve
    a3t "Il y a des constructions au loin tout là-bas !"
    mc "Ça a l'air vachement dangereux. J'ai vu ça dans des films, c'est bourré de pièges. Gardons la même direction."
    a3t "Mais non qu'est-ce que tu racontes. Il y a un portail d'âme là-bas, je t'assure qu'on devrait y aller."
    menu:
        a3t "Alors, on fait quoi ?"
        "Écouter A3T":
            mc "Bon, c'est d'accord on y va..."
            jump construction
        "Rester sur sa position":
            mc "Non, on continue sur notre chemin. Je ne veux pas mourir."
            a3t "... C'est comme tu veux."
            jump desert

label desert :

    scene bg desert nuit
    with bflash

    mc "Ça fait 3h qu'on marche... Je sens plus mes forces. On aurait dû aller à la pyramide..."
    a3t "Allez, tiens bon. Je vois un village au loin, on a bien fait de venir ici !"
    mc "Je suis désolé... je crois que... je crois que je vais..."

    scene black
    with flash
    stop music fadeout 1
    "Vous êtes mort de fatigue."

    scene bg paradis
    with bflash
    play music "paradis_musique.mp3" fadeout 1

    show dp_talk
    with dissolve
    dp "Alors tu avais des trous de mémoires ? Tu te souviens de tout désormais ?"
    mc "Je... je suis vraiment mort comme ça ??"

    scene black
    with bflash
    "Game over."
    dp "Allez, retente ta chance !"
    scene bg portails
    with lflash
    jump portails

label construction:

    scene bg desert crep
    with bflash

    show charlie
    with dissolve
    ch "Yo les gars ! Moi c'est Charlie. Vous savez c'est où Villejuif ? Jme suis perdu dans ce trou paumé.
    Ça fait une heure que je cherche le métro, y en a pas ici ? Comment jsuis arrivé ici déjà ?"
    a3t "Il a pas compris la situation... euh c'est juste derrière nous. Ensuite tu vas à droite."
    ch "Ok cimer les gars, vous êtes des bons. Par contre toi t'es bizarre un peu... J'ai peut-être un peu trop bu."
    hide charlie
    with Dissolve(1.0)
    mc "Mais pourquoi tu lui as pas expliquer la situation ? Il est bloqué ici à tout jamais !"
    a3t "C'est pas mon problème. Il était moche alors j'ai pas eu envie de l'aider."
    mc "Mais c'est un humain ! Il faut le sauver..."
    a3t "Je me demande comment il a pu atterrir ici. Il n'est pas là depuis longtemps et je ne l'ai pas vu
    lorsque j'étais enfermé... Il existerait d'autres portails dans votre monde ?"
    mc "J'en sais rien du tout, il faut aller l'aider !"
    a3t "C'est trop tard maintenant, on ne peut plus rien faire pour lui..."
    "AAAAAAAAAAAH !!!"
    mc "C'est Charlie ! Vite il faut aller l'aider !"
    ch "AU... AU SEC..."
    a3t "Il est mort...  Notre prédateur est juste derrière nous, il faut se dépêcher."
    mc "Pourquoi tu l'as dirigé droit vers le tueur ? Il ne méritait pas ça."
    a3t "Je n'ai aucune compassion pour vous les humains, je ne vois pas où est le problème à ce qu'ils meurent."
    mc "Tu es un monstre !"
    a3t "Vous mangez bien des pastèques... Tu es le seul humain qui mérite mon aide car tu m'as sauvé."
    menu :
        a3t "Vite, où allons-nous ?"
        "À gauche : la tour":
            mc "On va à la tour !"
            jump tour
        "À droite : la pyramide":
            mc "On va vers la pyramide !"
            jump pyramide


label pyramide :

    scene bg pyramide entree
    with dissolve
    if not vpyramide :
        a3t "Ma boussole détecte plusieurs portails pas loin. Il y a peut-être une salle des portails ici dans la pyramide."
        mc "Il y a un portail bizarre ici, il n'est pas comme ceux qu'on avait vu. C'est de ça dont tu me parlais tout à l'heure ?"
        a3t "Oui, c'est un portail d'âme. Il ne nous téléporte pas physiquement. Pourtant, on a l'impression d'être ailleurs après.
        Ils sont très rares. Tu veux le tester ?"
    elif vpyramide :
        a3t "Bon, où allons-nous cette fois ? On va dans le portail ?"

    menu:
        a3t "Alors ?"
        "Oui, allons-y.":
            if not vlaby:
                mc "C'est sans danger j'espère."
                a3t "Oui ne t'en fais pas, tu pourras toujours te déplacer ici."
                $ vpyramide = True

            elif vlaby :
                mc "On y retourne !"
            $ os.startfile("maze.exe")

        "Non, rentrons dans la pyramide.":

            if not vpyramide :
                mc "Cela ne m'inspire pas confiance. Allons dans la pyramide plutôt."
                a3t "Je pense qu'on sera forcé d'aller dans ce portail à un moment ou un autre."

            $ vpyramide = True

            jump in_pyramide
        "Allons à la tour plutôt.":
            if not vtour :
                mc "J'ai changé d'avis après mûre réflexion, on devrait aller à la tour..."
                a3t "Je te fais confiance."
            elif vtour :
                mc "Je crois qu'on a oublié quelque chose à la tour, on devrait y retourner."
            $ vpyramide = True
            jump tour
    if not vlaby :
            mc "Wow, je me sens... léger ?"
            a3t "Ton âme est à moitié dans un autre monde, tu peux le faire revenir ici quand tu veux."
            a3t "On devrait rentrer dans la pyramide pour se mettre à l'abri, on est moins vigilants actuellement."
            $ vlaby = True
    elif vlaby :
            mc "J'adore cette sensation !"
            a3t "Moi aussi. Mais retournons dans la pyramide."
    jump in_pyramide

label in_pyramide :

    scene bg pyramide porte
    with lflash
    show gnome at right
    with dissolve
    show gnome at left
    with move
    show gnome at right
    with move
    show gnome at left
    with move
    show gnome at right
    with move

    if not vpyramidein :

        gnome "Bordel, j'arrive pas à casser cette porte avec ma pioche !"
        a3t "Encore un qui vient d'un autre monde ! La salle des portails est sans doute par ici !"
        show a3t at left
        with dissolve
        a3t "Excusez-moi monsieur le... gnome ? Vous êtes un PITRE ou je me trompe ?"
        gnome "Moi !? Tout ça parce que je suis un gnome ? Franchement, vous êtes comme les autres...
        J'ai l'air si stupide que ça ?"
        a3t "Ce n'est pas ce que je voulais dire... Vous voyagez à travers les portails n'est-ce pas ?"
        gnome "Aaah... hum... Effectivement, oui. Je suis arrivé ici en dehors de la salle, c'est une particularité de ce monde je crois."
        gnome "On ne ressort pas par le portail mais on atterrit dans un endroit aléatoire."
        mc "C'est ce qui nous est arrivé ! Je me disais aussi que c'était bizarre..."
        a3t "C'est vrai... je ne l'avais pas remarqué..."
        gnome "J'essaye d'ouvrir cette porte pour avoir accès à la salle mais impossible de l'ouvrir...
        Je ne comprends pas le système de cette porte... J'ai beau taper le truc au milieu il ne se casse pas !"
        mc "Mais c'est un écran tactile ! Comment ça se fait qu'il y ait un truc comme ça ici ?"
        a3t "C'est quoi ? Je n'ai jamais rien vu de tel."
        mc "C'est un écran qui réagit lorsqu'on le touche, il détecte notre doigt. Il semblerait qu'il faut un mot de passe..."
        gnome "Ah ! Je crois savoir ce qu'il faut. C'est en rapport avec les signes sur la porte."
        a3t "LABY ? Je ne comprends pas... Il n'y a que 3 carrés, on ne peut pas écrire \"LABY\" avec les lettres en bas."

        $ vpyramidein = True

        if not vlaby:
            mc "Il y a un autre sens je crois... Il faut peut-être mieux chercher."
            gnome "Ah mais ça je peux encore vous aider ! Il faut aller dans le portail d'âme dehors, il nous téléporte dans un labyrinthe."
            gnome "Il faut peut-être réussir à trouver ce qu'il cache ?"
            a3t "Oui, allons-y."
            gnome "Je reste là, je suis trop fatigué..."

            jump pyramide

        if vlaby :
            mc "C'est le labyrinthe du portail de dehors !"
            a3t "Ah oui ! Il y avait un trésor caché. Je ne souviens plus... On l'avait trouvé ?
            Bref, je pense que le trésor doit être le mot de passe..."
            jump porte


    elif vpyramidein :

        if not vporte :
            gnome "Ah vous êtes revenus !"
            menu :
                gnome "Vous avez trouvé le mot de passe ?"
                "Oui":
                    jump porte
                "Non":
                    gnome "Les gars, faites un effort ! Retournez-y !"
                    jump pyramide
        elif vporte :
            gnome "Bon, on y retourne ?"
            jump intpyramide

label porte :
    scene bg pyramide porte
    with flash
    $ mdp = renpy.input("Rentrez le mot de passe :")
    if mdp == "A3T" :
        $ vporte = True
        jump intpyramide
    else :
        a3t "La porte ne s'ouvre pas."
        mc "C'était pas le bon mot de passe..."
        gnome "Ah dommage, vous allez réussir, n'abandonnez pas !"
        jump pyramide

label intpyramide :

    scene bg int pyramide
    with lflash
    if not vintpyramide :
        mc "Qu'est-ce qu'il se passe ?"
        mc "Pourquoi c'est ton nom le mot de passe ?"
        a3t "Je... je ne comprends pas non plus..."
        a3t "Je ne suis jamais venu ici pourtant... Est-ce à cause de ma mémoire ?"
        a3t "Je ne sais pas ce qu'il se passe."
        gnome "Qu'est-ce que vous marmonner tous les deux là ?"
        mc "C'est rien..."
        mc "D'ailleurs, il ne semble plus être derrière nous, le méchant."
        a3t "En effet... je crois qu'il s'est contenté de Charlie."
        mc "Quel horreur... Il s'est sacrifié pour nous malgré lui, tout ça à cause de toi !"
        a3t "Oh c'est bon ça va... On est en sécurité maintenant."
        gnome "Un méchant ? Quel méchant ?"
        mc "Non c'est rien."
        gnome "C'est pas juste, vous gardez tout entre vous. Je compte pour du beurre moi ?"
        mc "Mais non, c'est juste que tu ne comprendras pas."
        gnome "C'est vrai que j'ai toujours eu du mal à comprendre les histoires hahaha."
        a3t "On est arrivés."
        $ vintpyramide = True
    elif vintpyramide :
        mc "Toujours aussi long ce chemin..."
    if clef :
        scene black
        with lflash
        mc "Une porte verrouillée ? On a la clef ! Je t'avais bien dit qu'elle nous servirait cette clef !"
        a3t "T'as raison..."
        jump laser
    elif not clef :
        scene black
        with lflash
        a3t "Une porte verrouillée ? Il nous faut une clef..."
        gnome "Je n'ai pas de clef sur moi."
        mc "Il y a sûrement quelque chose dans la tour à mon avis, allons voir !"
        jump tour

label laser:
    scene bg porte laser
    with lflash
    if not vlaser :
        mc "Une porte avec un laser qui s'arrête en plein milieu de son chemin ?"
        gnome "Oh ! Des boutons en couleurs ! J'ai envie de les taper avec ma pioche."
        mc "Non attends, on en a besoin pour ouvrir la porte. Il faudra appuyer sur le bon bouton."
        a3t "Qu'est-ce qu'il faut faire ? Je ne comprends pas."
        $ vlaser = True
    elif vlaser :
        if not vtemps :
            mc "J'ai l'impression d'être revenu dans le temps..."
            a3t "Qu'est-ce que tu racontes encore ? On vient d'arriver ici..."
            mc "Vous vous souvenez pas d'après, lorsqu'on a appuyé sur un bouton ?"
            gnome "On ne l'a pas encore fait petit, tu délires ou quoi ?"
            mc "C'est bizarre... Peut-être que seul celui qui est en possession de la clef trouvée dans la Tour du Temps garde les souvenirs ?"
            mc "Mais tout de même, voyager dans le temps... C'est possible ça ? Mais jsuis bête, c'est forcément possible s'il existe le voyage dimensionnel..."
            gnome "Encore parti dans une histoire bizarre..."
            a3t "Je ne comprends rien à ce que tu racontes..."
            $ vtemps = True
        elif vtemps :
            mc "Encore..."
    scene bg porte laser 1
    with dissolve
    gnome "Des trucs sont apparus, il y a un compte à rebours..."
    mc "Il faut regarder où arrive le laser, il rebondit sûrement sur les miroirs noirs !"
    gnome "Il faut appuyer quelque part, vite !"
    $ time = 3
    $ timer_jump = 'times_up'
    show screen countdown
    menu:
        vide "Oui mais quel bouton ?"
        "Rouge !":
            hide screen countdown
            play sound "portail.mp3"
            scene black
            with lflash
            jump laser

        "Bleu !":
            hide screen countdown
            mc "La porte s'est ouverte !"

        "Vert !":
            hide screen countdown
            play sound "portail.mp3"
            scene black
            with lflash
            jump laser

    scene bg porte laser 2
    with lflash
    gnome "Encore une porte !?"
    $ time = 3
    $ timer_jump = 'times_up'
    show screen countdown
    menu:
        vide "Quel bouton ?"
        "Rouge !":
            hide screen countdown
            mc "La porte s'est ouverte !"

        "Bleu !":
            hide screen countdown
            play sound "portail.mp3"
            scene black
            with lflash
            jump laser

        "Vert !":
            hide screen countdown
            play sound "portail.mp3"
            scene black
            with lflash
            jump laser
    scene bg porte laser 3
    with lflash
    gnome "ENCORE !?"
    $ time = 3
    $ timer_jump = 'times_up'
    show screen countdown
    menu:
        vide "Quel bouton ???"
        "Rouge !":
            hide screen countdown
            play sound "portail.mp3"
            scene black
            with lflash
            jump laser
        "Bleu !":
            hide screen countdown
            mc "La porte s'est ouverte !"

        "Vert !":
            hide screen countdown
            play sound "portail.mp3"
            scene black
            with lflash
            jump laser

    jump pyramidefin

label times_up :
    "Temps écoulé..."
    play sound "portail.mp3"
    scene black
    with lflash
    jump laser

label pyramidefin:
    scene bg portails fin
    with lflash
    mc "C'est ouvert !"
    a3t "C'est la salle des portails !"
    show gnome at left
    with dissolve
    gnome "Ouiiiii, je vais enfin pouvoir rentrer chez moi."
    mc "Vos mondes sont là ?"
    show a3t
    with dissolve
    a3t "Oui, c'est celui juste au milieu."
    show gnome at right
    with move
    gnome "Merci les gars c'était sympa, je pars par ici moi."
    hide gnome
    with Dissolve(1.0)
    a3t "Nous aussi on y va, par ici."
    hide a3t
    with Dissolve(1.0)
    jump fin

label tour :

    if not clef :
        scene bg tour
        with lflash
        if not vtour :
            mc "La Tour du Temps ? Quel nom... merveilleux, on se croirait dans un film."
            a3t "Ah... ma tête... J'ai l'impression de reconnaître cet endroit. Non, ce n'est pas possible, je ne suis jamais venu ici..."
            mc "Tu m'avais parlé de perte de mémoire. J'ai l'impression que tu te souviens encore de pas mal de choses..."
            a3t "C'est parce que j'ai vécu très longtemps, ce qui est peu pour moi est beaucoup pour toi."
            mc "Ah, je vois..."
            mc "Bon, entrons à l'intérieur."

        elif vtour :
            mc "Bon, on fait quoi maintenant ?"

        menu :
            a3t "On devrait peut-être aller à la pyramide, j'ai un mauvais pressentiment."
            "Allons dans la tour !":
                mc "Mais non, ne t'en fais pas. Je suis sûr que tout se passera bien."
                a3t "Si tu le dis..."
                $ vtour = True
                jump int_tour
            "Allons à la pyramide.":
                mc "Tu as peut-être raison même si je sens qu'on sera contraint de revenir."
                a3t "Seul le temps nous le dira."
                $ vtour = True
                jump pyramide
    elif clef :
        scene bg tour block
        with flash
        mc "Ah oui, c'est bloqué ici... Pourquoi on est revenus ? Retournons à la pyramide."
        jump pyramide

label int_tour :
    if 0 <= hour < 3 or 12 <= hour < 15:
        scene bg porte temps 1
        with lflash
        play sound "clock.ogg"
    elif 3 <= hour < 6 or 15 <= hour < 18:
        scene bg porte temps 2
        with lflash
        queue sound "clock.ogg"
        queue sound "clock.ogg"
    elif 6 <= hour < 9 or 18 <= hour < 21:
        scene bg porte temps 3
        with lflash
        queue sound "clock.ogg"
        queue sound "clock.ogg"
        queue sound "clock.ogg"
    elif 9 <= hour <= 12 or 21 <= hour <= 24:
        scene bg porte temps 4
        with lflash
        queue sound "clock.ogg"
        queue sound "clock.ogg"
        queue sound "clock.ogg"
        queue sound "clock.ogg"

    mc "C'est une porte avec une horloge dessus. Il y a écrit \"Présent\" tout en haut, je me demande ce que ça veut dire..."
    show a3t at left
    with dissolve
    a3t "Je pense que c'est une énigme à résoudre pour pouvoir ouvrir la porte. Regarde, on peut bouger les chiffres sur la porte."
    mc "Cela semble représenter l'heure... J'ai perdu la notion du temps, je ne saurais dire si elle est bonne ou non."
    a3t "Je ne sais pas non plus."

    menu :
        a3t "On essaye ?"
        "Oui":
            mc "Absolument, je veux essayer. 4 chiffres donc..."

        "Non":
            mc "Non, ressortons d'ici."
            jump tour

    $ year, month, day, hour, minute, second, dow, doy, dst = time.localtime() # On reprend l'heure locale où moment où on clique sur "Oui"
    $ heure = str(hour).zfill(2) # On crée une variable avec l'heure locale qui ajoute un 0 devant si c'est juste 1 chiffre
    $ minutes = str(minute).zfill(2) # Pareil mais avec les minutes
    $ mdp_temps = heure + minutes # On additionne les deux qui sont des strings pour faire un mdp
    $ mdp_tour = renpy.input("Rentrez le mot de passe :")
    if mdp_tour == mdp_temps :
        mc "Génial, je savais que c'était ça !"
        a3t "Comment tu savais que c'était ça ?"
        mc "Moi même je ne sais pas, c'était mon... instinct ?"
        a3t "Il y a des escaliers, montons !"
        scene black
        with dissolve
        mc "Il y a beaucoup de marches... C'est trop épuisant."
        a3t "Allez, encore un peu."
        mc "Comment tu fais ? Tu n'as même pas de jambes."
        a3t "J'arrive à sauter, dans mon monde je sais voler."
        mc "Oh trop cool tu m'apprendras ?"
        a3t "Je sais pas trop..."
        mc "On est arrivés, c'est pas trop tôt."
        mc "Il y a une clef, prenons-la."
        a3t "Je sais pas si c'est une bonne idée ou pas..."
        play sound "cailloux.mp3"
        "*roches qui tombent*"
        mc "COURS ! IL FAUT VITE RESSORTIR !"
        $ clef = True
        scene bg tour block
        with lflash
        mc "On a eu chaud ! On ne peut plus y retourner, l'accès est bloqué..."
        a3t "Je savais que c'était une mauvaise idée de prendre la clef... C'était donc ça mon mauvais pressentiment."
        mc "C'est pas grave, au moins on l'a maintenant. Allons à la pyramide maintenant."
        jump pyramide
    else :
        mc "La porte ne s'ouvre pas... J'aurais parié que c'était ça."
        a3t "Ressortons.. À l'heure actuelle, il faut retrouver des portails."
        mc "L'heure actuelle t'as dit ? Je crois avoir compris..."
        a3t "Quoi donc ?"
        mc "Non rien, peut-être quelque chose en rapport avec le mot de passe mais je ne suis pas sûr. Sortons."
        jump tour

label fin :

    scene black
    with flash
    stop music fadeout 1
    "..."
    mc "Où est-ce que je suis ?"

    scene bg paradis
    with bflash
    play music "paradis_musique.mp3"

    show dp_talk
    with dissolve
    dp "Alors tu avais des trous de mémoires ? Tu te souviens de tout désormais ?"
    mc "Je... je suis mort ? Qui êtes-vous ? Le Dieu Pastèque ?"
    mc "Je ne me souviens pas de tout..."
    dp "Mais c'est moi !"
    dp "A3T ! Je m'en rappelle maintenant, je suis en fait le Dieu Pastèque."
    mc "C-c-comment !?"
    dp "Ne t'en fais pas, tu n'es pas mort. Repose-toi un peu, on a fait un long voyage. Je te raconterai tout plus tard."

    scene black
    with bflash
    "À suivre..."
    return
