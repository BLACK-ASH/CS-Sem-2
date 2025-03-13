def prec(e):
    if e == "^":
        return 3
    elif e == "*" or e == "/":
        return 2
    elif e == "-" or e == "+":
        return 1
    else:
        return -1

def postFix(eqn):
    stack = []
    result = ""
    for i in range(len(eqn)):
        e = eqn[i]

        if ("A" <= e <= "Z") or ("a" <= e and e <= "z") or ("9" >= e and e >= "0"):
            result += e

        elif e == "(":
            stack.append(e)
                     
        elif e == ")":
            while stack[-1] != "(":
                result += stack.pop()
            stack.pop()

        else:
            while stack and (prec(stack[-1]) >= prec(e)) :
                result += stack.pop()
            stack.append(e)

    while stack:
        result += stack.pop()
        
    print(result)


eqn = "(9+(A-B)*(A-8)+(C-B)-(7-c))/D"
postFix(eqn)
