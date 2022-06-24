
class FoodValues:
    def __init__(self, name, fat, carbs, protein, serv_size,calories=None):
        self.name = name
        self.fat = fat
        self.carbs = carbs
        self.protein = protein
        self.serv_size = serv_size
        # Automatically compute calories if caller doesn't override
        if calories is None:
            calories = 9 * fat + 4 * carbs + 4 * protein
        self.calories = calories

    # + operator
    def __add__(self, other):
        
        # Simplifies using the sum function
        if other == 0:
            return self

        # Other than 0, food values can only be added with other food values
        if not isinstance(other, type(self)):
            return NotImplemented
        

        return FoodValues(
            f'{self.name} + {other.name}',
            self.fat + other.fat,
            self.carbs + other.carbs,
            
            self.protein + other.protein,
            self.serv_size + other.serv_size,
            self.calories + other.calories,
        )


    # Allow addition in any order
    def __radd__(self, other):
        return self.__add__(other)

    # * operator
    def __mul__(self, other):
        if other == 0:
            return 0

        # Other than 0, food values can only be multiplied by an int
        if not isinstance(other, int):
            return NotImplemented

        selfname = self.name
        if '+' in selfname:
            # Quick and dirty grouping symbol
            selfname = f'({selfname})'

        return FoodValues(
            f'{other} {selfname}',
            self.fat * other,
            self.carbs * other,
            self.protein * other,
            self.serv_size * other,
            self.calories * other,
        )

        # * operator
    def __truediv__(self, other):
        if other == 0:
            return 0

        # Other than 0, food values can only be divided by an int
        if not isinstance(other, int):
            return NotImplemented

        selfname = self.name
        if '+' in selfname:
            # Quick and dirty grouping symbol
            selfname = f'({selfname})'

        return FoodValues(
            f'{other} {selfname}',
            self.fat / other,
            self.carbs / other,
            self.protein / other,
            self.serv_size / other,
            self.calories / other,
        )

    # Allow multiplication in any order
    def __rmul__(self, other):
        return self.__mul__(other)
    
    def __rdiv__(self, other):
        return self.__div__(other)

    def __str__(self):
        return ' '.join([
            f'{self.name}:',
            f'{self.calories} calories,',
            f'{self.fat} g fat,',
            f'{self.carbs} g carbs,',
            f'{self.protein} g protein',
        ])
    


