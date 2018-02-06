from eve import Eve
import sys
import json
import random
import requests
import platform
import psutil
from flask import jsonify

app = Eve()

# To Get Virtual Memory
@app.route('/ubuntu/ram', methods=['GET'])
def ram():
    ramdata = {
            "Total Virtual Memory": str(psutil.virtual_memory().total) + " Bytes",
            "Used Virtual Memory": str(psutil.virtual_memory().used)+ " Bytes",
            "Free Virtual Memory": str(psutil.virtual_memory().free)+ " Bytes"
            }
    return (jsonify(ramdata))

# To Get Processor and System Details
@app.route('/ubuntu/processorName', methods=['GET'])
def processor():
    processordata = {
            "ProcessorName": platform.processor(),
            "ProcessorVersion": platform.version(),
            "System": platform.system()
            }
    return (jsonify(processordata))

# To Get Disk details
@app.route("/ubuntu/diskspace", methods=['GET'])
def Diskdetail():
    Diskdata = {
		"Total Disk": str(psutil.disk_usage('/').total)+ " Bytes",
            	"Used Disk": str(psutil.disk_usage('/').used)+ " Bytes",
            	"Free Disk": str(psutil.disk_usage('/').free)+ " Bytes"	
            }
    return(jsonify(Diskdata))

# To Get CPU details
@app.route("/ubuntu/CPUDetails", methods=['GET'])
def CPUdetail():
    CPUdata = {
            "CPU Count": psutil.cpu_count(),
	    "Terminal": psutil.users()[0].terminal	
            }
    return(jsonify(CPUdata))


if __name__=='__main__':
    app.run()
    
    


