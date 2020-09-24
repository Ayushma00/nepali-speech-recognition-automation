from django.shortcuts import render
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session,sessionmaker
from django.http import HttpResponse
import numpy as np
import librosa
from pathlib import Path
import os
import pickle
from sklearn.preprocessing import MinMaxScaler
from keras.models import load_model
BASE_DIR=os.path.dirname(os.path.realpath(__file__))
text1=''
engine = create_engine("postgres://vrxmsncxrvcjor:1594c4b320f5dc33ef59ed2b04d5746ff36ed630591f77c38a8a9dcd21d5b400@ec2-34-232-212-164.compute-1.amazonaws.com:5432/dstmff6bkopfn")
db=scoped_session(sessionmaker(bind=engine))
# Create your views here.
ms = MinMaxScaler()
model1 = load_model(os.path.join(BASE_DIR,"open_close.h5"))
ohe1 = pickle.load(open(os.path.join(BASE_DIR,'ohe_open_close.pkl'),'rb'))
# Create your views here.
count=1
c=1
def main(request):
    global text1
    return render(request,"mainapp/index.html",{'text':text1})

def download(request):
    global text1
    global count
    global c
    if request.method=="POST":
        blob=request.body
        make_wav(blob)
        y, sr = librosa.load(Path('./file'+str(count)+'.wav'),sr=44100, mono = True, offset = 0.0, duration= None)
        count+=1
        text1=speechtotext(y,sr)
        datas=db.execute("SELECT * FROM sound")
        for data in datas:
            save_wav(data.speech)
        c+=1
        db.execute("INSERT INTO sound (speech, text) VALUES (:speech, :text)", {
                   'speech': blob, 'text': text1})
        db.commit()
        return HttpResponse("good")

def speechtotext(y,sr):
    n_fft=2048

    # Step or stride between windows. If the step is smaller than the window lenght, the windows will overlap
    hop_length=512
    spectrogram_librosa = np.abs(librosa.stft(
    y, n_fft=n_fft, hop_length=hop_length, win_length=n_fft, window='hann')) ** 2
    arr = np.zeros((1025,175))
    arr = arr + 1e-9
    if(spectrogram_librosa.shape[1]>=175):
        spectrogram_librosa= spectrogram_librosa[:,:175]
    arr[:,:spectrogram_librosa.shape[1]] = spectrogram_librosa
    spectrogram_librosa_db = librosa.amplitude_to_db(arr, ref=np.max)
    arr1 = np.transpose(spectrogram_librosa_db)
    sample = ms.fit_transform(arr1)
    sample=sample.reshape(1,175,1025)   # model1=175, model2=90
    pred=model1.predict(sample)
    pred = pred == pred.max()
    pred=ohe1.inverse_transform(np.round(pred))
    return pred[0][0]
def make_wav(blobs):
    global count
    f = open('./file'+str(count)+'.wav', 'wb')

    f.write(blobs)
    f.close()
def save_wav(blobs):
    global c
    f = open('./file'+str(c)+'.wav', 'wb')
    f.write(blobs)
    f.close()
