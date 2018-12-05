
REST Services with Eve - Capture the local machine details 

-   Install eve on machine

```$ pip install eve```
    
-   Download the REST git repo on your local machine
    
-   Verify the settings.py and run.py available in eve folder
    
-   Execute python run.py

## Execute the below Commands to verify the outputs
#Run the below URL to View the System details - 

http://127.0.0.1:5000/ubuntu/ram

![Alt](/REST/RAMScreenshotURL.png)

http://127.0.0.1:5000/ubuntu/processorName

![Alt](/REST/ProcessorSystemScreenshotURL.png)

http://127.0.0.1:5000/ubuntu/diskspace

![Alt](/REST/DiskScreenshotURL.png)

http://127.0.0.1:5000/ubuntu/CPUDetails

![Alt](/REST/CPUScreenshotURL.png)

#Using CURL 
curl -H "Content-Type: application/json" http://127.0.0.1:5000/ubuntu/ram/

curl -H "Content-Type: application/json" http://127.0.0.1:5000/ubuntu/processorName

curl -H "Content-Type: application/json" http://127.0.0.1:5000/ubuntu/diskspace

curl -H "Content-Type: application/json" http://127.0.0.1:5000/ubuntu/CPUDetails

Screenshot for all the above curl statement outputs -


![Alt](/REST/CURLStatementsScreenshot.png)
