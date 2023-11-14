from flask import Flask, request, render_template

app = Flask("__name__")


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        string = request.form['string']
        with open("lines_3.txt", "a") as file:
            file.write(string + '\n')
    return render_template('index.html')

@app.route('/file')
def fileoutput():
    with open("lines_3.txt", 'r') as f:
        content = f.readlines()
    return render_template("fileoutput.html", content=content)


if __name__ == '__main__':
    app.run()