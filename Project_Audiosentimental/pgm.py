import os
import pickle
import warnings
import numpy as np
import keras
import numpy as np
import librosa
from FeaturesExtractor import FeaturesExtractor

warnings.filterwarnings("ignore")

def gender(file):
    f=m=0
    features_extractor    = FeaturesExtractor()
    model = pickle.load(open('model.pkl', 'rb'))
    #files = ['test_m.wav']
    #for file in files:
    vector = features_extractor.extract_features(file)
    #print(len(vector))
    pred  = model.predict(vector)      
    for i in pred:
        if i == 0:
            f+=1
        elif i == 1:
            m+=1
    if m>f:
        print('{} is a male'.format(file))
    else:
        print('{} is a female'.format(file))

def makepredictions(file):
    '''
    process the files and create features.
    '''
    data, sampling_rate = librosa.load(file)
    mfccs = np.mean(librosa.feature.mfcc(y=data, sr=sampling_rate, n_mfcc=40).T, axis=0)
    x = np.expand_dims(mfccs, axis=1)
    x = np.expand_dims(x, axis=0)
    predictions = loaded_model.predict_classes(x)
    #print( "Prediction is", " ",convertclasstoemotion(predictions))
    return convertclasstoemotion(predictions)

def convertclasstoemotion(pred):
    '''
    convert the predictions (int) into human readable strings.
    '''
    if pred == 0:
        pred = "neutral"
        return pred
    elif pred == 1:
        pred = "calm"
        return pred
    elif pred == 2:
        pred = "happy"
        return pred
    elif pred == 3:
        pred = "sad"
        return pred
    elif pred == 4:
        pred = "angry"
        return pred
    elif pred == 5:
        pred = "fearful"
        return pred
    elif pred == 6:
        pred = "disgust"
        return pred
    elif pred == 7:
        pred = "surprised"
        return pred

loaded_model = keras.models.load_model('Emotion_Voice_Detection_Model.h5')
f=open('testFile.txt','r')
audio_file=f.read()
f.close()
//audio_file = 'fear.wav'
gender(audio_file)
emotion = makepredictions(audio_file)
print('Emotion is: ',emotion)
if emotion in ['neutral']:
	print('Attitude is: Neutral')
elif emotion in ['happy','calm','surprised']:
	print('Attitude is: Positive')
elif emotion in ['sad','disgust','fearful','angry']:
	print('Attitude is: Negative')