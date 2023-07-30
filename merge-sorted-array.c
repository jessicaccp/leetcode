// 88. Merge Sorted Array
// Runtime: 7 ms
// Memory Usage: 6.2 MB
// By https://leetcode.com/jessicaccp/ on Jul 24, 2023

void merge(int* nums1, int nums1Size, int m, int* nums2, int nums2Size, int n){
    int aux_n = n - 1;
    int aux_m = m - 1;
    for (int i = m + n - 1; i >= 0; i--) {
        if (aux_n < 0) {
            nums1[i] = nums1[aux_m];
            aux_m--;
        }
        else if (aux_m < 0) {
            nums1[i] = nums2[aux_n];
            aux_n--;
        }
        else if (nums1[aux_m] >= nums2[aux_n]) {
            nums1[i] = nums1[aux_m];
            aux_m--;
        }
        else {
            nums1[i] = nums2[aux_n];
            aux_n--;
        }
    }
}