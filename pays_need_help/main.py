class help():
    #clean the data and make prediction
    def result(path):
        lb = LabelEncoder()
        #import the dataset
        data = pd.read_csv(path)
        #drop columns that are not worthed
        df = data.drop(columns = ['Net migration','Infant mortality (per 1000 births)','Phones (per 1000)','Arable (%)','Crops (%)','Other (%)','Birthrate','Deathrate','Agriculture','Industry','Service','Literacy (%)','Climate'])
        country = df['Country']
        region = df['Region']
        #we drop this columns because we will transfer all the columns from categorical type to numeric type
        df.drop(columns = ['Country','Region'] , inplace = True)
        #transform all the categorical columns to numerical columns
        for col in df.select_dtypes('object'):
            df[col] = lb.fit_transform(df[col])
        #fill all the nan column
        df = df.fillna(0)
        #prepare the model
        kmeans = KMeans(init="random",n_clusters=2,n_init=10,max_iter=300,random_state=42)
        #fit the model
        kmeans.fit(df[['GDP ($ per capita)']])
        #add the prediction to the dataset
        df['country'] = country
        df['region'] = region
        df['predict'] = kmeans.labels_
        country_can_help = df.loc[df['predict']==1]['country']
        country_cannot_help = df.loc[df['predict']==0]['country']
        country_can_help.to_csv('/home/aziz/Documents/pays_need_help/country_can_help.csv')
        country_cannot_help.to_csv('/home/aziz/Documents/pays_need_help/country_cannot_help.csv')
    #search if the given country need help or no 
    def prediction(self):
        c_c_h = pd.read_csv('/home/aziz/Documents/pays_need_help/country_can_help.csv')
        cch = []
        for i in c_c_h['country']:
            cch.append(i)
        b = False
        for i in cch:
            if(self.country==i):
                print(self.country ,"doesn't need help")
                b = True
        if b == False:
            c_cn_h = pd.read_csv('/home/aziz/Documents/pays_need_help/country_cannot_help.csv')
            cch = []
            for i in c_cn_h['country']:
                cch.append(i)
            b = False
            for i in cch:
                if(self.country==i):
                    print(self.country ,"need help")
    def __init__(self):
        # seaching for the country's name you want
        self.country = input("give me the name of the country you searching for : ")
        self.country = self.country + ' '
if __name__=='__main__':
    #import the necessary libraries
    import pandas as pd
    from sklearn.preprocessing import LabelEncoder
    from sklearn.cluster import KMeans

    b = input('Do you want to update your Dataset :')
    if(b == 'yes'):
        path = input('give me the path of your directory dataset : ')
        #countries of the world(GDP).csv
        help.result(path)
        help().prediction()
    else:
        help().prediction()
