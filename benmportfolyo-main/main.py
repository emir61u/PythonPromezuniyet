# Import
from flask import Flask, render_template,request, redirect
from ses import turkce



app = Flask(__name__)

# İçerik sayfasını çalıştırma
@app.route('/')
def index():
    return render_template('index.html')


# Dinamik beceriler
@app.route('/', methods=['POST'])
def process_form():
    button_python = request.form.get('button_python')
    button_discord = request.form.get("button_discord")
    button_html = request.form.get("button_html")
    button_db = request.form.get("button_db")


    email = request.form.get("email")
    text = request.form.get("text")


    return render_template('index.html',button_python=button_python,
                                    button_discord = button_discord,
                                    button_html = button_html,
                                    button_db = button_db)


@app.route('/ses')
def sess():

    try:
        gibi = ""
        kayit = turkce()
        if kayit == "küresel ısınmayı tetikleyen nedenler":
            gibi = "Küresel ısınmayı; sera gazları, fosil yakıt kullanımı, ormansızlaşma, sanayi faaliyetleri, tarım ve hayvancılık gibi nedenler tetikler. "
        elif kayit == "küresel ısınmayı engellemek için ne yapmalıyız":
            gibi= "Yenilenebilir enerji, enerji verimliliği, atık yönetimi, toplu taşıma ve alternatif ulaşım gibi faaliyetlerle küresel ısınma ve etkisi azaltılabilir.  "
        elif kayit == "sera gazı etkisi nedir ve küresel ısınma ile nasıl bir bağlantısı vardır":
            gibi = "Sera gazı etkisi, belirli gazların atmosferde birikerek Dünya'nın yüzeyinden yayılan ısıyı tutma yeteneğidir. Bu gazlar, güneşten gelen ışınların atmosferden geçip yeryüzüne ulaşmasına izin verirken, yeryüzünden yayılan ısıyı hapseder ve böylece atmosferde sıcaklık artışına neden olur."
        elif kayit == "atıklar küresel ısınmayı ne şekilde tetikler":
            gibi="Çürümeye bırakılan meyveler metan gazı salgılar, kimyasal atıklar toprağa karışıp çevreyi kirletir ve bu şekilde küresel ısınma tetiklenmye ve sıcaklıklar artmaya devam eder. "
    except:
        gibi = ""
        kayit= "bir hata oluştu" 
    return render_template('index.html', kayit=kayit,
                                        gibi=gibi)

    
    

                                    
    
    
    

    

if __name__ == "__main__":
    app.run(debug=True)
