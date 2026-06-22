class Solution {
    public void rotate(int[] nums, int k) {
        k = k % nums.length;
        while (k>0) {
            int tmp = nums[nums.length-1];
            int i = nums.length-1;
            while (i > 0) { 
                nums[i] = nums[i-1];
                i--;
            }
            nums[0] = tmp;
            k--;
            
            
        }
        
        //while first el is not nums[k]
        //store last item in tmp
        //if i < nums.length-1
        //shift every value to the right by doing nums[i+1] = nums[i]
        //make first el tmp
        
    }
}