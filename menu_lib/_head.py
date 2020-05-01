

"""
Manage menu list

simple loop and dictionary
"""
class _menu(object):
    def __init__(self,
                 menu_list=None,
                 is_active=False):
        self.is_active = is_active
        self.menu_list = menu_list

        if not menu_list:
            menu_list = []
            print("Please provide list menu you wish ..")

    def looping_things(self):
        while self.is_active:
            menu_total = len(self.menu_list) + 1
            if menu_total > 1 and self.is_active:







