
class Solution {
    public boolean isValid(String s) {
        Stack<String> stack = new Stack<>();
        for (int i = 0; i < s.length(); i++) {
            if (s.substring(i,i+1).equals("{") || s.substring(i,i+1).equals("[") || s.substring(i,i+1).equals("(")) {
            stack.push(s.substring(i,i+1));
            }
            else {
                if (stack.isEmpty()) {
                    return false;
                }
                else {
                    String l = stack.pop();
                    if (validCheck(l,s.substring(i,i+1))) {
                        continue;
                    }
                    else {
                        return false;
                    }
                }
            }
            
        }
        if (!stack.isEmpty()) {
                return false;
            }
        return true;
        
    }


    public boolean validCheck(String s1, String s2) {
        if (s1.equals("{") && s2.equals("}")) {
            return true;
        }
        else if (s1.equals("[") && s2.equals("]")) {
            return true;
        }
        else if (s1.equals("(") && s2.equals(")")) {
            return true;
        }
        else {
            return false;
        }
    }
}