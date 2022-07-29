import json

import db


def lambda_handler(event, context):
    """Sample pure Lambda function

    Parameters
    ----------
    event: dict, required
        API Gateway Lambda Proxy Input Format

        Event doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-input-format

    context: object, required
        Lambda Context runtime methods and attributes

        Context doc: https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html

    Returns
    ------
    API Gateway Lambda Proxy Output Format: dict

        Return doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html
    """

    try:

        path = event['path']

        output = ''

        # Hello world endpoint
        if path == '/hello':
            output = 'Lambda is working!'

        # Custom hello endpoint
        elif path == '/helloCustom':
            raise NotImplementedError()

        # Get names endpoint
        elif path == '/getNames':
            raise NotImplementedError()
        
        elif path == '/addName':
            raise NotImplementedError()

        return {
            "statusCode": 200,
            "body": json.dumps(output)
        }
    
    # Error handling
    except Exception as e:
        return {
            "statusCode": 502,
            "body": json.dumps({
                "error": repr(e)
            })
        }
