import os


def pre_init(data_root, image):
    os.makedirs(os.path.join(data_root, 'alertmanager'))
    with open(os.path.join(data_root, 'alertmanager', 'config.yml'), 'w') as file_writer:
        file_writer.write('''
global:
  resolve_timeout: 5m

route:
  group_by: ['alertname']
  group_wait: 10s
  group_interval: 1m
  repeat_interval: 10m
  receiver: 'web.hook'

receivers:
  - name: 'web.hook'
    webhook_configs:
      - url: http://webhook:12345/webhook
        send_resolved: false
        ''')


def post_init(data_root, image):
    pass