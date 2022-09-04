dict_ = {'zero' : '0', 'one' : '1', 'two' : '2', 'three' : '3', 'four' : '4', 'five' : '5', 'six' : '6', 'seven' : '7', 'eight' : '8', 'nine' : '9'}

def solution(s):
    answer = ""
    i = 0
    while i < len(s):
        if ord(s[i]) >= 48 and ord(s[i]) <= 57:
            answer += s[i]
        else:
            for key in dict_.keys():
                find_key = key
                if s.find(key, i, i + len(find_key)) != -1:
                    answer += dict_.get(key)
                    i += len(key) - 1
                    break
        i += 1
    return int(answer)


# 다른 방법

# dict_ = {'zero' : '0', 'one' : '1', 'two' : '2', 'three' : '3', 'four' : '4', 'five' : '5', 'six' : '6', 'seven' : '7', 'eight' : '8', 'nine' : '9'}

# def solution(s):
#     answer = s
#     for key, value in dict_.items():
#         answer = answer.replace(key, value)
#     return int(answer)