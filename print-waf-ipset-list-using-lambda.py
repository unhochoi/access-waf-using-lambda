import json
import boto3

client = boto3.client('wafv2')

def lambda_handler(event, context):
    
    response = client.list_ip_sets(
        Scope='CLOUDFRONT')

    print(response)
    
    # TODO implement
    return {
        'statusCode': 200,
        
        'body': json.dumps('Hello from Lambda!')
    }
