import gspread.client

from datetime import datetime


class SheetManager:
    """

    """

    def __init__(self, gc: gspread.client.Client, spreadsheet_id: str):
        self.today = datetime.now().strftime('%d.%m.%Y')
        self.sh = gc.open_by_key(spreadsheet_id)
        self.users_ws = self.sh.get_worksheet(0)
        self.stat_ws = self.sh.get_worksheet(1)
        if not self.__check_today():
            self.__add_new_day()
        self.today_row = self.stat_ws.find(self.today).row

    def get_empty_cell_index(self) -> int:
        col_values = self.users_ws.col_values(1)
        empty_cell_index = len(col_values) + 1
        return empty_cell_index

    def check_user_in_spreadsheet(self, user_id: str) -> bool:
        users_ids = self.users_ws.col_values(1)
        if user_id in users_ids:
            return True
        return False

    def load_new_user_info(self, user_info: dict, row_ind: int) -> None:
        values_list = list(user_info.values())
        self.users_ws.update('A{0}:Z{0}'.format(row_ind), [values_list])

    def clear_user_info(self, user_id: str) -> None:
        users_ids = self.users_ws.col_values(1)
        user_ind = users_ids.index(user_id) + 1
        self.users_ws.delete_row(user_ind)

    def add_bot_activates_value(self) -> None:
        current_activates = int(self.stat_ws.acell('B2').value)
        self.stat_ws.update('B2', current_activates+1)

    def add_quest_passed_value(self) -> None:
        current_passed = int(self.stat_ws.acell('B3').value)
        self.stat_ws.update('B3', current_passed+1)

    def __add_new_day(self) -> None:
        last_day_index = len(self.stat_ws.col_values(5))
        default_info = [self.today, 0, 0, 0]
        self.stat_ws.update('E{0}:H{0}'.format(last_day_index+1), [default_info])

    def __check_today(self) -> bool:
        last_date_index = len(self.stat_ws.col_values(5))
        last_date = self.stat_ws.cell(last_date_index, 5).value
        if last_date == self.today:
            return True
        return False

    def add_new_member(self) -> None:
        current_users_val = int(self.stat_ws.cell(self.today_row, 6).value)
        self.stat_ws.update_cell(self.today_row, 6, current_users_val+1)

    def add_left_member(self) -> None:
        current_users_val = int(self.stat_ws.cell(self.today_row, 7).value)
        self.stat_ws.update_cell(self.today_row, 7, current_users_val+1)

    def add_new_message(self) -> None:
        current_messages_val = int(self.stat_ws.cell(self.today_row, 8).value)
        self.stat_ws.update_cell(self.today_row, 8, current_messages_val+1)
