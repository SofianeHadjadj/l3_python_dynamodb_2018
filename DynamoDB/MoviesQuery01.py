from __future__ import print_function
import boto3
import json
import decimal
from boto3.dynamodb.conditions import Key, Attr

class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            if o % 1 > 0:
                return float(o)
            else:
                return int(o)
        return super(DecimalEncoder, self).default(o)

dynamodb = boto3.resource('dynamodb', region_name='us-west-2', endpoint_url="http://localhost:8000")

table = dynamodb.Table('SofianeHadjadjMovies')

print("Films de l'année 1995 : ")

response = table.query(
    KeyConditionExpression=Key('year').eq(1995)
)

for i in response['Items']:
    print(i['year'], ":", i['title'])