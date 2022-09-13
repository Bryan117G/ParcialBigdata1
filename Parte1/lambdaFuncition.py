#Bryan Garavito 
import json
import boto3
import datetime
from scraping import lambda_handler1
from PasarArchivoCvs import lambda_handler2

def lambda_handler(event, context):
    #TODO implement
    lambda_handler1()
    lambda_handler2()
    
