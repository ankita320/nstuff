class Solution {
    public boolean isPalindrome(String s) {
        String fix = s.replaceAll("[^a-zA-Z0-9]", "").toLowerCase();
        Stack<String> pr = new Stack<>();


        for (int i = 0; i < fix.length(); i++) {
            pr.push(fix.substring(i,i+1));
        }

        for (int i = 0; i < fix.length(); i++) {
            if (!fix.substring(i,i+1).equals(pr.pop())) {
                return false;
            }
        }
         
        
        return true;
        
    }
}
