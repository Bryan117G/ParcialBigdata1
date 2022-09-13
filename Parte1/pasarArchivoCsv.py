#Bryan Garavito 
import json
import boto3
import datetime
import csv 
import pandas as pd

def lambda_handler2():
    #TODO implement
    # Se importa la funcion date time para sacar la fecha y poderla agregar al nombre del archivo txt
    now2= datetime.datetime.now()
    #se llama la funcion strtime para convertir la funcion datetime a string 
    x2 = now2.strftime('%d %m %Y')
    
    s3 = boto3.resource('s3')
    s3.Bucket('dolarraw01').download_file('dolar '+ x2 + '.txt', '/tmp/dolar.txt')
    
    websites = pd.read_csv('dolar '+ x2 + '.txt',header = None) 
    websites.columns = ['FechaHora', 'Valor'] 
    websites.to_csv('dolar_processed_ '+ x2 + '.csv', index = None) 
    
    
    client= boto3.client("s3","us-east-1")
    s3= boto3.resource('s3')
    bucket = s3.Bucket('dolarprocessed01')

    client.put_object(Body='dolar '+ x2 + '.txt', Bucket='dolarprocessed01', Key ='dolar_processed_ '+ x2 + '.csv')

    return{
        'statusCode':200,
        'body': json.dumps('Hello from Lambda!')
    }
