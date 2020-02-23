class CallBack:
    def __init__(self, message="", datas=[], status="", forms=""):
        self.message = message
        self.datas = datas
        self.status = status
        self.forms = forms

    def get_dict(self):
        return {
            "message": self.message,
            "datas": self.datas,
            "status": self.status,
            "forms": self.forms
        }
