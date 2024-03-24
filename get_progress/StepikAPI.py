from requests import get, post
from requests.auth import HTTPBasicAuth

OAUTH_URL = "https://stepik.org/oauth2/token/"
API_URL = "https://stepik.org/api/progresses"

class StepikAPI:
    """Класс, представляющий клиент Stepik.

    Note:
    ----
        Чтобы получить client id и client secret, необходимо
        создать oAuth приложение на сайте https://stepik.org/oauth2/applications/.

    Attributes:
    ----------
        client_id (:obj:`str`): oAuth client id, полученный после создания oAuth
        приложения.
        secret_id (:obj:`str`): oAuth client secret, полученный после создания oAuth
        приложения.

    """

    client_id: str
    client_secret:str

    def __init__(self: any, client_id: str, client_secret: str) -> None:  # noqa: D107
        self.client_id = client_id
        self.client_secret = client_secret

        try:
            auth = HTTPBasicAuth(client_id, client_secret)
            resp = post(url = OAUTH_URL, auth = auth,
                        data = {
                            'grant_type': 'client_credentials',
                            'scope': 'read'
                        }).json()
            self.token = resp['access_token']
        except Exception:
            print("Error while obtaining token")

    def get_progress(self: any, course_id: str) -> str:
        """Возвращает прогресс прохождения курса.

        Прогресс исчисляется аналогично сайта Stepik - отношение
        количества пройденных шагов к общему количеству шагов в курсе.

        Args:
        ----
            course_id (:obj:`str`): ID курса.

        Returns:
        -------
            :obj:`str`: Прогресс прохождения курса в процентах.

        """
        try:
            resp = get(url = API_URL, headers = {
                'Authorization': f'Bearer {self.token}'
            }, params = {
                'ids[]': course_id
            }).json()
        except Exception:
            print("Error")
            resp = None
        percentage = int(resp['progresses'][0]['n_steps_passed']/
                   resp['progresses'][0]['n_steps'] * 100)
        return f"{percentage}%"
