from django.shortcuts import render
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session,sessionmaker
from django.http import HttpResponse

engine = create_engine("postgres://vrxmsncxrvcjor:1594c4b320f5dc33ef59ed2b04d5746ff36ed630591f77c38a8a9dcd21d5b400@ec2-34-232-212-164.compute-1.amazonaws.com:5432/dstmff6bkopfn")
db=scoped_session(sessionmaker(bind=engine))


def main(request):
    return render(request,"mainapp/layout.html")

def download(request,text):

    if request.method=="POST":
        blob=request.body
        datas=db.execute("SELECT * FROM sound")
        db.execute("INSERT INTO sound (speech, text) VALUES (:speech, :text)", {
                   'speech': blob, 'text': text})
        db.commit()
        return HttpResponse("good")
