class Solution:
    def countMatches(self, items: list[list[str]], ruleKey: str, ruleValue: str) -> int:
        # Map ruleKey to the corresponding index in each item tuple:
        # items[i] = [type_i, color_i, name_i]
        key_to_index = {
            "type": 0,
            "color": 1,
            "name": 2
        }
        
        target_idx = key_to_index[ruleKey]
        
        # Count items where the attribute at target_idx matches ruleValue
        return sum(1 for item in items if item[target_idx] == ruleValue)
