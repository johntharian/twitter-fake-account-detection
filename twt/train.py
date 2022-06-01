import pickle
import pandas as pd
import numpy as np
import dateutil,datetime

from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error as mse
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense,Activation
from pickle import dump

from util import create_model    

filename = 'model.sav'


def train():
    data = dict()
    data["fake"]  = pd.read_csv("C:/Users/ASUS/Desktop/projects/twitter/twt/dataset/fusers.csv")
    data["legit"] = pd.read_csv("C:/Users/ASUS/Desktop/projects/twitter/twt/dataset/users.csv")

    data["legit"] = data["legit"].drop(["id", "name", "screen_name", "lang", "location", "default_profile", "default_profile_image", "geo_enabled", "profile_image_url", "profile_banner_url", "profile_use_background_image", "profile_background_image_url_https", "profile_text_color", "profile_image_url_https", "profile_sidebar_border_color", "profile_background_tile", "profile_sidebar_fill_color", "profile_background_image_url", "profile_background_color", "profile_link_color", "utc_offset", "protected", "verified", "dataset", "updated", "description", 'url', 'time_zone'], axis=1)
    data["fake"]  = data["fake"].drop(["id", "name", "screen_name", "lang", "location", "default_profile", "default_profile_image", "geo_enabled", "profile_image_url", "profile_banner_url", "profile_use_background_image", "profile_background_image_url_https", "profile_text_color", "profile_image_url_https", "profile_sidebar_border_color", "profile_background_tile", "profile_sidebar_fill_color", "profile_background_image_url", "profile_background_color", "profile_link_color", "utc_offset", "protected", "verified", "dataset", "updated", "description", 'url', 'time_zone'], axis=1)

    data['legit']['y']=1
    data['fake']['y']=0

    frames=[data['fake'],data['legit']]
    data=pd.concat(frames)


    age=[]
    now=datetime.date.today()

    for i in data['created_at']:
        #print(i)
        t=datetime.datetime.strptime(i,'%a %b %d %H:%M:%S %z %Y')
        d=datetime.date(t.year,t.month,t.day)
        
        delta=now-d
        #print(delta.days)
        age.append(delta.days)

    data['age']=age

    data['fr_c_by_fo_c']=data['friends_count']/data['followers_count']

    data['active']=data['statuses_count']/data['age']

    data=data.dropna()

    data=data.drop(["created_at"],axis=1)

    data.replace([np.inf,-np.inf],0,inplace=True)

    # data['active']=data['active']*1000

    # data['active']=data['active'].astype(int)

    # data['fr_c_by_fo_c']=data['fr_c_by_fo_c']*1000

    # data['fr_c_by_fo_c']=data['fr_c_by_fo_c'].astype(int)

    X = data.drop(['y'],axis=1)
    Y = data['y']

    X_train, X_test, y_train, y_test = train_test_split( X, Y, test_size=0.3, random_state=42)
    X_train, X_val, y_train, y_val = train_test_split( X_train, y_train, test_size=0.1, random_state=42)

    scaler=MinMaxScaler()

    scaler.fit(X_train)

    X_train=scaler.transform(X_train)
    X_test=scaler.transform(X_test)
    X_val=scaler.transform(X_val)

    dump(scaler, open('scaler.pkl', 'wb'))
    print('scaler saved')
    
    model=create_model()

    hist = model.fit(X_train, y_train,
          batch_size=32, epochs=100,
          validation_data=(X_test, y_test))


    model.evaluate(X_val, y_val)

    y_pred=model.predict(X_val)

    print("Mean Squared Error",mse(y_pred,y_val))

    model.save_weights('weights')
    print("model saved...")


if __name__=='__main__':
    train()
