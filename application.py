import json
from account import Account
from sign_in_page import Sign_In_Page

class Application:

    def __init__(self, accountList=[]):
        self.accountList = accountList
        
    def sign_up(self,username,password,email):
        for acc in self.accountList:
            if acc.username == username:
                return True
        else:
            account = Account(username, password, email)
            self.accountList.append(account)
            return False

    def sign_in(self, username, password):
        if self.accountList == []:
            return (True,None)
        else:
            for acc in self.accountList:
                if acc.username == username and acc.password == password:
                    return (False, acc)
            else:
                return (True, None)

    @classmethod
    def from_json(cls, data):
        decoded_accounts = []
        for i in range(len(data)):
            decoded_accounts.append(Account.from_json(data[i]))
        return decoded_accounts

    def load(self):
        with open("accounts.json", "r") as accounts_json:
            data = json.load(accounts_json)
            decoded_accounts = Application.from_json(data)
            self.accountList = decoded_accounts

    def save(self):
        with open("accounts.json", "w") as accounts_json:
            serilizated_data = self.serilization()
            json.dump(serilizated_data, accounts_json,sort_keys=True, indent=4)

    def serilization(self):
        exeList = []
        for i in range(len(self.accountList)):
            serilizated = {}
            serilizated["username"] = self.accountList[i].username
            serilizated["password"] = self.accountList[i].password
            serilizated["email"] = self.accountList[i].email
            serilizated["loan"] = self.accountList[i].loan
            exeList.append(serilizated)
        return exeList