class Solution {
    public int calPoints(String[] operations) {
        Stack<Integer> stack = new Stack<>();
        for (int i = 0; i < operations.length; i++) {
            if (!operations[i].equals("C") && !operations[i].equals("D") && !operations[i].equals("+")) {
                stack.push(Integer.parseInt(operations[i]));
            }
            else if (operations[i].equals("+")) {
                int p2 = stack.pop();
                int p1 = stack.pop();
                stack.push(p1);
                stack.push(p2);
                stack.push(p2 + p1);
            }
            else if (operations[i].equals("C")) {
                stack.pop();
            }
            else if (operations[i].equals("D")) {
                stack.push(stack.peek()*2);
            }


        }
        int sum = 0;
        while (!stack.isEmpty()) {
            sum += stack.pop();
        }
        return sum;

        
    }
}