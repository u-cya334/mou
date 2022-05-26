from flask import Flask
from flask import render_template
import youtube


app = Flask(__name__)
if __name__ == "__main__":
    app.run(debug=True)

videos_list = []

@app.route("/")
def hello():
    global videos_list
    channel_list = ["UChJ5FTsHOu72_5OVx0rvsvQ","UCckdfYDGrjojJM28n5SHYrA","UCP4nMSTdwU1KqYWu3UH5DHQ","UCG0rzBZV_QMP4MtWg6IjhEA","UCGhqxhovNfaPBpxfCruy9EA"]
    videos_list = youtube.return_videos(channel_list)[0]
    print(videos_list)
    maxResult = range(youtube.return_videos(channel_list)[2])
    no = range(len(channel_list))
    return render_template("home.html",videos_list = videos_list,maxResult = maxResult, no = no)


# routeの中の<id>のidを引数と使える
@app.route("/videos/<id>/<title>")
def videos(id,title):
    global videos_list
    return render_template("videos.html",id = id,title = title,videos_list = videos_list)


@app.route("/test")
def test():
    return render_template('test.html')


@app.route('/sw.js', methods=['GET'])
def sw():
    return app.send_static_file('sw.js')


