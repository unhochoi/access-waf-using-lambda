import json
import boto3

client = boto3.client('wafv2')

def lambda_handler(event, context):

    # ipset 생성
    response1 = client.create_ip_set(
    Name='unho-create-global-ipset',
    Scope='CLOUDFRONT',
    Description='unho-create-global-ipset',
    IPAddressVersion='IPV4',
    Addresses=[
        '10.0.0.0/24',
    ]
    )
    
    # ipset 출력
    response2 = client.list_ip_sets(
        Scope='CLOUDFRONT')
    
    print(response2)
    
    # TODO implement
    return {
        'statusCode': 200,
        
        'body': json.dumps('Hello from Lambda!')
    }
