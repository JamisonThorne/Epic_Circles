from __future__ import annotations

def get_unique_array(circle_array):
        unique_list = []
        for item in circle_array:
            if item not in unique_list:
                unique_list.append(item)
        return unique_list