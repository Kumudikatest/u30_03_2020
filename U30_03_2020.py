import boto3
import json
ses = boto3.client("ses")

def handler(event, context):

    print(event)

    tabledetails = json.loads(json.dumps(event["Records"][0]["dynamodb"]))
    print(tabledetails)

    name = tabledetails["NewImage"]["Name"]["S"];
    email = tabledetails["NewImage"]["Email"]["S"];

    try:
        data = ses.send_email(
            Source="kumudika@adroitlogic.com",
            Destination={
                'ToAddresses': [email]
            },
            Message={
                'Subject': {
                    'Data': "Test"
                },
                'Body': {
                    'Text': {
                        'Data': "Test"
                    }
                }
            }
        )
    except BaseException as e:
        #print(e)
        raise(e)

    
    return {"message": "Successfully executed"}
