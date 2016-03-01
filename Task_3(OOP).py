import string
import re
class RegexValidator(object):

    def __init__(self,regex,message):
        self.message = message
        self.regex = regex
    def __call__(self, text):
        self.text = text
        RegexValidator.Validate(self,text)
    def Validate(self,text):
        for text_letter in text:
            validate = False
            for regex_letter in self.regex:
                if (text_letter == regex_letter):
                    validate = True
                else:
                    pass
            if(validate == False):
                print(self.message)
                break
            else:
                pass
        if (validate == True):
            print("This text is valid")
        else:
            pass


validator = RegexValidator(string.ascii_lowercase,"Your input is not valid")
validator('sfasw')
validator('s')
validator('2')

class EmailValidator(RegexValidator):
    def __init__(self):
        RegexValidator.__init__(self, regex='[\w.]+[@][\w.]', message='Enter a valid email')
    def __call__(self, text):
        self.text = text
        if not re.match(self.regex, self.text):
            print (self.massage)
        else:
            print (self.text + ' is valid')

email_validator = EmailValidator("@.","thi is not")
email_validator('jira@name.com')


