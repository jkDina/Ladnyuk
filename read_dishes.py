with open('C:/Users/user/AppData/Local/Programs/Python/Python36-32/netology/dihes.py', encoding = 'utf8' ) as f:
    count = 0
    line=[]
    for line in f:
        eggs = line
        print("Блюдо:", eggs)
        ingradients = f.readline()
        print("Инградиенты в штуках:", ingradients)
        items = f.readline()
        print("Количество продуктов:", items)
        items = f.readline()
        print("Количество продуктов:", items)
        gap = f.readline()
        print("", gap)
        count +=1
        if count ==1:
            for line in f:
                steak=line
                print("Блюдо:", steak)
                ingradients = f.readline()
                print("Инградиенты в штуках:", ingradients)
                items1 = f.readline()
                print("Количество продуктов:", items1)
                items2 = f.readline()
                print("Количество продуктов:", items2)
                items3 = f.readline()
                print("Количество продуктов:", items3)
                
                gap = f.readline()
                print("", gap)
                count+=1
                
                if count == 2:
                  for line in f:
                      salad=line
                      print("Блюдо:", salad)
                      ingradients = f.readline()
                      print("Инградиенты в штуках:", ingradients)
                      items1 = f.readline()
                      print("Количество продуктов:", items1)
                      items2 = f.readline()
                      print("Количество продуктов:", items2)
                      items3 = f.readline()
                      print("Количество продуктов:", items3)
                      items4 = f.readline()
                      print("Количество продуктов:", items4)
                      gap = f.readline()
                      print("", gap)
                      break
        
            
      
        
        
        
        





        
        
        




