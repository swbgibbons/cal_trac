from Food_Bank import *

if __name__ == '__main__':

    bkfast = sum([coffee,ldu_marco_pollo,
                  reeses_egg*2])
    
    bkfast.name = 'Breakfast'
    
    lunch = sum([red_robins_scorpion_burger,red_robins_yam_fries,
                 lakewood_lager_12oz*2])
    lunch.name = 'Lunch'

    dinner = sum([modelo_24oz*2,buttermilk_sky_pecan_pie])
    dinner.name = 'Dinner'

    net_total = sum([bkfast,lunch,dinner])
    net_total.name = 'Net Total'

print(bkfast)
print(lunch)
print(dinner)
print(net_total)
