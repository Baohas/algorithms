def palindrome1(s: str):
    import re #регекс
    cleaned = re.sub(r'[^a-zA-Z]','', s).lower()#убираем все, что не символ алфавита
    return cleaned == cleaned[::-1] #сравниваем

def palindrome2(s: str):
    import re  # регекс
    cleaned = re.sub(r'[^a-zA-Z]', '', s).lower()  # убираем все, что не символ алфавита
    while len(cleaned) > 1:
        if s[cleaned] != cleaned[-1]:
            return False
        cleaned = cleaned[1:-1]
    return True

