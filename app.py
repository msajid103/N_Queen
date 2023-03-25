from flask import Flask,render_template
app = Flask(__name__)
class Node:
    def __init__(self,row,column):
        self.row = row    
        self.column = column     
        self.next = None
class Stack:
    def __init__(self):
        self.head = None
    def push(self,row,column):
        new = Node(row,column)      
        new.next = self.head
        self.head = new  
    def pop(self):
        self.head = self.head.next
        self.head.column += 1 
        q.check_position()
        q.addQueen() 
    def isEmpty(self):
        if self.head == None:
            return True
        return False
    def show(self):
        head = self.head
        indexes = []
        while head != None:
            indexes.append((head.row,head.column))
            head = head.next
        return indexes

class Queen:
    def __init__(self,no_of_queen):
        self.no_of_queen = no_of_queen
        if self.no_of_queen < 4:
            print("Enter The Number of Queen Greater Than Three!")
            return     

    def addQueen(self):
        if s.isEmpty():
           return s.push(1,1)
        elif s.head.row < self.no_of_queen:
            s.push(s.head.row+1,1)
            self.check_position()
        else:
            pass
            # print("Exceeded The Value")

    def check_position(self):
        head = s.head.next
        current = s.head
        i = 1        
        while head != None:
            if (current.column == head.column) or (current.column-i == head.column and current.row-i == head.row) or (current.column+i == head.column and current.row-i == head.row):
                current.column += 1 
                self.check_position()                                              
            head = head.next
            i += 1
        if s.head.column > self.no_of_queen:
            s.pop()       

s = Stack()
q = Queen(40)
q.addQueen()
q.addQueen()
q.addQueen()
q.addQueen()


@app.route("/")
def table():
    return render_template("index.html",no_of_queen = q.no_of_queen,indexes = s.show())

if __name__ == '__main__':
    app.run(debug =True)
