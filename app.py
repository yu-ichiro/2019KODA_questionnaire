import json
from datetime import datetime

from flask import Flask, request, render_template, jsonify, session
import os
import hashlib

app = Flask(__name__)
app.secret_key = 'unplugged'


@app.route('/', methods=['GET', 'POST'])
def questionnaire():
    if session.get('id', None) is None:
        session['id'] = hashlib.sha512(str(datetime.now()).encode()).digest().hex()[:64]
    songs = [
        ("季節は次々死んでいく / amazarashi", True),
        ("----", False),
        ("ドキドキ(しちゃうね) / ムノーノ = モーゼス", True),
        ("さよならリグレット / くるり", True),
        ("風になる / つじあやの", True),
        ("----", False),
        ("美しく燃える森 / 東京スカパラダイスオーケストラ", True),
        ("新しい歌 / 秦基博", False),
        ("君の話 / スキマスイッチ", True),
        ("----", False),
        ("恋する / SHISHAMO", True),
        ("傘 / 宗藤竜太", True),
        ("Junior Sweet / Chara", True),
        ("----", False),
        ("Alice / Avril Lavigne", True),
        ("光 / 宇多田ヒカル", True),
        ("中央フリーウェイ / 荒井由実", True),
        ("----", False),
        ("コイワズライ / Aimer", True),
        ("遠視のコントラルト / 君島大空", True),
        ("丸の内サディスティック / 椎名林檎", True),
        ("----", False),
        ("Trailer / Official髭男dism", True),
        ("キャラバン / 小田桐仁儀", False),
        ("初恋 / 村下孝蔵", True),
        ("----", False),
        ("Charm / WANIMA", True),
        ("青い栞 / Galileo Galilei", True),
        ("爽健美茶のラップ / Chelmico", False),
        ("----", False),
        ("Summer Gate / 佐藤千亜紀", True),
        ("雨 / ペトロールズ", True),
        ("LOOP / SIRUP", True),
        ("----", False),
        ("白日 / King Gnu", True),
        ("ワンモアタイム / 斉藤和義", True),
        ("楓 / スピッツ", True),
        ("----", False),
        ("東へ西へ／井上陽水", True),
        ("たらればわたがし / Unison Square Garden", True),
    ]
    if request.method == 'GET':
        return render_template('index.html', songs=json.dumps(songs))
    if request.method == 'POST':
        try:
            votes = [
                {
                    'id': _id,
                    'name': songs[int(_id)][0],
                    'reason': request.form.get('reason_' + _id, ''),
                    'vote_num': 2 if request.form.get('second_vote', None) == _id else 1
                }
                for _id in request.form.getlist('first_vote')
            ]
            file_path = 'votes/vote_{}.json'.format(session['id'])
            if os.path.exists(file_path):
                return jsonify({'status': 'error', 'errors': ['投票済みです']})
            with open(file_path, 'w') as fp:
                for vote in votes:
                    json.dump(vote, fp, ensure_ascii=False)
                    fp.write('\n')
            return jsonify({'status': 'success'})
        except Exception as e:
            print(e)
            return jsonify({'status': 'error', 'errors': ['サーバーでエラーが発生しました。スミスを殴ってください。']})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
