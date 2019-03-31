import requests
import json
import mycredentials
import URLs

LOGIN_URL = URLs.LOGIN_URL
COURSES_URL = URLs.COURSES_URL
PERIOD_URL = URLs.PERIOD_URL
USER_URL = URLs.USER_URL
STREAK_GRAPH_URL = URLs.STREAK_GRAPH_URL


class Login:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        with requests.Session() as self.client:
            self.client.get(LOGIN_URL)  # sets cookie
            csrftoken = self.client.cookies['csrftoken'] if 'csrftoken' in self.client.cookies else self.client.cookies['csrf']
            login_data = {'username': self.username, 'password': self.password, 'csrfmiddlewaretoken': csrftoken, 'next': '/'}
            self.client.post(LOGIN_URL, data=login_data, headers=dict(Referer=LOGIN_URL))

    def get_course(self):
        courses = self.client.get(COURSES_URL).text
        return json.loads(courses)

    def get_user_graph(self):
        streak_graph = self.client.get(STREAK_GRAPH_URL).text
        return json.loads(streak_graph)


if __name__ == "__main__":
    cs = Login(mycredentials.username, mycredentials.password)
    result = cs.get_user_graph()
    print(json.dumps(result, indent=4, sort_keys=True))
