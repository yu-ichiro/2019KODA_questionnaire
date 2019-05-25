import json

from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def questionnaire():
    songs = [
        ("季節は次々死んでいく / amazarashi", True),
        ("ドキドキ(しちゃうね) / ムノーノ = モーゼス", True),
        ("さよならリグレット / くるり", True),
        ("風になる / つじあやの", True),
        ("美しく燃える森 / 東京スカパラダイスオーケストラ", True),
        ("新しい歌 / 秦基博", False),
        ("君の話 / スキマスイッチ", True),
        ("恋する / SHISHAMO", True),
        ("傘 / 宗藤竜太", True),
        ("Junior Sweet / Chara", True),
        ("Alice / Avril Lavigne", True),
        ("光 / 宇多田ヒカル", True),
        ("中央フリーウェイ / 荒井由実", True),
        ("コイワズライ / Aimer", True),
        ("遠視のコントラルト / 君島大空", True),
        ("丸の内サディスティック / 椎名林檎", True),
        ("Trailer / Official髭男dism", True),
        ("キャラバン / 小田桐仁儀", False),
        ("初恋 / 村下孝蔵", True),
        ("Charm / WANIMA", True),
        ("青い栞 / Galileo Galilei", True),
        ("爽健美茶のラップ / Chelmico", False),
        ("Summer Gate / 佐藤千亜紀", True),
        ("雨 / ペトロールズ", True),
        ("LOOP / SIRUP", True),
        ("白日 / King Gnu", True),
        ("ワンモアタイム / 斉藤和義", True),
        ("楓 / スピッツ", True),
        ("東へ西へ／井上陽水", True),
        ("たらればわたがし / Unison Square Garden", True),

    ]
    if request.method == 'GET':
        return render_template('index.html', songs=json.dumps(songs))
    if request.method == 'POST':
        pass


if __name__ == '__main__':
    app.run(debug=True)
