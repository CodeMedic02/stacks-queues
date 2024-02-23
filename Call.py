# Name: Trent Adams
# Date: 2024-01-21

from time import strftime


class Call(object):
    
    def __init__(self, client_id=0, client_name="Unknown", client_phone="Unknown"):
        self.client_id = client_id
        self.client_name = client_name
        self.client_phone = client_phone
        self.call_date = strftime("%m/%d/%Y")
        self.call_time = strftime("%H:%M")

    # __str__() automatically called when you print the object.


    def __str__(self):
        return str(self.client_id) + "," + self.client_name + \
            "\n\tPhone: " + self.client_phone + \
            "\n\tDate/Time: " + self.call_date + " @ " + self.call_time

