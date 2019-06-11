class postfixToInfixConversion:

    def __init__(self):
        self.arrExpr = [];
        self.top = -1;
 
    def peek(self):
        return self.arrExpr[self.top];

    def push(self, data):
        self.top += 1;
        self.arrExpr.append(data);

    def pop(self):
        self.top -= 1;
        return self.arrExpr.pop();

    def postfixInfix(self, data):
        for x in data:
            if x.isalpha():
                self.push(x);
            else:
                evalExpress = "("+self.pop()+x+ self.pop()+")";
                self.push(evalExpress);

        return;

expression = 'abc-+de-fg-h+/*';
postfixToInfix = postfixToInfixConversion();
postfixToInfix.postfixInfix(expression);
print("Infix Expression is:", postfixToInfix.peek());

