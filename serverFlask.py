from flask import Flask, render_template, request
import exifReader as er
import datetime
app = Flask(__name__)
#app._static_folder = "templates/"




@app.route("/")
def index():
    return render_template('index.html')
#    return render_template('index.html',image_path="")




@app.route('/hist', methods=['POST', 'GET'])
def hist():
    im_name = "static/img/plots/t" + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + ".png"
    text = request.args.get("photo_path")
    if text:
        im_amount = ""
        im_amount= er.get_exif_info(text,im_name)
        print im_amount
        #result_ = "result for " + im_amount + " images"
        #print result_
        if im_amount > 0:
            im_path = "../" + im_name
            return render_template('index.html',result=im_amount,image_path=im_path)
        elif im_amount == 0:
            return render_template('index.html',result="no images found")
        else:
            return render_template('index.html',result="invalid path")

    else:
            return render_template('index.html',result="enter a path")

if __name__ == "__main__":
    app.run()

