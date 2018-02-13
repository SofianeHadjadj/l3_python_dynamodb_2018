from __future__ import print_function 
import boto3
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

response = table.put_item(
   Item={
        'year': year,
        'title': title,
        'info': {
            'plot':"Il ne s'est rien produit.",
            'rating': decimal.Decimal(0)
        }
    }
)

print("L'opération a réussi :")
print(json.dumps(response, indent=4, cls=DecimalEncoder))