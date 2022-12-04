import json
from package.tcppinglib.tcp_ping import tcpping

def lambda_handler(event, context):
  try:
    hostname = event['queryStringParameters']['host']

    host = tcpping(hostname, 80, 1, 1, 0.2)

    return {
      'statusCode': 200,
      'body': json.dumps({
        'success': True,
        'data': {
          'latency': host.avg_rtt,
          'host': event['headers']['Host']
        }
      })
    }
  except:
    return {
      'statusCode': 400,
      'body': json.dumps('Invalid or offline host')
    }