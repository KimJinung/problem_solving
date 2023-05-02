class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        List<List<Integer>> answer = new ArrayList<>();

        Arrays.sort(nums);

        int givenArrSize = nums.length - 1;

        for (int idx = 0; idx < nums.length; idx++) {
            if (idx > 0 && nums[idx] == nums[idx - 1]) {
                continue;
            }

            int left = idx + 1;
            int right = givenArrSize;

            while (left < right) {
                int sum = nums[idx] + nums[left] + nums[right];

                if (sum < 0) {
                    left += 1;
                } else if (sum > 0) {
                    right -= 1;
                } else {
                    List<Integer> correctCase = new ArrayList<>(Arrays.asList(nums[idx], nums[left], nums[right]));
                    answer.add(correctCase);

                    while (left < right && nums[left] == nums[left + 1]) {
                        left++;
                    }

                    while (left < right && nums[right] == nums[right - 1]) {
                        right--;
                    }

                    left++;
                    right--;
                }
            }
        }
        return answer;
    }
}