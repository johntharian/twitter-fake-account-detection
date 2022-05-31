from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense,Activation
import datetime
import numpy as np

def get_input():
    account=[]

    account.append(input("enter name"))

    return account

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

# data['active']=data['active']*1000

# data['active']=data['active'].astype(int)

# data['fr_c_by_fo_c']=data['fr_c_by_fo_c']*1000

# data['fr_c_by_fo_c']=data['fr_c_by_fo_c'].astype(int)


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

    return pred


