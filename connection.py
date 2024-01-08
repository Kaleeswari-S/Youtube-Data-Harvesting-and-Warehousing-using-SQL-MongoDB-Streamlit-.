#API key connection
def Api_connect():
    Api_Id="AIzaSyAX2gy1qjfm3sz1YEwYBnPgp_sAyZ0zyKc"

    api_service_name = "youtube"
    api_version = "v3"
    youtube = build(api_service_name,api_version,developerKey=Api_Id)
    return youtube

youtube=Api_connect()


#Pyhton Programmer : "UC68KSmHePPePCjW4v57VPQg" 
#Learn Tech : "UCzNFj4KZTV72DsrGoDquVQQ" 
#Data Nash : "UCRqCK8izkO5xeVVtMKSHeRQ" 
#Joma Tech : "UCV0qA-eDDICsRR9rPcnG7tw" 
#Alex The Analyst : "UC7cs8q-gJRlGwj4A8OmCmXg" 
#StatQuest with Josh Starmer : "UCtYLUTtgS3k1Fg4y5tAhLbw" 
#3Blue1Brown : "UCYO_jab_esuFRV4b17AJtAw" 
#Ken Jee : "UCiT9RITQ9PW6BhXK0y2jaeg" 
#Data Shool : "UCnVzApLJE2ljPZSeQylSEyg" 
#365 Data Science : "UCEBpSZhI1X8WaP-kY_2LLcg"


#MongoDB connection
client = pymongo.MongoClient("mongodb+srv://kaleeswariramkumar25:ram@kaleeswari24.stlokdg.mongodb.net/?retryWrites=true&w=majority")
dbase = client['Capstone_Project-1']


#SQL Connection
mydb = psycopg2.connect(host="localhost",
                    user="postgres",
                    password="ram7",
                    database= "project1_youtube",
                    port = "5432"
                    )
cursor = mydb.cursor()
