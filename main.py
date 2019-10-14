import json
import requests

config_text = ""

with open("conf.json", 'r') as f:
    config_text = f.read()

config = json.loads(config_text)
wp_login =f"{config['url']}/wp-login.php"

with requests.Session() as s:
    headers = {
        'Cookie' : 'wordpress_test_cookie=WP Cookie check'
    }
    data = {
        'log': config["username"],
        'pwd': config["password"],
        'wp-submit': 'Log In',
        'redirect_to': config["redir"],
        'testcookie': '1'
    }
    # Login
    s.post(wp_login, headers=headers, data=data)
    # Get other pages
    resp = s.get(config["redir"])

    print(resp.text)