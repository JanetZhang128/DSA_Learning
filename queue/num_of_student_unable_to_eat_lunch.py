from collections import Counter

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        res = len(students) # total number of students
        cnt = Counter(students) # count of students preferring each type of sandwich. cnt[0] = # who want 0, cnt[1] = # who want 1
        # Counter is a dict subclass for counting hashable objects, 
        # elements are stored as dictionary keys and their counts/occurrences are stored as dictionary values
        
        for s in sandwiches: #go through sandwiches from the top
            if cnt[s] > 0:  # if there is a student who prefers this type of sandwich
                res -= 1    # one less student unable to eat lunch
                cnt[s] -= 1 # one less student preferring this type of sandwich
            else:
                return res # no student prefers this type of sandwich, stop the process

        return res # the remaining students who were unable to eat lunch