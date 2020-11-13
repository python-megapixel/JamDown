class Script:
    def __init__(self):
        pass

    def openScripts(self,passedParams)->None:
        try:
            with open("scripts/" + passedParams[0],".js", "r", encoding="utf-8") as template:
                head = "<script>" + template.read() + "</script>" + head
        except FileNotFoundError:
                print("|--- [WARNING] Directive linkScript failed - scriptfile " + passedParams[0] + " not found.")

        return head
        
