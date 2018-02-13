from __future__ import print_function 
import boto3
from botocore.exceptions import ClientError
import json
import decimal

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

title = "Rush"
year = 2013

print("Tentative de suppression conditionnelle...")

try:
    response = table.delete_item(
        Key={
            'year': year,
            'title': title
        }
    )
except ClientError as e:
    if e.response['Error']['Code'] == "ConditionalCheckFailedException":
        print(e.response['Error']['Message'])
    else:
        raise
else:
    print("Film supprimé avec succès :")
    print(json.dumps(response, indent=4, cls=DecimalEncoder))