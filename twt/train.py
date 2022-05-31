import pickle
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
    

filename = 'model.sav'

def train():
    data = dict()
    data["fake"]  = pd.read_csv("C:/Users/ASUS/Desktop/projects/twitter/twt/dataset/fusers.csv")
    data["legit"] = pd.read_csv("C:/Users/ASUS/Desktop/projects/twitter/twt/dataset/users.csv")

    data["legit"] = data["legit"].drop(["id", "name", "screen_name", "created_at", "lang", "location", "default_profile", "default_profile_image", "geo_enabled", "profile_image_url", "profile_banner_url", "profile_use_background_image", "profile_background_image_url_https", "profile_text_color", "profile_image_url_https", "profile_sidebar_border_color", "profile_background_tile", "profile_sidebar_fill_color", "profile_background_image_url", "profile_background_color", "profile_link_color", "utc_offset", "protected", "verified", "dataset", "updated", "description"], axis=1)
    data["fake"]  = data["fake"].drop(["id", "name", "screen_name", "created_at", "lang", "location", "default_profile", "default_profile_image", "geo_enabled", "profile_image_url", "profile_banner_url", "profile_use_background_image", "profile_background_image_url_https", "profile_text_color", "profile_image_url_https", "profile_sidebar_border_color", "profile_background_tile", "profile_sidebar_fill_color", "profile_background_image_url", "profile_background_color", "profile_link_color", "utc_offset", "protected", "verified", "dataset", "updated", "description"], axis=1)

    data['legit']['y']=1
    data['fake']['y']=0

    frames=[data['fake'],data['legit']]
    data=pd.concat(frames)

    data=data.drop(['url','time_zone'],axis=1)

    X = data.drop(['y'],axis=1)
    Y = data['y']

    X_train, X_test, y_train, y_test = train_test_split( X, Y, 
        test_size=0.24, random_state=42)


    model=LogisticRegression(max_iter=1000,random_state=1)
    model.fit(X_train,y_train)

    y_pred=model.predict(X_test)

    print("Accuracy:",round(model.score(X_train, y_train)*100,2))

    pickle.dump(model, open(filename, 'wb'))
    print("model saved...")

if __name__=='__main__':

    train()