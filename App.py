import MemriseLogin
import mycredentials

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

username = mycredentials.username
password = mycredentials.password
new_login = MemriseLogin.Login(username, password)


class App:
    # Course data

    def course(self):
        """Captures course details such as course name, goal, progress, and streak"""

        course_list = new_login.get_course()
        for course in course_list['courses']:
            id_ = course['id']
            name_ = course['name']
            # some courses may not have goals attached to them.
            try:
                goal_, points_, streak_ = course['goal']['goal'], course['goal']['points'], course['goal']['streak']
            except KeyError:
                goal_, points_, streak_ = None, None, None
            progress_ = str(points_) + "/" + str(goal_)

            print(f"Course ID = {id_}, Course Name = {name_}, Today's progress' = {progress_}, Streak = {streak_}")

    def graph(self):
        """Capture and show activity over time"""
        # Graph data
        attendance_data = new_login.get_user_graph()['attendance_data']

        data = []
        for record in attendance_data:
            data.append([record['day'], record['num_events']])

        df = pd.DataFrame(data, columns=['Day', 'Activity'])
        df.Day = pd.to_datetime(df.Day)

        grouped = df.groupby(pd.Grouper(key='Day', freq='M')).sum()
        # grouped.plot(x=grouped.index.month, kind='bar', stacked=True)
        grouped.plot()
        plt.show()


if __name__ == "__main__":
    item = App()
    item.graph()

