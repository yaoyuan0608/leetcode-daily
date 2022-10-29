class Solution:
    def maximumGroups(self, grades: List[int]) -> int:
        grades = sorted(grades)
        count = 0
        start_idx = 0
        
        cur_num = 0
        total_num = len(grades)
        cur_grade = 0
        total_grade = sum(grades)
        
        while total_num >= 0 or total_grade >= 0:
            if total_grade - cur_grade <= 0 or total_num - cur_num <= 0:
                return count
            cur_num += 1
            cur_grade = sum(grades[start_idx:start_idx+cur_num])
            count += 1
            start_idx += cur_num
            total_grade -= cur_grade
            total_num -= cur_num
        return count