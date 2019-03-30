import MemriseLogin
new_login = MemriseLogin.Login('test_skr47ch', 'test_password')
course_list = new_login.get_course()
TEXT = None

for course in course_list['courses']:
    id_ = course['id']
    name_ = course['name']

    progress_ = None #str(course['goal']['points']) + "/" + str(course['goal']['goal'])
    streak_ = None #course['goal']['streak']

    print(f"Course ID = {id_}, Course Name = {name_}, Today's progress' = {progress_}, Streak = {streak_}")
