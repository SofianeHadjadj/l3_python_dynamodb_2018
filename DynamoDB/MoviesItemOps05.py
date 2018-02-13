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

title = "Sofiane is : The Arabian Gladiator"
year = 2018

print("Tentative de mise à jour conditionnelle")

try:
    response = table.update_item(
        Key={
            'year': year,
            'title': title
        },
        UpdateExpression="remove info.acteurs[0]",
        ConditionExpression="size(info.acteurs) >= :num",
        ExpressionAttributeValues={
            ':num': 3
        },
        ReturnValues="UPDATED_NEW"
    )
except ClientError as e:
    if e.response['Error']['Code'] == "ConditionalCheckFailedException":
        print(e.response['Error']['Message'])
    else:
        raise
else:
    print("Mise à jour réalisé avec succès :")
    print(json.dumps(response, indent=4, cls=DecimalEncoder))