#atmexcept.py---file name and acts as module name
class DepositError(Exception):pass

class WithdrawError (BaseException):pass

class InSuffFundError(Exception):pass