import requests
import json

LOGIN_URL = 'https://www.memrise.com/login/'
COURSES_URL = 'https://www.memrise.com/ajax/courses/dashboard/?courses_filter=most_recent&offset=0&limit=4&get_review_count=false'


class Login:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        with requests.Session() as client:
            client.get(LOGIN_URL)  # sets cookie
            csrftoken = client.cookies['csrftoken'] if 'csrftoken' in client.cookies else client.cookies['csrf']
            login_data = {'username': self.username, 'password': self.password, 'csrfmiddlewaretoken': csrftoken, 'next': '/'}
            client.post(LOGIN_URL, data=login_data, headers=dict(Referer=LOGIN_URL))

            courses = client.get(COURSES_URL).text
            self.course_data = json.loads(courses)

    def get_course(self):
        # return self.course_data
        return json.dumps(self.course_data, indent=4, sort_keys=True)


if __name__ == "__main__":
    cs = Login('test_skr47ch', 'test_password')
    result = cs.get_course()
    print(result)
