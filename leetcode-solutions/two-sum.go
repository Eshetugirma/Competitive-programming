// Time: O(n+n) = O(2n) = O(n)
// Space: O(n)
func twoSum(nums []int, target int) []int {
    // Space: O(n)
    m := make(map[int]int, 0)

    // Time: O(n)
    for idx, num := range nums {
        m[num] = idx
    }

    // Time: O(n)
    for indexX, num := range nums {
        // Time: O(1)
        if indexY, ok := m[target - num]; ok && indexX != indexY {
            return []int{indexX, indexY}
        }
    }

    return []int{}
}