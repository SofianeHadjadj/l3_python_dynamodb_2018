from __future__ import print_function 
import boto3
import json
import decimal
from boto3.dynamodb.conditions import Key, Attr
from botocore.exceptions import ClientError

class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            if o % 1 > 0:
                return float(o)
            else:
                return int(o)
        return super(DecimalEncoder, self).default(o)

dynamodb = boto3.resource("dynamodb", region_name='us-west-2', endpoint_url="http://localhost:8000")

table = dynamodb.Table('SofianeHadjadjMovies')

title = "Sofiane is : The Arabian Gladiator"
year = 2018

try:
    response = table.get_item(
        Key={
            'year': year,
            'title': title
        }
    )
except ClientError as e:
    print(e.response['Error']['Message'])
else:
    item = response['Item']
    print("Le film a été trouvé avec succès :")
    print(json.dumps(item, indent=4, cls=DecimalEncoder))