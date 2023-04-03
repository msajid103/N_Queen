from flask import Flask,render_template, request, redirect
app = Flask(__name__)
class Node:
    def __init__(self,row,column):
        self.row = row    
        self.column = column     
        self.next = None
class Stack:
    def __init__(self):
        self.head = None
        self.indexes = []

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
        self.indexes.clear()
        while head != None:
            self.indexes.append((head.row,head.column))
            head = head.next

class Queen:
    def __init__(self,n=0):
        self.no_of_queen = n      

    def addQueen(self):
        if s.isEmpty():
            s.push(1,1)
            s.show()
        elif s.head.row < self.no_of_queen:
            s.push(s.head.row+1,1)
            self.check_position()
            s.show()

      

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
q = Queen()


@app.route('/')
def index():  
    return render_template("index.html")

@app.route("/g", methods = ['POST','GET'])
def game():
    if request.method == 'POST':        
        numb = request.form["number"]
        
        if numb != '' and int(numb) > 3:
            q.no_of_queen = int(numb)
            s.head = None
            s.indexes.clear()
        else:
            return render_template("game.html", no_of_queen = q.no_of_queen,err = True, indexes = s.indexes)            
    return render_template("game.html", no_of_queen = q.no_of_queen, indexes = s.indexes)

@app.route("/add", methods = ['GET','POST'])
def add():
    q.addQueen()
    if s.head.row >= q.no_of_queen:
        return render_template("game.html", no_of_queen = q.no_of_queen,tr = True ,indexes = s.indexes)      
    return render_template("game.html", no_of_queen = q.no_of_queen, indexes = s.indexes)

@app.route("/reset", methods = ['GET','POST'])
def reset():
    s.head = None
    s.indexes.clear()
    return render_template("game.html", no_of_queen = q.no_of_queen, indexes = s.indexes) 

    

if __name__ == '__main__':
    app.run(debug =True)
