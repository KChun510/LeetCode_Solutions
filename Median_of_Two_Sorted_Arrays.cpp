class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        nums1.insert(nums1.end(), nums2.begin(), nums2.end()); //Combine both vectors, into one
        sort(nums1.begin(), nums1.end()); //Sort combined vector in ascending order
        
        int size = nums1.size();
        if(size % 2 == 0){
            return (nums1[size/2] + nums1[(size/2) - 1]) / double(2); //If even length vector
        }
        else{
            return(nums1[size/2]); //If odd length vector
        }
    }
};
