from flask import Flask, render_template, request
import random
#pip install flask
app = Flask(__name__)

@app.route("/", methods = ["GET"])
def index():

    return render_template("index.html")
    #return "<p>Hellooooooooo World!</p>"


@app.route("/Ball", methods = ["POST"])
def Ball():
    tmp = dict(request.form)
    ime1 = tmp.get("ime1")
    moje_besede = ["Da", "Ne", "Mogoče", "Vprašaj Kasneje", "Zdi se, da ti je usoda naklonjena... ali pa ni.",
    "Izgleda, da je bil odgovor včeraj, danes pa ga že pozabi.",
    "Če bi vedel odgovor, bi ti ga povedal. Ampak sem preveč skrivnosten.",
    "Tvoje možnosti so bolj meglene kot moj vid.",
    "Odvisno od tega, kaj si pojedel za zajtrk.",
    "Ali nisi slučajno vprašal že pred 5 minutami?",
    "Morda! Ampak tudi morda ne. Hm.",
    "Boljši odgovor boš našel v Siri.",
    "Tvoje življenje je kot ta odgovor - polno presenečenj.",
    "Nekaj mi pravi, da boš še naprej čakal na odgovor.",
    "Mislim, da je to bolj filozofsko vprašanje.",
    "Preveri vremensko napoved za odgovor.",
    "Hmm, preden odgovorim, povej mi, kakšne nogavice nosiš.",
    "Še vedno se sprašujem, če sem pravi vir za ta odgovor.",
    "Hmmm... lahko bi bilo huje. Lahko bi bilo bolje.",
    "Odgovor je v tvoji roki... če držiš to kroglo pravilno!"]
    r = f"{ime1} {random.choice(moje_besede) }"
    return render_template("index.html", rezultat = r)
    
    #return f"{ime1} + {ime2} = {random.randint(0,100)} %"
    #Naloga z IF

    #if "ljubezen" in ime1.lower():
        #odgovor = "Kupi raje GPU."
    #elif "vikend" in ime1.lower():
       # odgovor = "TikTok all day."
    #elif "denar" in ime1.lower():
        #odgovor = "Burek only."
    #elif "profesor" in ime1.lower():
       # odgovor = "F speedrun."
   # elif ime1.endswith("!"):
       # odgovor = "Ne kriči."
   # else:

app.run(debug= True)