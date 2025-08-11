# 1. We have sorted array, we have to return true if there exist a pair of numbers that 
# sum to target

# def check_sum(arr, target):
#     for i in range(len(arr)-1):
#         for j in range(i+1,len(arr)):
#             if arr[i]+arr[j]==target:
#                 print(arr[i])
#                 print(arr[j])
#                 return True
            
# arr = [5, 8, 2, 1, 0, 7, 15]
# res = check_sum(arr,12)
# print(res)

# Above question with sorted array

# def check_sum_for_sorted_arr(arr, target):
#     l=0
#     r=len(arr)-1

#     while(r>l):
#         sum=arr[l]+arr[r]
#         if(target>sum):
#             l+=1
#         elif(target<sum):
#             r-=1
#         else:
#             print(arr[l])
#             print(arr[r])
#             return True
#     return False

# arr = [0,1,2,5,7,9,15]
# res=check_sum_for_sorted_arr(arr,12)
# print(res)

# Remove duplicate from array

# arr=[5,3,2,5,4,3,2,6,7,8,5]
# res=[]
# for i in arr:
#     if i not in res:
#         res.append(i)
# print(res)

# 3 Find out first occurance of substring in a string

# str='Hello all.....Hello world'
# print(str.index("all"))

# 4 Find all occurances of substring in string
# str='Hello all.....Hello world'
# positions=[]
# s=0
# substr="Hello"
# while True:
#     i=str.find(substr,s)
#     if i!=-1:
#         positions.append(i)
#         s=s+len(substr)
#     else:
#         break
# print(positions)

# # 5 Find longest palindrome

# def chk_pal(str,i,j):
#     while(i<j):
#         if str[i]!=str[j]:
#             return False
#         i+=1
#         j-=1
#     return True

# def longest_pal(s):
#     n=len(s)
#     maxlen=1
#     start=0
#     for i in range(n):
#         for j in range(i,n):
#             if chk_pal(s,i,j):
#                 if(j-i+1)>maxlen:
#                     start=i
#                     maxlen=j-i+1
#     return(s[start:start+maxlen])

# s="startraffic"
# print(longest_pal(s))

# 6 reverse words in a string, e.g. "hello all welcome" - o/p - "welcome all hello"

# def reverse_words(str):
#     arr=[]
#     word=" "
#     #read characters
#     for ch in str:
#         if ch==" ":
#             arr.append(word)
#             word=" "
#         else:
#             word+=ch
#     if word:
#         arr.append(word)
#     return " ".join(arr[::-1])  # accessing array elements in reverse order

# str = "hello all welcome"
# print(reverse_words(str))

# 7 print sum of subarray which gives maximum sum, all elements of subarray should be at 
# continuous positions

# def max_subarray(arr):
#     maxsum=arr[0]
#     for i in range(len(arr)):
#         currsum = 0
#         for j in range(i, len(arr)):
#             currsum+=arr[j]
#             maxsum = max(maxsum,currsum)
#     return maxsum

# arr=[-7, 2, 3, -5, 9, -1, 0, 4]
# print(max_subarray(arr))