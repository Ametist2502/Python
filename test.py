def count_vietnamese_characters(input_str):
    telex_mapping = {
        'aw': 'ă',
        'aa': 'â',
        'dd': 'đ',
        'ee': 'ê',
        'oo': 'ô',
        'ow': 'ơ',
        'uw': 'ư',
        'w' : 'ư',
        '[' : 'ơ',
        ']' : 'ư'
    }
    
    count = 0
    i = 0
    while i < len(input_str):
        found = False
        for telex, char in telex_mapping.items():
            if input_str[i:i+len(telex)] == telex:
                count += 1
                i += len(telex)
                found = True
                break
        if not found:
            i += 1
    
    return count

# Test
input_str = input("Nhập chuỗi chữ cái Latin: ")
result = count_vietnamese_characters(input_str)
print("Số lượng chữ cái Tiếng Việt có thể tạo thành: ", result)
