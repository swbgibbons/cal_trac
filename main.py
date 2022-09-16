from Food_Bank import *

if __name__ == '__main__':

    bkfast = sum([coffee,bkfast_burrito,protein_shake,
                  banana,fairlife_choc_milk])
    
    bkfast.name = 'Breakfast'
    
    lunch = sum([chicken_breast_6oz,butter,yams_100g*2,brussels_100g])
    lunch.name = 'Lunch'

    dinner = sum([salmon_4oz,butter/2,white_rice_6oz*2,broccoli_100g,
                  modelo_24oz])
    dinner.name = 'Dinner'

    net_total = sum([bkfast,lunch,dinner])
    net_total.name = 'Net Total'

print(bkfast)
print(lunch)
print(dinner)
print(net_total)
