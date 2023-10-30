from flask import Flask, request, jsonify
from Music_Reccommend_Function import Reccommendation

app = Flask('test')

@app.route('/recommend', methods=['POST'])
def recommend():
    data = request.get_json()
    artist1 = data['album1']
    artist2 = data['album1']
    album1 = data['album1']
    album2 = data['album2']
    recommendation = Reccommendation(artist1,album1,artist2,album2)
    return jsonify({'recommendation': recommendation})

if __name__ == '__main__':
    app.run()
