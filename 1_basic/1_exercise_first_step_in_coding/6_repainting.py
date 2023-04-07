protective_layer_sqr_m = int(input())
paint_liters = int(input())
paint_razreditel_liters = int(input())
working_hours = int(input())

protective_layer_sqr_m_price = 1.50
paint_liters_price = 14.50
paint_razreditel_liters_price = 5.00


workers_payment =(((((protective_layer_sqr_m_price*(protective_layer_sqr_m+2))+(paint_liters_price*paint_liters*1.1)+
                paint_razreditel_liters*paint_razreditel_liters_price)+0.40))*0.3)*working_hours

price_for_materials = ((((protective_layer_sqr_m_price*(protective_layer_sqr_m+2))+(paint_liters_price*paint_liters*1.1)+
                paint_razreditel_liters*paint_razreditel_liters_price)+0.40))

total = price_for_materials +workers_payment
print(total)

