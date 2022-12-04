import json
import time
from package.tcppinglib.tcp_ping import tcpping

def lambda_handler(event, context):
  t = time.time()

  try:
    hostname = event['queryStringParameters']['host']

    host = tcpping(hostname, 80, 0.5, 2, 0)

    if (host.packets_received < 1):
      return {
        'statusCode': 400,
        'body': json.dumps({
          'success': False,
          'data': {
            'message': 'Offline or unreachable',
            'host': event['headers']['Host']
          },
          'time': time.time() - t
        })
      }

    return {
      'statusCode': 200,
      'body': json.dumps({
        'success': True,
        'data': {
          'received': host.packets_received,
          'loss': host.packet_loss,
          'latency': host.avg_rtt,
          'host': event['headers']['Host']
        },
        'time': time.time() - t
      })
    }
  except Exception as e:
    return {
      'statusCode': 400,
      'body': json.dumps({
        'success': False,
        'data': {
          'message': 'Invalid hostname',
          'error': str(e),
          'host': event['headers']['Host']
        },
        'time': time.time() - t
      })
    }