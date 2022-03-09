from megasena.utils.purify_data import purify_data_in_tsv
import datetime

class Upload:
    def __init__(self, name, modelMegaSena):
        self.name = name
        self.model = modelMegaSena

    def handling_data_in_tsv_file(self): 
        data = purify_data_in_tsv(self.name, 8)        
        for i in range(1, len(data)):                      
            instance = self.model.objects.create(
                contest=data[i][0],
                date=datetime.datetime.strptime(data[i][1], '%d/%m/%Y'),
                orb_1=data[i][2],
                orb_2=data[i][3],
                orb_3=data[i][4],
                orb_4=data[i][5],
                orb_5=data[i][6],
                orb_6=data[i][7],
            )
            instance.save()
    
    def remove_all_data_uploaded(self):       
        self.model.objects.all().delete()