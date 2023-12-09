// merge sort in place two sorted ascending arrays
// https://leetcode.com/problems/merge-sorted-array

let nums1 = [0,1,3,10,101,0,0,0,0,0,0,0]
let m = 5
let nums2 = [-14,0,4,7,100,102,1042]
const n = 7

var merge = function(nums1, m, nums2, n) {
    var index = 0;
    for (var i = 0; i < n; i++) {
        for (var j = index; j < m+n; j++) {
            if (nums2[i] < nums1[j]) {
                index = j;
                for (var z = m+n-1; z > j; z--) {
                    nums1[z] = nums1[z-1];
                }
                nums1[j] = nums2[i];
                break;
            }
            else if (j >= m+i) {
                nums1[j] = nums2[i];
                break;
            }
        }
    }
};

merge(nums1, m, nums2, n)
console.log(nums1);
