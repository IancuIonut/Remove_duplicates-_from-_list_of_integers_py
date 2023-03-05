
def removeDuplicates(nums):
    if not nums:
        return 0
    nums.sort() # Sort the list in non-decreasing order
    slow = 0    # Initialize a slow pointer at the beginning of the list
    for fast in range(1, len(nums)): # Loop through the list using a fast pointer
        if nums[fast] != nums[slow]: # If the current element is not a duplicate, move the slow pointer one position to the right
# and copy the current element to the slow pointer position
            slow += 1
            nums[slow] = nums[fast]

    return slow + 1 # Return the length of the new list

while True: #Loop to take user input and remove duplicates
    nums = list(map(int, input("Enter a list of integers separated by space (press q to quit): ").split())) # Prompt the user to enter a list of integers separated by space
    if nums[0] == 'q': # Break out of the loop if the user enters 'q'
        break
    k = removeDuplicates(nums) 
    print(nums[:k]) # Print the first k elements of the list, which contain the unique elements in non-decreasing order
    print()