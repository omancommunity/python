"""
Short tutorial & notes starting from
split directory, you can navigate and
learn from that; or run this script and
go with it step by step .
You can do whatever you want this for passing and learn
and study python .


"""



global is_active






def _play_thing() -> object:
    """
    This is the start point
    :return: _menu_and_friends()
    """

    f  = open("tag.txt","r")
    tag = "".join(f.readlines())
    print('\n\n\n' +u'\u001b[46;1m'+tag+ '\n\n\n\n'+ u'\u001b[0m'+ '\n\n\n')
    return _menu_and_friends()


def _menu_and_friends() -> bool:
    """
    simple questions and answers, by number and friends
    :return: -> is_active
    """
    select = 0
    is_active = True
    print('                   ' + u'\u001b[42m [ Please select  option from list ]  '+u'\u001b[0m'+ '                  \n')
    print("    " + u"\u001b[32;1m     [ Which path you want to start 1 , 2, 3, 4, 5 : ]    "+u'\u001b[0m'+ '                  \n')
    print(u'\u001b[32;1m > [ 1 ]'+ u'\u001b[0m' +" Short introduction, python ?"+ "\n")
    print(u'\u001b[32;1m > [ 2 ] '+ u'\u001b[0m' +" Scraping web pages using python ?" +"\n")
    print(u'\u001b[32;1m > [ 3 ] '+ u'\u001b[0m' +" Python core and tricks! " +"\n")
    print(u'\u001b[32;1m > [ 4 ] '+ u'\u001b[0m' +" Examples & short notes" +"\n")
    print(u'\u001b[32;1m > [ 5 ] '+ u'\u001b[0m' +" Exit \n")
    select = input(": ")

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
