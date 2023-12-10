// remove duplicates from sorted array in place
// https://leetcode.com/problems/remove-duplicates-from-sorted-array

public class Solution
{
    public int RemoveDuplicates(int[] nums)
    {
        int duplicates = 0;
        // iterate through the array, shrinking the search area as we find duplicates
        for (int i = 0; i < nums.Length - duplicates - 1;)
        {
            // if the next element is the same as the current one, move all items one step to the left
            if (nums[i] == nums[i + 1])
            {
                // optimization opportunity: since the list is sorted, all duplicates should be next to each other
                // so we could count how many duplicates x there are and then move elements x steps to the left
                for (int j = i + 1; j < nums.Length - duplicates - 1; j++)
                {
                    nums[j] = nums[j + 1];
                }
                duplicates++;
            }
            else
            {
                i++;
            }
        }
        return nums.Length - duplicates;
    }
}
