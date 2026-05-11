/*     
Problem: 2553. Separate the Digits in an Array
Platform: LeetCode (2553)
Difficulty: Easy
Approach: String Conversion and List Accumulation
Time Complexity: O(n * m) where n is the number of elements in the input array and m is the average number of digits in each number
Space Complexity: O(n * m) for the list that stores the separated digits
*/

import java.util.ArrayList; 

class L2553 {
  public int[] separateDigits(int[] nums) {
    ArrayList<Integer> ans = new ArrayList<>();

    for (final int num : nums)
      for (final char c : String.valueOf(num).toCharArray())
        ans.add(c - '0');

    return ans.stream().mapToInt(Integer::intValue).toArray();
  }
}