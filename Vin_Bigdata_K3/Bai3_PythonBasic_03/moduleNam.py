def greeting(name='Hoang', year =2000):
    '''
    Ham chao hoi
    input: ten, nam sinh
    '''
    
    Name = name.upper()
    old =  2022-int(year)
    print(f' Chao Bạn "{Name}" - {old} tuổi!')

greeting('Minh Thang', 2003)
def cal_point(score = [2.5, 8.4, 9.5, 3]):
    print('Diem he 10: {}'.format(score))
    so_mon_hoc = len(score)
    tong = 0.0
    for i in score:
        tong+= i
    avr_score = tong/so_mon_hoc
    print('Diem trung binh he 10: ', avr_score)
    print('Diem trung binh he 4:', avr_score*4/10 )
cal_point([9])
