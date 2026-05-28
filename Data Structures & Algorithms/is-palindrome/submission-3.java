class Solution {
    public boolean isPalindrome(String s) {
        String fix = s.replaceAll("[^a-zA-Z0-9]", "").toLowerCase();

        int end = fix.length()-1;
        int start = 0;
        for (int i = 0; i <= end; i++) {
            if (!fix.substring(i,i+1).equals(fix.substring(end,end+1))) {
                return false;
            }
            end = end-1;
        }

         
        
        return true;
        
    }
}
