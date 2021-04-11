from datetime import datetime
from notifypy import Notify
import webbrowser
import json

# gets current time and makes code with it
now = datetime.now()

# this is as simple as hell, basically code consists of 3 numbers, first of them is day of the week where
# 0 is sunday and 6 is saturday, second two numbers are time when the lecture starts
# for example: 'კალკულუსი სამშაბათი' --> 211 --> 2 & 11 --> means that calculus starts on Tuesday, 11:00 AM.
# but this code is string data type so I have converted that into integer to make arithmetic operations on that.


coden = int(now.strftime('%w%H'))  # %w is weekday, %H is hour

# this is for testing
#coden = "enter code here"

# with this you can switch different users


user_mode = 1

# dictonary about different lectures and times, their links and logos which makes cooler.


lectures = {
    'კალკულუსი სამშაბათი': {
        'code': 211,
        'lecture_link': f'meet.google.com/wva-visk-hzf?pli=1&authuser={user_mode}',
        'logo': 'logos\calc.png'
    },
    'კალკულუსი ხუთშბათი': {
        'code': 411,
        'lecture_link': f'meet.google.com/wva-visk-hzf?pli=1&authuser={user_mode}',
        'logo': 'logos\calc.png'

    },
    'პერსონალური კომპიუტერის არქიტექტურა': {
        'code': 215,
        'lecture_link': f'meet.google.com/irf-djha-bqw?pli=1&authuser={user_mode}',
        'logo': 'logos\pca.png'
    },
    'ბექენდი': {
        'code': 315,
        'lecture_link': f'meet.google.com/ckb-cvwd-rrt?pli=1&authuser={user_mode}',
        'logo': 'logos/backend.png'
    },
    'ფრონტენდი': {
        'code': 415,
        'lecture_link': f'meet.google.com/kip-adfc-vcs?pli=1&authuser={user_mode}',
        'logo': 'logos/frontend.png'
    },
    'პითონი': {
        'code': 617,
        'lecture_link': f'meet.google.com/kwr-evqm-nss?pli=1&authuser={user_mode}',
        'logo': 'logos\python.jpg'
    },
    'ციფრული ტექნოლოგიების პრინციპები': {
        'code': 619,
        'lecture_link': f'meet.google.com/zyc-mnki-pxt?pli=1&authuser={user_mode}',
        'logo': 'logos\ctp.png'
    }
}


# sends notification when executed.


def standard_message(lecture, time_left, logo):

    notification = Notify()
    notification.title = lecture
    notification.message = f'ლექციამდე დარჩენილია {time_left} საათი, არ დაგავიწყდეს BTU-სა და Google ქლასრუმებზე დავალების ნახვა.'
    notification.icon = logo
    notification.send()

# opens lecture link in the browser(in this case in google chrome)


def lecture_opener(url):
    webbrowser.register(
        'chrome',
        None,
        webbrowser.BackgroundBrowser(
            'C:\Program Files\Google\Chrome\Application\chrome.exe')
    )
    webbrowser.get('chrome').open(url)


# this is the main part of this programm, it navigates through "lectures" dictonary and picks neccesarry information when needed

for lecture in lectures:

    # when curent time equal to code in given dictonary it sends notification about that and opens link instantly
    if coden == lectures[lecture]['code']:
        standard_message(lecture, 0, lectures[lecture]['logo'])
        lecture_opener(lectures[lecture]['lecture_link'])

    # these statements are executed when 24; 6; 1 hour are left
    if coden == lectures[lecture]['code'] - 100:
        standard_message(lecture, 24, lectures[lecture]['logo'])

    if coden == lectures[lecture]['code'] - 25:
        standard_message(lecture, 6, lectures[lecture]['logo'])

    if coden == lectures[lecture]['code'] - 1:
        standard_message(lecture, 1, lectures[lecture]['logo'])
