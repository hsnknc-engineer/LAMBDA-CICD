import json

def lambda_handler(event, context):
    # Beispieländerung für den Test
    return {
        'statusCode': 200,
        'body': json.dumps('HI, I would like update LAMBDA')
    }
