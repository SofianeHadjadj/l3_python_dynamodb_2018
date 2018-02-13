from __future__ import print_function 
import boto3
import json
import decimal
from boto3.dynamodb.conditions import Key, Attr

class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            return str(o)
        return super(DecimalEncoder, self).default(o)

dynamodb = boto3.resource('dynamodb', region_name='us-west-2', endpoint_url="http://localhost:8000")

table = dynamodb.Table('SofianeHadjadjMovies')

print("Films commençant par 'The' en 2015 :")

response = table.query(
    ProjectionExpression="#yr, title, info.genres, info.actors[0]",
    ExpressionAttributeNames={ "#yr": "year" }, 
    KeyConditionExpression=Key('year').eq(2015) & Key('title').begins_with('The')
)

for i in response[u'Items']:
    print(json.dumps(i, cls=DecimalEncoder))