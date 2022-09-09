class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        groups =  collections.defaultdict(list)
        
        min_atk = 10**5 + 1
        max_atk = 0
        
        for attack, defense in properties:
            min_atk = min(min_atk, attack)
            max_atk = max(max_atk, attack)
            groups[attack].append(defense)
        
        count = 0 
        max_def = -1
        
        for i in range(max_atk, min_atk - 1, -1):
            if groups[i]:
                for defense in groups[i]:
                    if defense < max_def:
                        count += 1
                max_def = max(max_def, max(groups[i]))
        return count
        