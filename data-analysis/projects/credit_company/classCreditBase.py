#This class contains the basic information of our possible clients

from datetime import date
from datetime import datetime
# Libraries to validate information

class PreClients: 
    """
    Builder
    :param ID: unique identifier/primary key
    :param name: name of the client (no borrower yet)
    :param firstnm: the first name of the client
    :param type: the type of the credit
    :param req_date: request credit date
    :param req_amount: credit amount request
    :param status: the status of the credit - (to_validate/approved/current/finished)
    """
    def __init__(self, ID:str, name: str, firstnm: str, type: str, req_date: date, req_amount: int, status: str):
        # There is not default builder for this case
        self.__ID = ID
        self.__name = name
        self.__firstnm = firstnm
        self.__type = type
        self.__req_date = datetime.strptime(str(req_date),"%d-%m-%Y").date()
        self.__req_amount = req_amount
        self.__status = status

    @property 
    def ID(self):
        """
        Method for obtain the primary key/unique identifier of clients
        :return: Unique ID for the client
        :rtype: str"""
        return self.__ID
    
    @property
    def name(self):
        return self.__name
    
    @property
    def firstnm(self):
        return self.__firstnm
    
    @property
    def type(self):
        return self.__type
    
    @property
    def req_date(self):
        return self.__req_date
    
    @property
    def req_amount(self):
        return self.__req_amount
    
    @property
    def status(self):
        return self.__status
    
    #Setters
    @ID.setter
    def ID(self, ID):
        self.__ID = ID

    @name.setter
    def name(self, name):
        self.__name = name

    @firstnm.setter
    def firstnm(self, firstnm):
        self.__firstnm = firstnm   

    @req_date.setter
    def req_date(self, req_date):
        self.__req_date = req_date
    
    @req_amount.setter
    def req_amount(self, req_amount):
        self.__req_amount = req_amount

    @status.setter
    def status(self, status):
        self.__status = status

    def __str__(self):
        """
        Method to print PREclient basic information in str
        :return: Name, first name, credit type, request date, request amount, current status
        :rtype: str
        """
        return "Request information of: {}, {} | Credit Type: {} | Required Amount: {} | Status: {}".format(self.__firstnm, self.__name, self.__type, self.__req_amount, self.__status)
    
    def __iter__(self):
        return iter([self.__ID, \
                    self.__name, \
                    self.__firstnm, \
                    self.__type, \
                    self.__req_date, \
                    self.__req_amount, \
                    self.__status])