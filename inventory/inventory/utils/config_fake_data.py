from faker import Faker
import random

faker = Faker(['pt-br'])

class ConfigData:
    def data_company(self):    
        fake_profile = faker.profile()

        id = (faker.text()[0:3].split(' ')[0]).join(str([faker.random_int()][0:2][0]))[0:5]
        company_name = faker.company()
        company_phone = faker.msisdn()[2:]
        company_mail = fake_profile['mail']
        company_website = fake_profile['website'][0]

        return{
            'id': id,
            'name': company_name,
            'phone': company_phone,
            'mail' : company_mail,
            'site' : company_website,
        }

    def data_product(self, entity):        

        products = ['lápis', 'caneta', 'borracha', 'caderno', 'notebook', 'mouse', 'teclado', 'fone de ouvido', 'lapiseira', 'relógio', 'roda', 'papel']

        list_ids_group_products = entity.objects.values_list('id') 
        semi_formated = faker.pricetag()
        position_semi_formated = semi_formated.index(',')
        
        name = faker.words(1, products, True)[0]
        unit = faker.random_int()
        price = semi_formated[2:position_semi_formated].replace('.', '')    
        active = faker.boolean()
        foreign_key = entity(random.choice(list_ids_group_products)[0])

        return {
            'name' : name,
            'unit' : unit,
            'price' : price,
            'active' : active,
            'foreign_key' : foreign_key,
        }

    def data_group_product(self):    
        groups = ["material escolar", "tecnologia", "meio ambiente", "tinta", "material de limpeza",]
        name = faker.words(1, groups, True)[0]
        active = faker.boolean()

        return {
            'name' : name,
            'active' : active,
        }

    def data_stock(self, product_atrib, company_atrib):   
        quantity = faker.random_int()
        last_update = faker.date_time()
        list_ids_product = product_atrib.objects.values_list('id')
        list_ids_company = company_atrib.objects.values_list('id')
        id_product = product_atrib(random.choice(list_ids_product)[0])
        id_company = company_atrib(random.choice(list_ids_company)[0])

        return {
            'quantity' : quantity,
            'last_update' : last_update,
            'id_product' : id_product,
            'id_company' : id_company,
        }