class Note:
    __title = ""
    __content = ""
    __author = ""
    __month = 0
    __day = 0

    def __init__(self, title, content, author, month, day):
        self.__title = title
        self.__content = content
        self.__author = author
        self.__month = month
        self.__day = day
        print(f"Note: {self.__title} created")

    def __str__(self):
        return f"Title: {self.__title}\nContent: {self.content}\nMonth: {self.month}\nDay: {self.day}"
    
    def getTitle(self):
        return self.__title
    
    def setTitle(self, newTitle):
        if (len(newTitle) > 0 and len(newTitle) <= 30):
            self.__title = newTitle
            return True
        return False

    def getContent(self):
        return self.__content
    
    def setContent(self, newContent):
        if (len(newContent) > 0):
            self.__content = newContent
            return True
        return False

    def getAuthor(self):
        return self.__author

    def getMonth(self):
        return self.__month
    
    def setMonth(self, newMonth):
        if (newMonth > 0 and newMonth <= 12):
            self.__month = newMonth
            return True
        return False
    
    def getDay(self):
        return self.__day
    
    def setDay(self, newDay):
        if (newDay > 0 and newDay <= 31):
            self.__day = newDay
            return True
        return False