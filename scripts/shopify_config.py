import os
from pathlib import Path

def load_env():
    env_file = Path(__file__).resolve().parent.parent / '.env'
    if env_file.exists():
        with open(env_file, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#') and '=' in line:
                    k, v = line.split('=', 1)
                    os.environ.setdefault(k.strip(), v.strip())

load_env()

TOKEN = os.environ.get('SHOPIFY_ACCESS_TOKEN', '')
STORE = os.environ.get('SHOPIFY_STORE', 'f0chrv-j7.myshopify.com')
THEME_ID = os.environ.get('SHOPIFY_THEME_ID', '155909324961')
