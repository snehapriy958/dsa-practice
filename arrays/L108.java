// Platform: LeetCode (108)
// Difficulty: Easy

// Approach: Divide and Conquer / Recursion

// Time Complexity: O(n)

// Space Complexity: O(log n)
// (for recursive stack in balanced BST)

class TreeNode {

    int val;
    TreeNode left;
    TreeNode right;

    TreeNode() {
    }

    TreeNode(int val) {
        this.val = val;
    }

    TreeNode(int val, TreeNode left, TreeNode right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

class Solution {

    public TreeNode sortedArrayToBST(int[] nums) {
        return buildBST(nums, 0, nums.length - 1);
    }

    public TreeNode buildBST(int[] nums, int left, int right) {

        // Base condition
        if (left > right) {
            return null;
        }

        // Find middle index
        int mid = (left + right) / 2;

        // Create root node
        TreeNode root = new TreeNode(nums[mid]);

        // Build left subtree
        root.left = buildBST(nums, left, mid - 1);

        // Build right subtree
        root.right = buildBST(nums, mid + 1, right);

        // Return root node
        return root;
    }
}