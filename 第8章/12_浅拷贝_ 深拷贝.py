import copy
# 直接赋值
# nums1 = [10,20,30,40]
# nums2 = nums1
# nums2[3] = 99

#浅拷贝
# nums1 = [10,20,30,40]
# nums2 = copy.copy(nums1)
# nums2[3] = 99

#浅拷贝存在的问题
# nums1 =[10,20,30,[40,50]]
# nums2 = copy.copy(nums1)
# nums2[3][0] = 99
# print(nums1[3][0])
# print(nums2[3][0])

#深拷贝
nums1 =[10,20,30,[40,50]]
nums2 = copy.deepcopy(nums1)
nums2[3][0] = 99

print(nums1[3][0])
print(nums2[3][0])

print(id(nums1[3]))
print(id(nums2[3]))

