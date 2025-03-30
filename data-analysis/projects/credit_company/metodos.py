import subclass as sc
import csv
import pandas as pd
from datetime import datetime

class adminSys:
    def __init__(self):
        self.__customers = [] # We have to create a list for our clients with this we can create our amortization table (will be a Pandas dataframe)
        self.__applicants = []

    @property
    def customers(self):
        return self.__customers
    
    @property
    def applicants(self):
        return self.__applicants
    
    @customers.setter
    def customers(self, customers):
        self.__customers = customers

    @applicants.setter
    def applicants(self, applicants):
        self.__applicants = applicants

#The following methods make work our system.

    def emptyCustomers(self):
        """
        Returns True if the len of the set is empty, in other words if the list Customer is empty
        :return; True if is empty, False in the other way
        :rtype: bool
        """
        return len(self.__customers) == 0
    
        