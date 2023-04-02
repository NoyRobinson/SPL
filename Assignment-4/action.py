from persistence import *

import sys

def main(args : list[str]):
    inputfilename : str = args[1]
    with open(inputfilename) as inputfile:
        for line in inputfile:
            splittedline : list[str] = line.strip().split(", ")
            #TODO: apply the action (and insert to the table) if possible

            #supply
            if int(splittedline[1]) > 0:
                product_object = repo.products.find(id = int(splittedline[0]))
                if len(product_object) == 0:
                    continue
                new_quantity = product_object[0].quantity + int(splittedline[1])
                repo.products.update(product_object[0], quantity = new_quantity)
                activitie_object = Activitie(splittedline[0], splittedline[1], splittedline[2], splittedline[3])
                repo.activities.insert(activitie_object)
            
            #sell
            elif int(splittedline[1]) < 0:
                product_object = repo.products.find(id = int(splittedline[0]))
                if len(product_object) == 0:
                    continue
                new_quantity = product_object[0].quantity + int(splittedline[1])
                if(new_quantity >= 0):
                    repo.products.update(product_object[0], quantity = new_quantity)
                    activitie_object = Activitie(splittedline[0], splittedline[1], splittedline[2], splittedline[3])
                    repo.activities.insert(activitie_object)
                    

if __name__ == '__main__':
    main(sys.argv)