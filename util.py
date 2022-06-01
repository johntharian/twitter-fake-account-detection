import datetime
import numpy as np
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense,Activation
from pickle import load


def process(data):

    age=[]
    now=datetime.date.today()

    for i in data['created_at']:
        d=datetime.date(i.year,i.month,i.day)
        delta=now-d
        age.append(delta.days)

    data['age']=age

    data['fr_c_by_fo_c']=data['friends_count']/data['followers_count']

    data['active']=data['statuses_count']/data['age']

    data=data.drop(["created_at"],axis=1)

    data.replace([np.inf,-np.inf],0,inplace=True)

    scaler = load(open('scaler.pkl', 'rb'))
    data = scaler.transform(data)

    return data


def create_model():
    model = Sequential([
    Dense(10, activation='relu', input_shape=(8,)),
    Dense(32,activation='relu'),
    Dense(32, activation='relu'),
    Dense(1, activation='sigmoid'),
    ])  

    model.compile(optimizer='sgd',
              loss='binary_crossentropy',
              metrics=['accuracy'])

    # print(model.weights)
    return model


def predict(data):
    model=create_model()
    model.load_weights('weights')
    
    pred=model.predict(data)
    p=[]
    for i in pred:
        if i <0.5:
            p.append(1)
        else:
            p.append(0)

    return p[0]


