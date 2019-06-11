class prefixToInfixConversion:

    def __init__(self):
        self.arrExpr = [];
        self.top = -1;
        self.expression = '*-A/BC-/AKL';

    def peek(self):
        return self.arrExpr[self.top];

    def push(self, data):
        self.top += 1;
        self.arrExpr.append(data);

    def pop(self):
        self.top -= 1;
        return self.arrExpr.pop();

    def prefixInfix(self):
        expressionRev = reversed(self.expression);
        for x in expressionRev:
            if x.isalpha():
                self.push(x);
            else:
                evalExpress = "("+self.pop()+x+ self.pop()+")";
                self.push(evalExpress);

        return;

prefixToInfix = prefixToInfixConversion();
prefixToInfix.prefixInfix();
print("Infix Expression is:", prefixToInfix.peek());

