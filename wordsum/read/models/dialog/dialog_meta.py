class Dialog_Meta():


    def __init__(self):
        self.dialog = False
        self.dialog_being = False
        self.dialog_continue = False
        self.dialog_end  = False


    @property
    def dialog(self):
        return self.dialog

    @dialog.setter
    def dialog(self, dialog):
        self.dialog = dialog


    @property
    def dialog_begin(self):
        return self.dialog_begin

    @dialog_begin.setter
    def dialog_begin(self, dialog_begin):
        self.dialog_begin = dialog_begin


    @property
    def dialog_continue(self):
        return self.dialog_continue

    @dialog_continue.setter
    def dialog_continue(self, dialog_continue):
        self.dialog_continue = dialog_continue


    @property
    def dialog_end(self):
        return self.dialog_end

    @dialog_end.setter
    def dialog_end(self, dialog_end):
        self.dialog_end = dialog_end



