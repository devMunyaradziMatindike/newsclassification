import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from joblib import load
import json

class model:


    def get_data(self):

        # Load the news dataset
        data = pd.read_json('News_Category_Dataset_v3.json',lines=True)

        kmeans = load("kmeans_model.joblib")

        vectorizer = TfidfVectorizer(stop_words='english')
        X = vectorizer.fit_transform(data['category'])
        # Use the KMeans model to make predictions on the new data
        y_pred = kmeans.predict(X)

        data['cluster'] = kmeans.labels_

        list_ = [['Political News',1,"Politics.html"], ['Sport',2,"Sports.html"] ,['Technology',3,"Tech.html"], ['Crime',4,"Crime.html"], ['Entertainment',5,"entertainment.html"]]

        # list_ = [['COMEDY',1,"Comedy.html"],['TECH',2,"Tech.html"],
        #     ['SPORTS',3,"Sports.html"], ['ENTERTAINMENT',4,"entertainment.html"], ['POLITICS',5,"Politics.html"],
        #         ['CRIME',6,"Crime.html"] ,
        #     ['FOOD & DRINK',7,"Food.html"],
        #     ['TRAVEL',7,"Travel.html"], ['RELIGION',8,"Religion.html"],
        #     ['HEALTHY LIVING',9,"Health.html"]]


        data2 = data.to_dict('dict')
        clust_list = list(data2.get('cluster').values())
        category_list = list(data2.get('category').values())
        link_list = list(data2.get('link').values())
    
     
        info = [[_clust,_link,_cat]for _clust,_link,_cat in zip(clust_list,link_list,category_list)]
 
        return list_



    def get_comedy(self):

        # Load the news dataset
        data = pd.read_json('News_Category_Dataset_v3.json',lines=True)

        kmeans = load("kmeans_model.joblib")

        vectorizer = TfidfVectorizer(stop_words='english')
        X = vectorizer.fit_transform(data['category'])
        # Use the KMeans model to make predictions on the new data
        y_pred = kmeans.predict(X)

        data['cluster'] = kmeans.labels_

        data2 = data.to_dict('dict')
        clust_list = list(data2.get('cluster').values())
        category_list = list(data2.get('category').values())
        link_list = list(data2.get('link').values())

        info = [[_clust,_link,_cat]for _clust,_link,_cat in zip(clust_list,link_list,category_list)]

        info2 =  [item for item in info if item[2] == 'COMEDY'][:15]
        return info2


    def get_tech(self):

        # Load the news dataset
        data = pd.read_json('News_Category_Dataset_v3.json',lines=True)

        kmeans = load("kmeans_model.joblib")

        vectorizer = TfidfVectorizer(stop_words='english')
        X = vectorizer.fit_transform(data['category'])
        # Use the KMeans model to make predictions on the new data
        y_pred = kmeans.predict(X)

        data['cluster'] = kmeans.labels_

        data2 = data.to_dict('dict')
        clust_list = list(data2.get('cluster').values())
        category_list = list(data2.get('category').values())
        link_list = list(data2.get('link').values())

        info = [[_clust,_link,_cat]for _clust,_link,_cat in zip(clust_list,link_list,category_list)]

        info2 =  [item for item in info if item[2] == 'TECH'][:15]
        return info2

        
    def get_crime(self):

        # Load the news dataset
        data = pd.read_json('News_Category_Dataset_v3.json',lines=True)

        kmeans = load("kmeans_model.joblib")

        vectorizer = TfidfVectorizer(stop_words='english')
        X = vectorizer.fit_transform(data['category'])
        # Use the KMeans model to make predictions on the new data
        y_pred = kmeans.predict(X)

        data['cluster'] = kmeans.labels_

        data2 = data.to_dict('dict')
        clust_list = list(data2.get('cluster').values())
        category_list = list(data2.get('category').values())
        link_list = list(data2.get('link').values())

        info = [[_clust,_link,_cat]for _clust,_link,_cat in zip(clust_list,link_list,category_list)]

        info2 =  [item for item in info if item[2] == 'CRIME'][:15]
        return info2


        
    def get_entertainment(self):

        # Load the news dataset
        data = pd.read_json('News_Category_Dataset_v3.json',lines=True)

        kmeans = load("kmeans_model.joblib")

        vectorizer = TfidfVectorizer(stop_words='english')
        X = vectorizer.fit_transform(data['category'])
        # Use the KMeans model to make predictions on the new data
        y_pred = kmeans.predict(X)

        data['cluster'] = kmeans.labels_

        data2 = data.to_dict('dict')
        clust_list = list(data2.get('cluster').values())
        category_list = list(data2.get('category').values())
        link_list = list(data2.get('link').values())

        info = [[_clust,_link,_cat]for _clust,_link,_cat in zip(clust_list,link_list,category_list)]

        info2 =  [item for item in info if item[2] == 'ENTERTAINMENT'][:15]
        return info2

          
    def get_food(self):

        # Load the news dataset
        data = pd.read_json('News_Category_Dataset_v3.json',lines=True)

        kmeans = load("kmeans_model.joblib")

        vectorizer = TfidfVectorizer(stop_words='english')
        X = vectorizer.fit_transform(data['category'])
        # Use the KMeans model to make predictions on the new data
        y_pred = kmeans.predict(X)

        data['cluster'] = kmeans.labels_

        data2 = data.to_dict('dict')
        clust_list = list(data2.get('cluster').values())
        category_list = list(data2.get('category').values())
        link_list = list(data2.get('link').values())

        info = [[_clust,_link,_cat]for _clust,_link,_cat in zip(clust_list,link_list,category_list)]

        info2 =  [item for item in info if item[2] == 'FOOD & DRINK'][:15]
        return info2


        
    def get_health(self):

        # Load the news dataset
        data = pd.read_json('News_Category_Dataset_v3.json',lines=True)

        kmeans = load("kmeans_model.joblib")

        vectorizer = TfidfVectorizer(stop_words='english')
        X = vectorizer.fit_transform(data['category'])
        # Use the KMeans model to make predictions on the new data
        y_pred = kmeans.predict(X)

        data['cluster'] = kmeans.labels_

        data2 = data.to_dict('dict')
        clust_list = list(data2.get('cluster').values())
        category_list = list(data2.get('category').values())
        link_list = list(data2.get('link').values())

        info = [[_clust,_link,_cat]for _clust,_link,_cat in zip(clust_list,link_list,category_list)]

        info2 =  [item for item in info if item[2] == 'HEALTHY LIVING'][:15]
        return info2


        
    def get_politics(self):

        # Load the news dataset
        data = pd.read_json('News_Category_Dataset_v3.json',lines=True)

        kmeans = load("kmeans_model.joblib")

        vectorizer = TfidfVectorizer(stop_words='english')
        X = vectorizer.fit_transform(data['category'])
        # Use the KMeans model to make predictions on the new data
        y_pred = kmeans.predict(X)

        data['cluster'] = kmeans.labels_

        data2 = data.to_dict('dict')
        clust_list = list(data2.get('cluster').values())
        category_list = list(data2.get('category').values())
        link_list = list(data2.get('link').values())

        info = [[_clust,_link,_cat]for _clust,_link,_cat in zip(clust_list,link_list,category_list)]

        info2 =  [item for item in info if item[2] == 'POLITICS'][:15]
        return info2


    def get_religion(self):
    
        # Load the news dataset
        data = pd.read_json('News_Category_Dataset_v3.json',lines=True)

        kmeans = load("kmeans_model.joblib")

        vectorizer = TfidfVectorizer(stop_words='english')
        X = vectorizer.fit_transform(data['category'])
        # Use the KMeans model to make predictions on the new data
        y_pred = kmeans.predict(X)

        data['cluster'] = kmeans.labels_

        data2 = data.to_dict('dict')
        clust_list = list(data2.get('cluster').values())
        category_list = list(data2.get('category').values())
        link_list = list(data2.get('link').values())

        info = [[_clust,_link,_cat]for _clust,_link,_cat in zip(clust_list,link_list,category_list)]

        info2 =  [item for item in info if item[2] == 'RELIGION'][:15]
        return info2


        
    def get_sports(self):
    
        # Load the news dataset
        data = pd.read_json('News_Category_Dataset_v3.json',lines=True)

        kmeans = load("kmeans_model.joblib")

        vectorizer = TfidfVectorizer(stop_words='english')
        X = vectorizer.fit_transform(data['category'])
        # Use the KMeans model to make predictions on the new data
        y_pred = kmeans.predict(X)

        data['cluster'] = kmeans.labels_

        data2 = data.to_dict('dict')
        clust_list = list(data2.get('cluster').values())
        category_list = list(data2.get('category').values())
        link_list = list(data2.get('link').values())

        info = [[_clust,_link,_cat]for _clust,_link,_cat in zip(clust_list,link_list,category_list)]

        info2 =  [item for item in info if item[2] == 'SPORTS'][:15]
        return info2


    def get_travel(self):
        
        # Load the news dataset
        data = pd.read_json('News_Category_Dataset_v3.json',lines=True)

        kmeans = load("kmeans_model.joblib")

        vectorizer = TfidfVectorizer(stop_words='english')
        X = vectorizer.fit_transform(data['category'])
        # Use the KMeans model to make predictions on the new data
        y_pred = kmeans.predict(X)

        data['cluster'] = kmeans.labels_

        data2 = data.to_dict('dict')
        clust_list = list(data2.get('cluster').values())
        category_list = list(data2.get('category').values())
        link_list = list(data2.get('link').values())

        info = [[_clust,_link,_cat]for _clust,_link,_cat in zip(clust_list,link_list,category_list)]

        info2 =  [item for item in info if item[2] == 'TRAVEL'][:15]
        return info2