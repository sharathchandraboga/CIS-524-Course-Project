from flask import Flask,render_template,request
from datetime import datetime

app = Flask(__name__)
app.config["DEBUG"] = True


result = []
@app.route('/hello')
def hello_world():
    return 'Hello from Flask!'
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/click",methods=["GET","POST"])
def read():
    if request.method == "POST":
        filename="/static/abc.txt"
        f1= open(filename,'r')
        a=f1.read()
        a=a.lower()
        fmt="%I:%M:%p"
        totalmins=0;
        dele=a.find("time log:");
        if dele!=-1:
            a=a[dele+len("time log:"):]
            index=a.find('-')
            a1=a;
        while (index!=-1):
            if a1[index+1]==' ':
                a1=a1[:index-1]+"&"+a1[index+2:];
            elif a1[index-1]==' ':
                a1=a1[:index-2]+"&"+a1[index+1:]
            else:
                a1=a1[:index-1]+"&"+a1[index+1:];
                index=a1.find("&",index-2,index+2);
                time1=a1.rfind(" ",0,index);
                time1=a1[time1+1:index];
                time2=a1.find("m",index,index+20);
                time2=a1[index+1:time2+1];
            time1=time1[:len(time1)-2]+":"+time1[len(time1)-2:]
            time2=time2[:len(time2)-2]+":"+time2[len(time2)-2:]
            try:
                time1=datetime.strptime(time1,fmt)
                time2=datetime.strptime(time2,fmt)
                totalmins=totalmins+(time2-time1).seconds/60
            except:
                index=a1.find('-')
                continue;
            index=a1.find('-')
            x = int(totalmins//60)
            y = int(totalmins%60)

            result.append(x)
            result.append(y)
        return render_template("result.html",result)
        #print("Total Time is:",int(totalmins//60),"hrs", int(totalmins%60),"mins")
