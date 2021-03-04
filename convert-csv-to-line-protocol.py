import pandas as pd
#convert csv to line protocol;

#convert sample data to line protocol (with nanosecond precision)
df = pd.read_csv("data/integration-spike.csv")
lines = ["elapsed=" + str(df["elapsed"][d]) 
         + ",label=" + str(df["label"][d]) 
         + ",responseCode=" + str(df["responseCode"][d]) 
         + ",responseMessage=" + str(df["responseMessage"][d]) 
         + ",threadName=" + str(df["threadName"][d]) 
         + ",dataType=" + str(df["dataType"][d]) 
         + ",success=" + str(df["success"][d]) 
         + ",failureMessage=" + str(df["failureMessage"][d]) 
         + ",bytes=" + str(df["bytes"][d])
         + ",sentBytes=" + str(df["sentBytes"][d])   
         + ",grpThreads=" + str(df["grpThreads"][d])    
         + ",allThreads=" + str(df["allThreads"][d])    
         + ",URL=" + df["URL"]
         + ",Latency=" + str(df["Latency"][d])    
         + ",IdleTime=" + str(df["IdleTime"][d])  
         + " " + str(df["timeStamp"][d]) for d in range(len(df))]
thefile = open('data/chronograf.txt', 'w')
for item in lines:
    thefile.write("%s\n" % item)
