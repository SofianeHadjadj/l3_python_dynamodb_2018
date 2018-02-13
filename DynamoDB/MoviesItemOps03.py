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

response = table.update_item(
    Key={
        'year': year,
        'title': title
    },
    UpdateExpression="set info.rating = :r, info.plot=:p, info.acteurs=:a",
    ExpressionAttributeValues={
        ':r': decimal.Decimal(5.5),
        ':p': "Un film avec énormément d'action !!!.",
        ':a': ["Sofiane Hadjadj", "Adem Hadjadj", "Moussa Hadjadj"]
    },
    ReturnValues="UPDATED_NEW"
)

print("Mise à jour réalisé avec succès :")
print(json.dumps(response, indent=4, cls=DecimalEncoder))