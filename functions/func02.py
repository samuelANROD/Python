def student_info(*args, **kwargs):
    print(args) #tuple
    print(kwargs) #dicionarios

#demonstração
#ele imprime separadamente
student_info('math', 'art', name = 'sam', age = 10)