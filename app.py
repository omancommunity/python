"""
Short tutorial & notes starting from
split directory, you can navigate and
learn from that; or run this script and
go with it step by step .
You can do whatever you want this for passing and learn
and study python .

Still project started in 1/5/2020 and you are more than welcome
to add fix and modify what are think it is good practice and handy to learn
keep sharing and separate love over the world .
"""

import os
global is_active




# this is work for most operation system
HOME_DIR = os.path.expanduser("~")
DIRE_PATH = HOME_DIR + "/PycharmProjects/python-master/"
# for me it will be
# DIRE_PATH = HOME_DIR + "/PycharmProjects/python/"


# If you're on Python 3.5+ you can use pathlib.Path.home():
# from pathlib import Path
# HOME_DIR = str(Path.home())
# https://stackoverflow.com/questions/4028904/how-to-get-the-home-directory-in-python




def _make_text_bold(bold_msg) -> str:
    """
    Return bold_msg text with added decoration using ansi code
    :param msg:
    :return: u"\u001b[1m"+ bold_msg + u"\u001b[0m"
    """
    return u"\u001b[1m"+ bold_msg + u"\u001b[0m"


def _make_text_underline(under_line_msg) -> str:
    """
    Return under_line_msg text with added decoration using ansi code
    :param msg:
    :return: u"\u001b[4m"+ under_line_msg + u"\u001b[0m"
    """
    return u"\u001b[4m"+ under_line_msg + u"\u001b[0m"




def _play_thing() -> object:
    """
    This is the start point
    :return: _menu_and_friends()
    """

    # Make sure when you open a file select correct permission
    # use [with] and try to [catch any error] will raise finally [clean your room]
    # when you wake up don't just open things without closing,
    # [close the file]
    tag = None
    try:
        # make sure to add Directory  PATH to tag.txt file
        with open(DIRE_PATH +"tag.txt","r") as f:
            tag = "".join(f.readlines())
            f.close()
    except Exception as err:
        print(err)


    if tag is not None:
        print('\n\n\n' +u'\u001b[46;1m'+tag+ '\n\n\n\n'+ u'\u001b[0m'+ '\n\n\n')
    else:
        print("There was an error with reading tag.txt file"
              " please make sure you enter correct path directory "
              "to this project .")
    return _menu_and_friends()


def _menu_and_friends() -> bool:
    """
    simple questions and answers, by number and friends
    :return: -> is_active
    """
    select = 0
    is_active = True

    # make sure if you use ANSI escape codes to change color and things to use reset color code [ u'\u001b[0m' ]
    # just try to change number and things and figure out which color stable for you , just you
    # for more information you can visit :
    # https://www.lihaoyi.com/post/BuildyourownCommandLinewithANSIescapecodes.html#background-colors
    """
    Black: \u001b[30m
    Red: \u001b[31m
    Green: \u001b[32m
    Yellow: \u001b[33m
    Blue: \u001b[34m
    Magenta: \u001b[35m
    Cyan: \u001b[36m
    White: \u001b[37m
    Reset: \u001b[0m
    """

    print('                   ' + u'\u001b[42m' + _make_text_bold("[ Please select  option from list ]")+u'\u001b[0m'+ '                  \n')
    print("    " + u"\u001b[32;1m   \u001b[1m  [ Which path you want to start 1 , 2, 3, 4, 5 : ]    "+u'\u001b[0m'+ '                  \n')
    print(u'\u001b[32;1m > [ 1 ]'+ u'\u001b[0m' +_make_text_underline(" Short introduction, python ?")+ "\n")
    print(u'\u001b[32;1m > [ 2 ] '+ u'\u001b[0m' +_make_text_underline(" Scraping web pages using python ?") +"\n")
    print(u'\u001b[32;1m > [ 3 ] '+ u'\u001b[0m' +_make_text_underline(" Python core and tricks! ") +"\n")
    print(u'\u001b[32;1m > [ 4 ] '+ u'\u001b[0m' +_make_text_underline(" Examples & short notes") +"\n")
    print(u'\u001b[32;1m > [ 5 ] '+ u'\u001b[0m' +_make_text_underline(" Exit \n"))
    select = input("Type your numer here: ")

    while is_active:
        if int(select) == 1 and is_active:
            print(u'\u001b[32;1m [1.]'+ u'\u001b[0m' +" Short introduction, python ?"+ "\n")
            is_active = False
            return is_active
        elif int(select) == 2 and is_active:
            print(u'\u001b[32;1m [2.] '+ u'\u001b[0m' +"Scraping web pages using python ?" +"\n")
            is_active = False
            return is_active
        elif int(select) == 3 and is_active:
            print(u'\u001b[32;1m [3.] '+ u'\u001b[0m' +"Python core and tricks! " +"\n")
            is_active = False
            return is_active
        elif int(select) == 4 and is_active:
            print(u'\u001b[32;1m [4.] '+ u'\u001b[0m' +" Examples & short notes" +"\n")
            is_active = False
            return is_active
        elif int(select) == 5 and is_active:
            print(u'\u001b[32;1m [5.] '+ u'\u001b[0m' +"Exit \n")
            print("\ngood..bay ...\nclose tutorials.....now.....\n")
            is_active = False
            return is_active
        else:
            print("\n Please make sure to select number from option above !!\n Rerun the script again ...  \n")
            is_active = False
            return is_active
    return False


if __name__ == '__main__':
    _play_thing()
