from inventory.utils.config_fake_data import ConfigData

class PopulateData:

    def __init__(self, company, product, productGroup, stock):
        self.company = company
        self.product = product
        self.productGroup = productGroup
        self.stock = stock
        self.fake_data = ConfigData()

    def populate_with_fake_data_company(self, quantity):        
        for i in range(0, quantity):           
            data = self.fake_data.data_company()
            instance = self.company.objects.create(
                id=data['id'], 
                name=data['name'], 
                phone=data['phone'],
                mail=data['mail'], 
                site=data['site'],
            )
            instance.save()            
            
    def populate_with_fake_data_product(self, quantity):        
        for i in range(0, quantity):
            data = self.fake_data.data_product(self.productGroup)
            instance = self.product.objects.create(
                name=data['name'],
                unit=data['unit'],
                price=data['price'],
                active=data['active'],
                product_group=data['foreign_key']
            )
            instance.save()
           
    def populate_with_fake_data_product_group(self, quantity):
        for i in range(0, quantity):
            data = self.fake_data.data_group_product()
            instance = self.productGroup.objects.create(
                name=data['name'],
                active=data['active']
            )
            instance.save()
    
    def populate_with_fake_data_stock(self, quantity):
        for i in range(0, quantity):
            data = self.fake_data.data_stock(self.product, self.company)
            instance = self.stock.objects.create(
                quantity=data['quantity'],
                last_update=data['last_update'],
                product_in_stock=data['id_product'],
                company=data['id_company']
            )
            instance.save()
    
    def clean_all_data_in_tables(self):
        self.product.objects.all().delete()
        self.company.objects.all().delete()
        self.productGroup.objects.all().delete()
        self.stock.objects.all().delete()