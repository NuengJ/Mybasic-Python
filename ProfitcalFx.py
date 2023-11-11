minimumorder = 0.01
calmove = 100
thb = 36
basicprofit = (minimumorder*calmove)*thb
profitratio = 2

def profit(lot,target) :
    profit_cal = (lot*target)*thb
    stoploss = profit_cal/profitratio
    stoploss_target = target/profitratio
    print('กำไรเป้าหมาย: {} บาท' .format(profit_cal))
    print('ขนาดlot ที่เข้า: {} บาท ระยะ targetpoint: {} จุด' .format(lot,target))
    print('ขาดทุนถ้าผิดทางที่: {} บาท' .format(stoploss))
    print('ระยะ stoploss: {} จุด' .format(stoploss_target))

    
profit(0.01,1000)    
    

