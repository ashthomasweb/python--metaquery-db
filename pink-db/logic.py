
import ui
import dal_mysql
import dal_mongodb
import dal_test_db
import credentials

db = None
mydb = None

class DependencyInjection():

    global db

    def switch(input):
        global db
        global mydb

        if input == 1:
            # set active db to test module in DAL
            db = dal_test_db.test_db_1
            print('Interface connected to Test db1')
            ui.server_display_text.delete('1.0', 'end')
            ui.server_display_text.insert('1.0', 'Test DB')
        elif input == 2:
            # get credentials and set active db to local MongoDB module in DAL
            dal_mongodb.myclient = credentials.myclient

            # connect module caller and global interface object
            db = dal_mongodb.GlobalCaller
            print('Interface connected to local MongoDB')
            ui.server_display_text.delete('1.0', 'end')
            ui.server_display_text.insert('1.0', 'MongoDB Local')
        elif input == 3:
            # get credentials and set active db to local MySQL module in DAL
            dal_mysql.mydb = credentials.db
            # set db server/query variable in DAL
            dal_mysql.set_db_server()
            # connect module caller and global interface object
            db = dal_mysql.GlobalCaller
            print('Interface connected to local MySQL')
            ui.server_display_text.delete('1.0', 'end')
            ui.server_display_text.insert('1.0', 'MySQL Local')
        else: 
            print('failboat sailboat')
 

# db set by DI
# called from ui
# method run in appropriate DAL
class GlobalInterface():

    def show_all_db():
        db.show_all_db()

    def create_db():
        db.create_db()



    # # mock CRUD operations 
    # def create_test():
    #     db.create()

    # def read_test():
    #     db.read()

    # def update_test():
    #     db.update()

    # def delete_test():
    #     db.delete()


# Return to UI objects

class Results():

    results = None

    def __init__(self):
        pass    

    def display_results(self):
        for x in self.results:
            ui.db_query_text.insert('1.0', f'{x}\n')

    def set_result(self, input):
        self.results = input
        self.display_results()


result_sender = Results()


class Messages():

    message = None
    
    def __init__(self):
        pass

    def display_message(self):
        ui.message_display_text.delete('1.0', 'end')

        # for x in self.message:
        ui.message_display_text.insert('1.0', f'{self.message}')
        
    def set_message(self, input):
         self.message = input
         self.display_message()


message_sender = Messages()














# END of document
