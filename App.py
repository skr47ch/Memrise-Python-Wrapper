import MemriseLogin

new_login = MemriseLogin.Login('test_skr47ch', 'test_password')
course_list = new_login.get_course()

for course in course_list['courses']:
    id_ = course['id']
    name_ = course['name']

    # some courses may not have goals attached to them.
    try:
        goal_ = course['goal']['goal']
        points_ = course['goal']['points']
        streak_ = course['goal']['streak']
    except KeyError:
        goal_, points_, streak_ = None, None, None

    progress_ = str(points_) + "/" + str(goal_)

    print(f"Course ID = {id_}, Course Name = {name_}, Today's progress' = {progress_}, Streak = {streak_}")
