from hashlib import md5
import requests

WD_AUTHENTICATION = "https://wdauth.wsi.edu.pl/"


def get_wd_token(user_id: int, password: str) -> str:
    pass_md5 = md5(password.encode('utf-8')).hexdigest()
    token_url = WD_AUTHENTICATION + "auth?album=" + str(user_id) + "&pass=" + pass_md5
    # Alternatywnie
    # token_url = f'{WD_AUTHENTICATION}auth?album={str(user_id)}&pass={pass_md5}'
    resp = requests.get(token_url)
    if resp.status_code == 200:
        token = resp.text
        return token



if __name__ == '__main__':
    pass