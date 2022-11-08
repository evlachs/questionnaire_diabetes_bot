
BOT_TOKEN = 'TOKEN'

SPREADSHEET_ID = 'ID'

GIFT_MENU_URL = 'URL'

BOT_URL = 'URL'

GROUP_ID = 'GROUP_ID'

SERVICE_ACCOUNT = 'path/to/service_account_file.json'  # it's recommended to place it in the 'data' folder

WEBHOOK_HOST = 'IP-address of your sever'
WEBHOOK_PORT = 443  # 443, 80, 88 or 8443
WEBHOOK_LISTEN = 'IP-address of your sever'  # or 0.0.0.0

WEBHOOK_SSL_CERT = 'path/to/webhook_cert.pem'  # it's recommended to place it in the 'data' folder
WEBHOOK_SSL_PRIVATE = 'path/to/webhook_pkey.pem'  # it's recommended to place it in the 'data' folder

WEBHOOK_URL_BASE = f'https://{WEBHOOK_HOST}:{WEBHOOK_PORT}'
WEBHOOK_URL_PATH = f'/webhook/{BOT_TOKEN}'
