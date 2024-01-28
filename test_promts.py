revenue = """Проанализируй таблицу выручки компании за год
Статья,Год,Январь,Февраль,Март,Апрель,Май,Июнь,Июль,Август,Сентябрь,Октябрь,Ноябрь,Декабрь
ПМУ ХиИ,95178715.76,4865887.00,7112164.00,10431657.00,11028230.00,10100641.00,9927427.00,6825255.86,12167418.16,9950405.12,12769630.62,0.00,0.00
ПМУ Ортопедия,127889434.33,6206199.00,9596160.00,13831894.00,15086639.00,12060727.00,14868321.00,9367850.33,17260044.32,14333651.68,15277948.00,0.00,0.00
ПМУ Ортодонтия,17663825.00,829195.00,1732710.00,767510.00,1514800.00,1574290.00,2199970.00,1858350.00,2516670.00,2451860.00,2218470.00,0.00,0.00
ПМУ Терапия и детство,32791768.98,2982708.00,2793359.00,3337487.00,3355930.00,3650747.00,3932291.00,2524760.65,3661948.40,2914458.50,3638079.43,0.00,0.00
ДМС,1786680.00,88870.00,129660.00,211620.00,209685.00,177930.00,146825.00,234660.00,157040.00,257200.00,173190.00,0.00,0.00
ПМУ товары,108765.00,77400.00,15892.00,2050.00,0.00,9690.00,850.00,548.00,1350.00,635.00,350.00,0.00,0.00
ОМС,178532.28,17323.14,147601.77,13607.37,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00
Итого,275597721.35,15067582.14,21527546.77,28595825.37,31195284.00,27574025.00,31075684.00,20811424.84,35764470.88,29908210.30,34077668.05,0.00,0.00
"""

variable_production = """Проанализируй таблицу переменных производсвенных компании за год
ФОТ производственного персонала|Хирургия и имплантация,-15315918.63,-957771.85,-1321216.60,-2031594.77,-2060689.30,-1729823.94,-2029600.79,-1248873.69,-2189488.93,-1746858.77,0.00,0.00,0.00
ФОТ производственного персонала|Ортопедия,-22873944.24,-1166837.64,-1926349.43,-2902476.52,-3103956.21,-2302023.23,-3404307.87,-1847901.90,-3334527.22,-2885564.22,0.00,0.00,0.00
ФОТ производственного персонала|Ортодонтия,-3342489.04,-233591.84,-449371.80,-191899.00,-350389.00,-348550.10,-484657.66,-322018.20,-467803.80,-494207.64,0.00,0.00,0.00
ФОТ производственного персонала|Терапия и детство,-6764361.74,-618936.79,-667847.88,-866614.63,-882152.52,-973385.04,-694286.33,-627748.72,-882816.37,-550573.46,0.00,0.00,0.00
ФОТ производственного персонала|Ассистенты,-10723805.67,-716124.42,-739150.98,-1058945.65,-1121221.43,-1243830.40,-1342920.79,-1275601.93,-1605885.88,-1601971.19,-18153.00,0.00,0.00
Расходники|Аптека и анестезия|Напрямую в ОПИУ,-404149.96,-35500.00,0.00,-25000.00,-43156.00,-113585.00,-21967.56,-23003.03,-22156.00,-119782.37,0.00,0.00,0.00
Расходники|ЗТЛ|Напрямую в ОПИУ,-24820590.00,-1720190.00,-1791700.00,-3099360.00,-2667380.00,-3502430.00,-2984060.00,-2515800.00,-3822620.00,-2717050.00,0.00,0.00,0.00
Эквайринг,-2761549.56,-232597.53,-294820.11,-410602.30,-408986.00,-534477.00,-336829.39,-166187.83,-215397.95,-161651.45,0.00,0.00,0.00
РасходникиХиИ|Хирургические шаблоны|Напрямую в ОПИУ),-1158960.00,-70000.00,-248000.00,-360.00,-220000.00,-3000.00,-119000.00,0.00,-334600.00,-164000.00,0.00,0.00,0.00
Закупка товаров,-319404.00,-140000.00,-61442.00,-1700.00,-12350.00,-23132.00,-44750.00,-25008.00,-11022.00,0.00,0.00,0.00,0.00
Расходники|КТ|Напрямую в ОПИУ,-941400.00,-120780.00,-170370.00,-180810.00,-172530.00,-64080.00,-65520.00,-96840.00,-70470.00,0.00,0.00,0.00,0.00
Расх.ДДС|Общие,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00
Общие+хирургические(23/1),-15543402.00,-1565724.00,-1870625.00,-3917798.00,-2848227.00,-3223452.00,-2117576.00,0.00,0.00,0.00,0.00,0.00,0.00
Расх.1С|Мелкое мед.оборудование и медицинское ТМЦ,-1021008.00,0.00,0.00,0.00,0.00,0.00,0.00,-25661.00,-61609.00,-933738.00,0.00,0.00,0.00
Расх.1С|Общее(ЦСО и пр.),-601185.00,0.00,0.00,0.00,0.00,0.00,0.00,-161797.00,-183947.00,-255441.00,0.00,0.00,0.00
Расх.1С|Ортопедия,-3560885.00,0.00,0.00,0.00,0.00,0.00,0.00,-1450584.00,-1074267.00,-1036034.00,0.00,0.00,0.00
Расх.1C|Ортодонтия,-1060051.00,0.00,0.00,0.00,0.00,0.00,0.00,-225215.00,-349691.00,-485145.00,0.00,0.00,0.00
Расх.1С|Такси.доставка и пр.,-27633.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,-24851.00,-2782.00,0.00,0.00,0.00
Расх.1С|Терапия и детство,-792479.00,0.00,0.00,0.00,0.00,0.00,0.00,-338254.00,-207055.00,-247170.00,0.00,0.00,0.00
Расх.1С|ХиИ,-6089015.00,0.00,0.00,0.00,0.00,0.00,0.00,-1656315.00,-2406080.00,-2026620.00,0.00,0.00,0.00
Расх.ДДС|ХиИ,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00
Расх.ДДС|Ортодонтия,-1349199.61,-151107.28,-194424.35,-93267.15,-245925.58,-365268.74,-299206.51,0.00,0.00,0.00,0.00,0.00,0.00
ФОТМОП,-4020827.00,-354409.00,-626568.00,-754013.00,-651823.00,-322525.00,-449523.00,-120586.00,-535445.00,-205935.00,0.00,0.00,0.00
Списания ДМС|с нашей стороны,-338836.00,-4990.00,-21000.00,-59761.00,-78675.00,-60285.00,-24520.00,-55575.00,-18030.00,-16000.00,0.00,0.00,0.00
Списание ДМС|от компаний,-11970.00,0.00,-3990.00,-3990.00,0.00,0.00,-3990.00,0.00,0.00,0.00,0.00,0.00,0.00
Итого,-123843063.45,-8088560.35,-10386876.15,-15598192.01,-14867461.05,-14809847.46,-14422715.90,-12182970.29,-17817763.15,-15650524.10,-18153.00,0.00,0.00
"""