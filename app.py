import json

from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def questionnaire():
    songs = [
        ("光 / 宇多田ヒカル", True),
        ("初恋 / 村下孝蔵", True),
        ("丸の内サディスティック / 椎名林檎", True),
        ("ワンモアタイム / 斉藤和義", True),
        ("Trailer / Official髭男dism", True),
        ("Charm / WANIMA", True),
        ("雨 / ペトロールズ", True),
        ("傘 / 宗藤竜太", True),
        ("爽健美茶のラップ / Chelmico", True),
        ("Junior Sweet / Chara", True),
        ("季節は次々死んでいく / amazarashi", True),
        ("Summer Gate / 佐藤千亜紀", True),
        ("美しく燃える森 / 東京スカパラダイスオーケストラ", True),
        ("恋する / SHISHAMO", True),
        ("君の話 / スキマスイッチ", True),
        ("新しい歌 / 秦基博", True),
        ("白日 / King Gnu", True),
        ("LOOP / SIRUP", True),
        ("ドキドキ(しちゃうね) / ムノーノ = モーゼス", True),
        ("青い栞 / Galileo", True),
        ("Galilei", True),
        ("楓 / スピッツ", True),
        ("Alice / Avril", True),
        ("Lavigne", True),
        ("風になる / つじあやの", True),
        ("たらればわたがし / Unison", True),
        ("Square", True),
        ("Garden", True),
        ("さよならリグレット / くるり", True),
        ("中央フリーウェイ / 荒井由実", True),
        ("遠視のコントラルト / 君島大空", True),
        ("コイワズライ / Aimer", True),
        ("キャラバン / 小田桐仁儀", True),
        ("東へ西へ／井上陽水", True),
    ]
    if request.method == 'GET':
        return render_template('index.html', songs=json.dumps(songs))
    if request.method == 'POST':
        pass


if __name__ == '__main__':
    app.run(debug=True)
