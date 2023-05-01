import java.util.HashMap;

class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> memory = new HashMap<>();

        int[] result = new int[2];

        for (int idx = 0; idx < nums.length; idx++) {
            Integer targetNum = target - nums[idx];

            if (memory.containsKey(targetNum)) {
                result[0] = memory.get(targetNum);
                result[1] = idx;
                break;
            }

            memory.put(nums[idx], idx);
        }
        return result;
    }
}