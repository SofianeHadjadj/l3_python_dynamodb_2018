from __future__ import print_function 
import boto3

dynamodb = boto3.resource('dynamodb', region_name='us-west-2', endpoint_url="http://localhost:8000")


table = dynamodb.create_table(
    TableName='SofianeHadjadjMovies',
    KeySchema=[
        {
            'AttributeName': 'year',
            'KeyType': 'HASH' 
        },
        {
            'AttributeName': 'title',
            'KeyType': 'RANGE' 
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'year',
            'AttributeType': 'N'
        },
        {
            'AttributeName': 'title',
            'AttributeType': 'S'
        },

    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 10,
        'WriteCapacityUnits': 10
    }
)

print("Table status:", table.table_status)
