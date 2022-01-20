class RunTimeExercises:

    def linearSearch(self, my_list, target):
        """Find target value, return true if exists."""
        for i in range(len(my_list)):
            if my_list[i] == target:
                return True
            #added a comment line
        return False

    def findMax(self, a_list):
        """Return the maximum element from a nonempty Python list."""
        biggest = a_list[0]  # The initial value to beat
        for val in a_list:  # For each value:
            if val > biggest:  # if it is greater than the best so far,
                biggest = val  # we have found a new best (so far)
        return biggest  # When loop ends, biggest is the max

    def prefix_average1(self, a_list):
        """Return list such that, for all j, A[j] equals average of S[0], ..., S[j]."""
        n = len(a_list)
        A = [0] * n  # create new list of n zeros
        for j in range(n):
            total = 0  # begin computing a_list[0] + ... + a_list[j]
            for i in range(j + 1):
                total += a_list[i]
            A[j] = total / (j + 1)  # record the average
        return A

    def prefix_average2(self, a_list):
        """Return list such that, for all j, A[j] equals average of a_list[0], ..., a_list[j]."""
        n = len(a_list)
        A = [0] * n  # create new list of n zeros
        for j in range(n):
            A[j] = sum(a_list[0:j + 1]) / (j + 1)  # record the average
        return A

    def prefix_average(self, a_list):
        """Return list such that, for all j, A[j] equals average of S[0], ..., S[j]."""
        n = len(a_list)
        A = [0] * n  # create new list of n zeros
        total = 0  # compute prefix sum as a_list[0] + a_list[1] + ...
        for j in range(n):
            total += a_list[j]  # update prefix sum to include a_list[j]
            A[j] = total / (j + 1)  # compute average baa_listed on current a_listum
        return A

    def binarySearch(self, data, value, low_index, high_index):
        if low_index > high_index:
            return False
        else:
            mid = (low_index + high_index) // 2
            if value == data[mid]:
                return True
            elif value < data[mid]:
                return self.binarySearch(data, value, low_index, mid - 1)
            else:
                return self.binarySearch(data, value, mid + 1, high_index)