if __name__ == '__main__':
    #Pantry Items
    egg = FoodValues('Egg', calories=72, fat=5, carbs=0, protein=6, serv_size=50)
    cheese = FoodValues('Cheese', calories=90, fat=7, carbs=0, protein=5, serv_size=24)
    butter = FoodValues('Butter', calories=100, fat=14, carbs=0, protein=0,serv_size=14)
    bacon_grease = FoodValues('Bacon Grease', calories=116, fat=14, carbs=0, protein=0,serv_size=14)
    bacon = FoodValues('Bacon', calories=45, fat=3, carbs=0, protein=3, serv_size=8)
    oats = FoodValues('Oatmeal', calories=140, fat=0, carbs=25, protein=5, serv_size=40)
    corn_tortilla = FoodValues('Corn tortilla', calories=130, fat=5, carbs=17, protein=2, serv_size=28)
    coffee = FoodValues('Coffee', calories=5, fat=0, carbs=0, protein=0, serv_size=12)
    dkb_slice = FoodValues('Corn tortilla', calories=110, fat=1, carbs=22, protein=5, serv_size=45)
    wc_peanut_butter = FoodValues('White Chocolate Peanut Butter', calories=180, fat=18, carbs=2, protein=7, serv_size=32)
    banana = FoodValues('Banana', calories=105, fat=1, carbs=25, protein=1, serv_size=106)
    blood_orange = FoodValues('Blood Orange', calories=70, fat=1, carbs=15, protein=1, serv_size=75)
    dkb_slice = FoodValues('DKB bread slice', calories=110, fat=1, carbs=22, protein=5, serv_size=45)
    mission_corn_tortillas = FoodValues('Corn tortilla', calories=100, fat=1, carbs=21, protein=2, serv_size=30)
    protein_shake = FoodValues('Protein Shake', calories=110, fat=0, carbs=0, protein=25, serv_size=12)
    powercrunch_kids = FoodValues('Powercrunch Kids protein Bar', calories=180, fat=12, carbs=8, protein=10, serv_size=32)
    lays_dill_chips = FoodValues('Lay\'s Dill Pickle Chips', calories=150, fat=10, carbs=16, protein=2, serv_size=28)
    diet_dp = FoodValues('Diet Dr Pepper', calories=0, fat=0, carbs=0, protein=0, serv_size=12)
    fairlife_choc_milk = FoodValues('Fairlife Chocolate Milk', calories=140, fat=6, carbs=13, protein=13,serv_size=8)

    #Whole Foods
    wf_hemp_protein = FoodValues('WF Hemp Protein', calories=110, fat=3, carbs=8, protein=15, serv_size=30)
    wf_oat_protein_bites = FoodValues('WF Oat Protein Bites', calories=160, fat=7, carbs=23, protein=6, serv_size=40)
    wf_multi_seed_bread = FoodValues('WF Multi Seed Bread Slice', calories=90, fat=2, carbs=16, protein=4, serv_size=33)
    coco_water_8oz = FoodValues('WF Coco Water', calories=50, fat=0, carbs=13, protein=0, serv_size=8)
    wf_jap_hummus = FoodValues('WF Jap Hummus', calories=70, fat=5, carbs=5, protein=2, serv_size=30)

    #WF Hot Bar
    wf_meatball_marinara = FoodValues('WF Meatball Marinara', calories=180, fat=11, carbs=11, protein=12, serv_size=112)
    wf_butternut_lasagna = FoodValues('WF Hemp Protein', calories=320, fat=15, carbs=34, protein=13, serv_size=253)
    wf_paleo_brussels = FoodValues('WF Hemp Protein', calories=250, fat=11, carbs=16, protein=9, serv_size=72)

    #McDonalds
    mcdonalds_big_mac = FoodValues("Mcd Big Mac", calories=550, fat=30, carbs=45, protein=25, serv_size=300)
    mcdonalds_med_fries = FoodValues("Mcd Med Fries", calories=320, fat=15, carbs=43, protein=5, serv_size=200)
    mcdonalds_sweet_n_sour = FoodValues("Mcd Sweet and Sour", calories=48, fat=0, carbs=11, protein=0, serv_size=28)
    mcdonalds_ssg_egg_chz_mcgriddle = FoodValues("Mcd McGriddle", calories=550, fat=13, carbs=33, protein=19, serv_size=230)
    mcdonalds_hash_brown = FoodValues("Mcd Hashbrown", calories=140, fat=8, carbs=18, protein=2, serv_size=100)
    mcdonalds_slushie = FoodValues("Mcd Sweet and Sour", calories=240, fat=0, carbs=64, protein=0, serv_size=16)

    
    #Hu Kitchen Chocolate Bars
    hu_kitchen_almond_crunch = FoodValues('Hu Kitchen Almond Crunch Bar', calories=380, fat=24, carbs=26, protein=6, serv_size=60)
    hu_kitchen_orange_vanilla = FoodValues('Hu Kitchen Orange Vanilla Bar', calories=360, fat=26, carbs=28, protein=6, serv_size=60)

    #Social Nights (lolz)
    omi_night_out = FoodValues('Omi Night Out', calories=1500, fat=65, carbs=45, protein=42, serv_size=215)
    omi_night_out_alcohol = FoodValues('Omi Night Out Alcohol', calories=1000, fat=0, carbs=65, protein=0, serv_size=115)

    #Andy's Custard (peanut butter something med; 1700 cal)
    andys_jbj = FoodValues('Andy\'s James Brown Jackhammer w Reeses', calories=1700, fat=115, carbs=162, protein=39, serv_size=350)
    
    #Tacos Azteca (Sope de carnita, gordita de rajas con queso)
    tacos_azteca_sope = FoodValues('Tacos Azteca Sope', calories=400, fat=24, carbs=35, protein=18, serv_size=150)
    tacos_azteca_gordita = FoodValues('Tacos Azteca Gordita', calories=200, fat=12, carbs=20, protein=6, serv_size=58)
    tacos_azteca_tacos = FoodValues('Tacos Azteca Tacos', calories=220, fat=13, carbs=22, protein=7, serv_size=68)

    #MP Proteins
    ny_strip_1oz = FoodValues('NY Strip 1oz serving', calories=55, fat=3, carbs=0, protein=8, serv_size=28)
    ny_strip_6oz = FoodValues('NY Strip 6oz serving', calories=330, fat=18, carbs=0, protein=48, serv_size=168)
    prolific_beef_round_5oz = FoodValues('Beef Round 5oz serving', calories=267, fat=8, carbs=0, protein=45, serv_size=224)
    prolific_beef_round_8oz = FoodValues('Beef Round 8oz serving', calories=427, fat=13, carbs=0, protein=72, serv_size=224)
    salmon_1oz = FoodValues('Salmon 1oz', calories=38, fat=1, carbs=0, protein=6, serv_size=28)
    salmon_4oz = FoodValues('Salmon 4oz', calories=150, fat=5, carbs=0, protein=25, serv_size=113)
    chicken_breast_1oz = FoodValues('Chicken Breast 1oz serving', calories=55, fat=2, carbs=0, protein=8, serv_size=28)
    chicken_breast_6oz = FoodValues('Chicken Breast 6oz serving', calories=330, fat=12, carbs=0, protein=48, serv_size=168)
    chicken_thigh_1oz = FoodValues('Chicken Thigh 1oz serving', calories=47, fat=3, carbs=0, protein=5, serv_size=28)
    chicken_thigh_6oz = FoodValues('Chicken Thigh 6oz serving', calories=318, fat=12, carbs=0, protein=30, serv_size=168)
    mahi_mahi_4oz = FoodValues('Chicken Thigh 6oz serving', calories=100, fat=1, carbs=0, protein=22, serv_size=112)
    beef_chorizo = FoodValues('Beef Chorizo 3.5oz', calories=350, fat=35, carbs=7, protein=8, serv_size=99)
    chicken_wings_4oz = FoodValues('Chicken Wings 4oz', calories=210, fat=14, carbs=0, protein=20, serv_size=112)

    #MP sides
    white_rice_6oz = FoodValues('White Rice 6oz', calories=170, fat=0, carbs=38, protein=4, serv_size=170)

    #Whippin da kitchen
    pesto_paste = FoodValues('Pesto Paste', calories=230, fat=23, carbs=6, protein=3, serv_size=52)
    chickpea_pasta = FoodValues('Chickpea Pasta', calories=190, fat=3, carbs=35, protein=11, serv_size=56)
    chicken_stock = FoodValues('Chicken Stock', calories=50, fat=0, carbs=0, protein=6, serv_size=240)
    sweet_onion = FoodValues('Sweet Onion', calories=47, fat=0, carbs=11, protein=1, serv_size=148)
    shallot = FoodValues('Shallot', calories=72, fat=0, carbs=17, protein=2, serv_size=100)
    lite_brown_sugar = FoodValues('Lite Brown Sugar 100g', calories=363, fat=0, carbs=96, protein=0, serv_size=100)
    soy_sauce = FoodValues('Soy Sauce 8oz', calories=150, fat=0, carbs=16, protein=0, serv_size=8)
    bosc_pear = FoodValues('Bosc Pear', calories=100, fat=0, carbs=26, protein=0, serv_size=200)
    thai_chili_sauce = FoodValues('Sweet Thai Chili Sauce', calories=50, fat=0, carbs=12, protein=0, serv_size=33
    )

    #MP Veg
    yams_100g = FoodValues('Yams 100 grams', calories=86, fat=0, carbs=20, protein=2, serv_size=100)
    asparagus_85g = FoodValues('Asparagus 85g', calories=20, fat=0, carbs=3, protein=3, serv_size=85)
    brussels_100g = FoodValues('Brussels 100g', calories=38, fat=0, carbs=9, protein=3, serv_size=100)
    broccoli_100g = FoodValues('Broccoli 100g', calories=35, fat=0, carbs=7, protein=2, serv_size=100)
    cottage_chz_110g = FoodValues('Cottage Cheese 110g', calories=130, fat=7, carbs=3, protein=14, serv_size=110)
    blueberries_140g = FoodValues('Blueberry 140g', calories=70, fat=0, carbs=18, protein=1, serv_size=140)
    mango_chunks_140g = FoodValues('Frozen Mango 140g', calories=80, fat=0, carbs=21, protein=1, serv_size=140)
    avo_chunks_50g = FoodValues('Avocado Chunks 50g', calories=50, fat=4.5, carbs=3, protein=1, serv_size=50)
    bell_pepper_medley_85g = FoodValues('Bell Peppers 85g', calories=40, fat=0, carbs=4, protein=0, serv_size=85)
    euro_greens_110g = FoodValues('European Greens 110g', calories=90, fat=6, carbs=8, protein=3, serv_size=110)

    #Fried Chicken
    angels_chkn_hill_country = FoodValues('Angel\'s Chicken Hill Country Biscuit', calories=800, fat=58, carbs=68, protein=28, serv_size=324)

    #Arlington
    biscuit_bar_hoss_biscuit = FoodValues('Biscuit Bar HOSS Biscuit', calories=900, fat=46, carbs=68, protein=28, serv_size=225)
    biscuit_bar_southern_tots = FoodValues('Biscuit Bar Southern Tots', calories=600, fat=28, carbs=52, protein=7, serv_size=175)
    biscuit_bar_tipsy_joe = FoodValues('Biscuit Bar Tipsy Joe', calories=275, fat=11, carbs=15, protein=3, serv_size=14)

    #Chain Food
    fuzzys_taco_bkfast_combo = FoodValues('Fuzzy\'s Breakfast Combo', calories=1200, fat=55, carbs=75, protein=35, serv_size=650)
    fuzzys_fried_avocado_taco = FoodValues('Fuzzy\'s Fried Avocado taco', calories=250, fat=15, carbs=28, protein=8, serv_size=165)
    fuzzys_fried_shrimp_taco = FoodValues('Fuzzy\'s Baja Shrimp taco', calories=380, fat=22, carbs=39, protein=22, serv_size=184)
    fuzzys_marg = FoodValues('Fuzzy\'s Margarita', calories=160, fat=0, carbs=18, protein=0, serv_size=16)
    shake_shack_dbl_smoke_shack = FoodValues('Shake Shack Double Smoke Shack', calories=830, fat=53, carbs=28, protein=58, serv_size=300)
    shake_shack_crinkle_fries = FoodValues('Shake Shack Crinkle Fries', calories=470, fat=22, carbs=63, protein=7, serv_size=250)

    #Chik_fila
    chik_fila_biscuit = FoodValues('Chik Fila Biscuit', calories=460, fat=23, carbs=45, protein=19, serv_size=200)
    chik_fila_hash_browns = FoodValues('Chik Fila Hash Browns', calories=270, fat=18, carbs=23, protein=3, serv_size=100)
    chik_fila_filet = FoodValues('Chik Fila Filet', calories=250, fat=12, carbs=12, protein=24, serv_size=75)
    chik_fila_frosted_lemonade = FoodValues('Chik Fila Frosted Lemonade', calories=330, fat=6, carbs=65, protein=6, serv_size=14)
    chik_fila_sauce = FoodValues('Chik Fila Sauce', calories=140, fat=13, carbs=7, protein=0, serv_size=28)
    chik_fila_bbq_sauce = FoodValues('Chik Fila BBQ Sauce', calories=45, fat=0, carbs=11, protein=0, serv_size=28)
    chik_fila_sriracha = FoodValues('Chik Fila Sriracha Sauce', calories=45, fat=0, carbs=11, protein=0, serv_size=28)
    
    #Starbucks
    starbs_cinn_coffee_cake = FoodValues('Starbucks Cinnamon Coffee Cake', calories=330, fat=15, carbs=43, protein=4, serv_size=106)
    
    #Snacks
    reeses_sticks = FoodValues('Reese\'s Sticks', calories=220, fat=13, carbs=23, protein=4, serv_size=42)
    reeses_egg = FoodValues('Reese\'s Sticks', calories=180, fat=11, carbs=19, protein=3, serv_size=34)
    m_m_cookie = FoodValues('M&M Cookie', calories=80, fat=6, carbs=12, protein=2, serv_size=25)
    reeses_crunchy_pb_bar = FoodValues('Reese\'s Crunchy PB Bar', calories=510, fat=36, carbs=36, protein=15, serv_size=90)
    reeses_fast_break_king_size = FoodValues('Reese\'s Fast Break King Size', calories=450, fat=21, carbs=63, protein=9, serv_size=99)
    cool_ranch_doritos = FoodValues('Cool Ranch Doritos', calories=150, fat=8, carbs=18, protein=2, serv_size=28)
    jap_cheetos = FoodValues('Jalapeno Cheets', calories=160, fat=9, carbs=17, protein=4, serv_size=28)
    negritos = FoodValues('Negritos Two Pack', calories=520, fat=20, carbs=76, protein=6, serv_size=124)
    costco_walkers = FoodValues('Walkers Cookies', calories=190, fat=11, carbs=22, protein=3, serv_size=37)
    qt_jap_cheddar_hot_dog = FoodValues('QT Jalapeno Hot Dog', calories=400, fat=26, carbs=22, protein=12, serv_size=42)
    protein_gatorade = FoodValues('Gatorade with Protein', calories=50, fat=0, carbs=1, protein=10, serv_size=500)
    ruffles_sour_cream_cheddar_chips = FoodValues('Ruffles Sour Cream and Cheddar chips', calories=160, fat=10, carbs=15, protein=2, serv_size=28)
    goldfish_flavor_blasted = FoodValues('Goldfish Pizza Flavor Blasted', calories=140, fat=5, carbs=21, protein=3, serv_size=30)

    #Desserts
    bnj_everything_but_the = FoodValues('Ben and Jerry\'s EBTKS', calories=1250, fat=78, carbs=119, protein=21, serv_size=441)
    chocolate_froyo = FoodValues('Chocolate FroYo', calories=300, fat=28, carbs=42, protein=6, serv_size=188)
    milk_and_cream_donut = FoodValues('Milk and Cream Donut', calories=800, fat=42, carbs=68, protein=7, serv_size=245)
    yoyo_cake = FoodValues('Yoyo Cake', calories=300, fat=16, carbs=38, protein=4, serv_size=175)
    choc_chip_cookie = FoodValues('Chocolate Chip Cookie', calories=200, fat=13, carbs=28, protein=5, serv_size=26)
    tiramisu = FoodValues('Tiramisu', calories=500, fat=22, carbs=36, protein=8, serv_size=78)
    tiffs_treats_choc_pb_brownie = FoodValues('Tiff\'s Treats Chocolate Peanut Butter Brownie a la mode', calories=900, fat=50, carbs=112, protein=16, serv_size=300)
    reeses_heart = FoodValues('Reeses Valentine Heart', calories=700, fat=40, carbs=85, protein=15, serv_size=140)
    blue_bell_two_step = FoodValues('Blue Bell Two Step Nutrition', calories=250, fat=11, carbs=33, protein=5, serv_size=102)
    buttermilk_sky_pecan_pie = FoodValues('Buttermilk Sky Pie Shop', calories=450, fat=18, carbs=38, protein=6, serv_size=150)
    
    #Alcohol
    hendricks_soda = FoodValues('Hendrick\'s and soda', calories=185, fat=0, carbs=11, protein=0, serv_size=16)
    tx_sour = FoodValues('Texas Sour', calories=240, fat=0, carbs=16, protein=0, serv_size=14)
    atlas_japan_layover = FoodValues('Atlas Jap Bourbon and Beer', calories=340, fat=0, carbs=34, protein=0, serv_size=30)
    blue_cenote_marg_beer = FoodValues('BN Beer Rita', calories=300, fat=0, carbs=35, protein=0, serv_size=36)
    woodford_reserve = FoodValues('Woodford Reserve 1.5oz', calories=110, fat=0, carbs=0, protein=0, serv_size=1.5)

    #Blue Cenote
    blue_cenote_marg_beer = FoodValues('BN Beer Rita', calories=300, fat=0, carbs=35, protein=0, serv_size=36)
    blue_cenote_guac_n_chips = FoodValues('BN Guac and Chips', calories=500, fat=28, carbs=45, protein=3, serv_size=225)

    #Costco
    costco_hot_dog = FoodValues('Costco Hot Dog', calories=600, fat=33, carbs=54, protein=24, serv_size=145)

    #Pizza
    yonkers_aikman_slice = FoodValues('Yonkers Aikman slice', calories=500, fat=24, carbs=38, protein=26, serv_size=125)
    enos_supreme = FoodValues('Enos Supreme Pizza Whole', calories=1200, fat=52, carbs=74, protein=35, serv_size=675)
    cane_rosso_gemma = FoodValues('Cane Rosso Gemma Pizza Whole', calories=1150, fat=48, carbs=68, protein=32, serv_size=650)
    papa_johns_pepp_pizza = FoodValues('Papa John\'s Pepperoni Pizza Slice', calories=320, fat=15, carbs=37, protein=15, serv_size=123)

    #La Reunion
    croissant = FoodValues('La Reunion Croissant', calories=500, fat=19, carbs=42, protein=7, serv_size=140)
    old_fashioned = FoodValues('La Reunion Old Fashioned', calories=200, fat=0, carbs=16, protein=0, serv_size=10)

    #Emporium Pies
    cookie_cream_pie_ala_mode = FoodValues('Cookie cream pie a la mode', calories=1200, fat=64, carbs=75, protein=16, serv_size=450)
    drunken_nut_ala_mode = FoodValues('Drunken Nut Pie a la mode', calories=1100, fat=58, carbs=72, protein=25, serv_size=500)

    #BBQ Babyyyy
    jambos_two_meat = FoodValues('Jambos Brisket and Rib combo', calories=2000, fat=85, carbs=65, protein=54, serv_size=400)
    
    #Coffee Shop
    wrc_white_rocker = FoodValues('White Rock Coffee White Rocker (half pumps, xtra shot)', calories=425, fat=15, carbs=26, protein=5, serv_size=16)
    wrc_dirty_chai = FoodValues('White Rock Coffee Dirty Chai)', calories=500, fat=17, carbs=32, protein=6, serv_size=16)
    wrc_bkfast_brioche = FoodValues('White Rock Coffee Bkfast Brioche Bun', calories=575, fat=28, carbs=45, protein=22, serv_size=265)
    wrc_bkfast_strata = FoodValues('White Rock Coffee Bkfast Brkfast Strata', calories=700, fat=26, carbs=38, protein=16, serv_size=195)
    ham_n_chz_cxt = FoodValues('Ham and Chz Cxt', calories=500, fat=24, carbs=36, protein=12, serv_size=220)
    ldu_marco_pollo = FoodValues('LDU Marco Pollo', calories=600, fat=28, carbs=45, protein=25, serv_size=225)


    #Mom Food
    burrito_de_carne = FoodValues('Burrito de Carne', calories=700, fat=28, carbs=42, protein=35, serv_size=240)
    green_chkn_tamale = FoodValues('Green Chicken Tamale', calories=215, fat=11, carbs=19, protein=10, serv_size=115)
    rajas_con_queso_tamale = FoodValues('Rajas con queso Tamale', calories=180, fat=28, carbs=8, protein=21, serv_size=112)
    pork_posole = FoodValues('Pork Posole', calories=400, fat=15, carbs=35, protein=24, serv_size=250)
    enchidladas_entomatadas = FoodValues('Enchiladas Entomatadas', calories=375, fat=21, carbs=35, protein=16, serv_size=125)
    helado_d_pinon = FoodValues('Pinon Ice Cream', calories=250, fat=21, carbs=32, protein=8, serv_size=160)

    #Longhorn Steakhouse
    titos_tx_tea = FoodValues('Texas Tea', calories=240, fat=0, carbs=35, protein=0, serv_size=16)
    chop_steak = FoodValues('Chop Steak', calories=640, fat=13, carbs=46, protein=44, serv_size=325)
    asparagus_spears = FoodValues('Asparagus Spears', calories=150, fat=7, carbs=9, protein=8, serv_size=168)
    loaded_baked_potato = FoodValues('Loaded Baked Potato', calories=470, fat=20, carbs=65, protein=11, serv_size=285)

    #Ramen
    ninja_spicy_ramen = FoodValues('Ninja Spicy Ramen', calories=1500, fat=42, carbs=74, protein=28, serv_size=450)
    jinga_tonkotsu_og = FoodValues('Jinga Tonkotsu Ramen', calories=1320, fat=72, carbs=111, protein=54, serv_size=500)

    #Tacos
    tacos_el_si_hay = FoodValues('Tacos El Si Hay', calories=200, fat=9, carbs=22, protein=12, serv_size=28)
    tacos_el_chilango = FoodValues('Tacos El Chilango', calories=150, fat=10, carbs=11, protein=9, serv_size=22)
    quesadilla_el_chilango = FoodValues('Quesadilla El Chilango', calories=360, fat=18, carbs=19, protein=21, serv_size=49)
    eloto_el_chilango = FoodValues('Elote El Chilango', calories=500, fat=22, carbs=58, protein=3, serv_size=45)

    #Dallas Royal Lane
    no_one_plus_yangyum_wings = FoodValues('No 1 Plus Yangyum wings', calories=1600, fat=75, carbs=55, protein=45, serv_size=800)
    no_one_plus_yam_fries = FoodValues('No 1 Plus Yam Fries', calories=600, fat=28, carbs=64, protein=7, serv_size=500)

    #Thai
    royal_thai_spicy_noodles = FoodValues('RT Spicy Noodles', calories=950, fat=38, carbs=72, protein=29, serv_size=520)
    saucys_spicy_noodles = FoodValues('Saucys Spicy Noodles', calories=1000, fat=36, carbs=68, protein=28, serv_size=700)

    #Uptown
    crimson_cafe_bahn_mi = FoodValues('Crimson Cafe Bahn Mi', calories=600, fat=20, carbs=50, protein=50, serv_size=334)

    #Shug's Bagels
    shugs_bacon_egg_chz_bagel = FoodValues('Shug\'s Bagel', calories=800, fat=26, carbs=58, protein=26, serv_size=250)
    shugs_spicy = FoodValues('Shug\'s Spicy Bagel', calories=950, fat=32, carbs=68, protein=28, serv_size=275)
    shugs_russian_cutlet_bagel = FoodValues('Shug\'s Bagel', calories=1000, fat=45, carbs=55, protein=40, serv_size=250)
    shugs_pesto_cutlet_bagel = FoodValues('Shug\'s Bagel', calories=1000, fat=38, carbs=60, protein=42, serv_size=250)
    shugs_reuben_bagel = FoodValues('Shug\'s Bagel', calories=1200, fat=45, carbs=70, protein=38, serv_size=275)
    shugs_potato_salad = FoodValues('Shug\'s Bagel', calories=300, fat=15, carbs=36, protein=5, serv_size=125)

    #Burgers
    lakewood_landing_burger = FoodValues('Lakewood Landing Burger', calories=1000, fat=42, carbs=56, protein=28, serv_size=380)
    lakewood_landing_onion_rings = FoodValues('Lakewood Landing Onion Rings', calories=600, fat=38, carbs=54, protein=9, serv_size=250)
    smashburger_classic = FoodValues('SmashBurger Classic Burger', calories=640, fat=20, carbs=42, protein=30, serv_size=300)
    smashburger_yam_fries = FoodValues('SmashBurger Yam Fries', calories=440, fat=15, carbs=65, protein=4, serv_size=200)
    red_robins_scorpion_burger = FoodValues('Red Robin\'s Scorpion Burger', calories=950, fat=57, carbs=67, protein=43, serv_size=300)
    red_robins_yam_fries = FoodValues('Red Robin\'s Yam Fries', calories=460, fat=23, carbs=60, protein=4, serv_size=250)

    #Loro
    loro_sesame_rice_noodz = FoodValues('Loro Sesame Rice Noodles', calories=400, fat=12, carbs=45, protein=6, serv_size=175)
    loro_brisket_curry_fried_rice = FoodValues('Loro Brisket Curry Fried Rice', calories=600, fat=22, carbs=52, protein=16, serv_size=250)
    loro_brisket_sandwich = FoodValues('Loro Brisket Sandwich', calories=800, fat=45, carbs=38, protein=25, serv_size=375)
    loro_ribs = FoodValues('Loro Ribs', calories=900, fat=58, carbs=12, protein=46, serv_size=540)
    loro_turkey = FoodValues('Loro Turkery', calories=650, fat=32, carbs=7, protein=35, serv_size=224)
    loro_potatoes = FoodValues('Loro Potatoes w Ailoi', calories=600, fat=32, carbs=45, protein=8, serv_size=215)
    loro_zucchini = FoodValues('Loro Oak Zucchini', calories=300, fat=16, carbs=34, protein=5, serv_size=320)
    loro_g_and_t = FoodValues('Loro Gin & tonic', calories=150, fat=0, carbs=14, protein=0, serv_size=14)
    loro_swirl = FoodValues('Loro Gin and Sake swirl', calories=200, fat=0, carbs=22, protein=0, serv_size=14)

    #Beer
    peticolas_royal_scandal = FoodValues('Peticolas Royal Scandal', calories=220, fat=0, carbs=25, protein=0, serv_size=16)
    peroni_16oz = FoodValues('Pernoi 16oz', calories=200, fat=0, carbs=15, protein=2, serv_size=16)
    anchor_steam_16oz = FoodValues('Anchor Steam 16oz', calories=200, fat=0, carbs=20, protein=2, serv_size=16)
    lakewood_lager_12oz = FoodValues('Lakewood Lager 12oz', calories=155, fat=0, carbs=16, protein=1, serv_size=12)
    shiner_12oz = FoodValues('Shiner Bock 12oz', calories=141, fat=0, carbs=14, protein=0, serv_size=12)
    shiner_16oz = FoodValues('Shiner Bock 16oz', calories=188, fat=0, carbs=16, protein=0, serv_size=16)
    modelo_12oz = FoodValues('Modelo 12oz', calories=120, fat=0, carbs=12, protein=0, serv_size=12)
    modelo_24oz = FoodValues('Modelo 24oz', calories=240, fat=0, carbs=24, protein=0, serv_size=24)
    modelo_32oz = FoodValues('Modelo 32oz', calories=384, fat=0, carbs=37, protein=3, serv_size=32)
    mosaic_ipa_12 = FoodValues('Mosaic IPA 12oz', calories=225, fat=0, carbs=14, protein=0, serv_size=12)
    mosaic_ipa_16 = FoodValues('Mosaic IPA 16oz', calories=288, fat=0, carbs=16, protein=0, serv_size=16)
    brooklyn_brewery_24oz = FoodValues('Brooklyn Brewery 24oz', calories=280, fat=0, carbs=32, protein=0, serv_size=24)
    sapporo_16oz = FoodValues('Sapporo 16oz', calories=186, fat=0, carbs=14, protein=0, serv_size=16)
    asahi_16oz = FoodValues('Asahi 16oz', calories=198, fat=0, carbs=14, protein=0, serv_size=16)
    singha_12oz = FoodValues('Singha 12oz', calories=120, fat=0, carbs=18, protein=0, serv_size=12)
    hite_12 = FoodValues('Hite Beer 12oz', calories=140, fat=0, carbs=14, protein=0, serv_size=12)
    hite_54 = FoodValues('Hite Beer 54oz', calories=700, fat=0, carbs=60, protein=4, serv_size=54)
    

    # Oat Combos
    hu_k_almond_crunch_oats = sum([oats, hu_kitchen_almond_crunch/2])
    pb_banana_oats = sum([oats, banana, wc_peanut_butter])
    
    # Breakfast
    bkfast_burrito = sum([3 * egg, cheese, bacon, corn_tortilla])
    
    # Popular Combos
    hemp_coco_shake = sum([coco_water_8oz * 2, wf_hemp_protein])
    hemp_coco_shake_ultra = sum([coco_water_8oz * 2, wf_hemp_protein*2])
    omelette = sum([egg*3,butter])
    pb_toast = sum([dkb_slice,wc_peanut_butter])
    chorizo_egg_tacos = sum([egg*3,beef_chorizo,mission_corn_tortillas])
    wc_pb_sandwich = sum([wf_multi_seed_bread*2, wc_peanut_butter])
    blueberry_parfait = sum([coco_water_8oz / 2 , cottage_chz_110g, blueberries_140g/2, protein_shake])
    mango_protein_parfait = sum([coco_water_8oz / 2 , cottage_chz_110g, mango_chunks_140g/2,
                                 avo_chunks_50g,protein_shake])
    chinga_wingz = sum([chicken_wings_4oz*4,shallot*2,soy_sauce/2,
                        lite_brown_sugar/2,bosc_pear])
    steak_fried_rice = sum([prolific_beef_round_8oz/2,sweet_onion/2,
                        thai_chili_sauce,butter,white_rice_6oz,egg])

    # Kitchen Prep
    pesto_chkn_pasta = sum([chickpea_pasta*4, pesto_paste*2,
                            sweet_onion,butter*2,chicken_breast_6oz*3])
    
                                          


    todays_combo = sum([chicken_breast_1oz*8,yams_100g*3,
                        thai_chili_sauce,brussels_100g*2,
                        butter*2])

        
    
    # Add manually
    # bkfast_burrito = 3 * egg + cheese + bacon + corn_tortilla
    # Or use sum, the main reason to implement addition to 0


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
