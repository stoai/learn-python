#-*- coding: utf-8 -*-
# List Comprehension là dạng cú pháp đặc biệt (syntactic sugar) (mới có từ Python 2.x) 
# cho phép thao tác trên toàn bộ dãy (list) mà không cần viết rõ vòng lặp. 
# Chẳng hạn y là một dãy mà mỗi phần tử của nó bằng bình phương 
# của từng phần tử trong dãy x:

x = [1, 2, 3, 4, 5]

y = [a**2 for a in x]

print y