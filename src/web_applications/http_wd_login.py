from dataclasses import dataclass
from hashlib import md5
import requests

WD_AUTHENTICATION_URL = "https://wdauth.wsi.edu.pl/"


@dataclass
class Token:
    studentid: int
    wdauth: str
    expiry_epoch_s: int


def get_wd_token(user_id: str, password: str) -> tuple[Token, list[str]]:
    pass_md5 = md5(password.encode('utf-8')).hexdigest()
    # Alternatywnie
    token_url = f'{WD_AUTHENTICATION_URL}authenticate?album={user_id}&pass={pass_md5}'
    resp = requests.get(token_url)
    if resp.status_code == 200:
        data = resp.json()
        token = data['token']
        roles = data['roles']
        return token, roles
    else:
        raise RuntimeError('Unauthorized')


if __name__ == '__main__':
    token_ = get_wd_token('1234', '--secret--')
    print(token_)
