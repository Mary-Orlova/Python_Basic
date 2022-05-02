def get_put():
    num_discs = 2 #кол-во
    from_peg = 1 #стержень, с ктр взять
    to_peg = 3 #стержень, на ктр перелдожить
    temp_peg = 2 #временный стержень

    move_discs(num_discs,from_peg,to_peg, temp_peg)
    print('Все диски перемещены')


def move_discs(num,from_peg,temp_peg,to_peg):
    if num > 0:
        move_discs(num-1, from_peg, temp_peg,to_peg)
        print('Переложить диск ',num,'со стержня номер',from_peg,'на стержень номер', to_peg)
        move_discs(num-1,temp_peg,to_peg,from_peg)

get_put()