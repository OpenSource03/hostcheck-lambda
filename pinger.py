import json
from package.tcppinglib.tcp_ping import tcpping

def lambda_handler(event, context):
  hostname = event['queryStringParameters']['host']

  host = tcpping(hostname, 80, 1, 2, 0.2)

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