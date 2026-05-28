class Solution {
    public int evalRPN(String[] tokens) {

        Stack<Integer> fin = new Stack<>();
        for (int i = 0; i < tokens.length; i++) {
            if (!tokens[i].equals("*") && !tokens[i].equals("+") && !tokens[i].equals("/") && !tokens[i].equals("-")) {
                fin.push(Integer.parseInt(tokens[i]));
            }
            else {
                int p2 = fin.pop();
                int p1 = fin.pop();
                fin.push(operate(tokens[i],p2,p1));
            }

        }
        return fin.pop();
        
    }

    public int operate(String oper, int num1, int num2) {
        if (oper.equals("+")) {
            return num1+num2;
        }
        else if (oper.equals("-")) {
            return num2-num1;
        }
        else if (oper.equals("*")) {
            return num1*num2;
        }
        
            return num2/num1;
        

    }
}
