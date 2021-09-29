from flask import render_template,Flask,request
import sys
from smtplib import SMTP
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)

@app.route("/") # ➀の処理
def search():
    return render_template("page1.html")
@app.route("/No")
def No():
    return render_template("page1_No.html")
@app.route("/Yes")
def Yes():
    return render_template("page2.html")

@app.route("/ready")
def ready():
    return render_template("page3.html")
cnt = 3
@app.route("/Q1_no")

def Q1_no():
    global cnt   
    cnt -= 1
    if cnt ==0:
        return render_template("page3_thread.html")
    if cnt <0:
        sys.exit()
        
       
    return render_template("page3_report.html", cnt=cnt)
@app.route("/Q1_yes")
def Q1_yes():
    global cnt
    cnt = 3
    return render_template("page4.html")
@app.route("/Q2_no")
def Q2_no():
    return render_template("page5.html")
@app.route("/message")
def mess():
    return render_template("page6.html")
@app.route("/message_yes")
def mess_yes():
    return render_template("page6_yes.html")
@app.route("/mess_no")
def mess_No():
    return render_template("page7.html")
@app.route("/gmail" , methods = ["POST"])
def gmail():
    gmail = request.form.get("gmail")
    pw = request.form.get("pw")
    text = request.form.get("text")
    print(gmail)
    print(pw)
    print(text)
    atesaki = "batphat98@gmail.com"
    kenmei= "lời nhắn của em"
    honbun= text
    ID = gmail
    PASS = pw
    host = "smtp.gmail.com"
    port = 587
        #instance mime
    msg = MIMEMultipart()
        #HTML setting
    msg.attach(MIMEText(honbun,"html"))
        #件名、送信元アドレス、送信先アドレスを設定
    msg["Subject"] = kenmei
    msg["From"] = ID
    msg["To"] = atesaki 
    server = SMTP(host,port)
    server.starttls()
    server.login(ID,PASS)
    server.send_message(msg)
    server.quit
    return render_template("mail_result.html")

if __name__ == "__main__":
    app.run(debug=True)