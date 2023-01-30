
import pymongo
import pandas as pd
import json
# Provide the mongodb localhost url to connect python to mongodb.
client = pymongo.MongoClient("mongodb://localhost:27017/neurolabDB")

DATABASE_NAME="aps"
COLLECTION_NAME="sensor"
DATA_PATH="/config/workspace/aps_failure_training_set1.csv"


if __name__ =="__main__":
    data=pd.read_csv(DATA_PATH)
data.head(4)
data.info()
data.tail()
print(f"rows & colummns :{data.shape}")


#convert Dataframe to Json format so that  we can dump dataset into mongodb
data.reset_index(inplace=True,drop=True)
json_record=list(json.loads(data.T.to_json()).values())
print(json_record[0])

#insert converted json into mongodb
client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)

