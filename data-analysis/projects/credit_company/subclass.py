import classCreditBase as ccb
from datetime import date
from datetime import datetime

class Clients(ccb.PreClients):
    """
    Builder
    :param ID: unique identifier/primary key
    :param name: name of the client (no borrower yet)
    :param firstnm: the first name of the client
    :param type: the type of the credit
    :param req_date: request credit date
    :param req_amount: credit amount request
    :param status: the status of the credit - (to_validate/approved/current/finished)
    OWN parameters...
    :param author_date: the date when the credit was authorized
    :param author_amount: the amount authorized
    :param pay_timing: the timing established for the client payments - (fortnightly, monthly, bimonthly, quarterly, semiannual, annual)
    :param interest: the interest rate established for the client
    :param expec_date: the expected date when the client payments finished
    :param cap_pay: list of amount payments to capital from the client 
    :param delinq: tuples with the date and continuous period of lack payments of the client"""
    def __init__(self,  ID:str, name: str, firstnm: str, type: str, req_date: date, req_amount: int, status: str, author_date: date, author_amount: int, pay_timing: str, interest: float, expec_date: date, cap_pay: float, delinq: list):
        super().__init__(ID, name, firstnm, type, req_date, req_amount, status)
        self.__author_date = datetime.strptime(str(author_date),"%d-%m-%Y").date()
        self.__author_amount = author_amount
        self.__pay_timing = pay_timing
        self.__interest = interest
        self.__expec_date = datetime.strptime(str(expec_date),"%d-%m-%Y").date()
        self.__cap_pay = cap_pay
        self.__delinq = delinq

    #Getters
    @property
    def author_date(self):
        return self.__author_date
    
    @property
    def author_amount(self):
        return self.__author_amount
    
    @property
    def pay_timing(self):
        return self.__pay_timing
    
    @property
    def interest(self):
        return self.__interest
    
    @property
    def expec_date(self):
        return self.__expec_date
    
    @property
    def cap_pay(self):
        return self.__cap_pay
    
    @property
    def delinq(self):
        return self.__delinq
    
    #Setters
    @author_date.setter
    def author_date(self, author_date):
        self.__author_date = author_date

    @author_amount.setter
    def author_amount(self, author_amount):
        self.__author_amount = author_amount

    @pay_timing.setter
    def pay_timing(self, pay_timing):
        self.__pay_timing = pay_timing

    @interest.setter
    def interest(self, interest):
        self.__interest = interest

    @expec_date.setter
    def expec_date(self, expec_date):
        self.__expec_date = expec_date

    @cap_pay.setter
    def cap_pay(self, cap_pay):
        self.__cap_pay = cap_pay

    @delinq.setter
    def delinq(self, delinq):
        self.__delinq = delinq

    def __str__(self):
        """
        Method to print the client basic information in str
        :return: Name, first name, status
        :rtype: str
        """
        return "Request information of: {}, {} | Credit Type: {} | Required Amount: {} | Status: {}".format(self.__firstnm, self.__name, self.__type, self.__req_amount, self.__status)