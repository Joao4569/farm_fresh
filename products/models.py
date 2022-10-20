from django.db import models
# taken directly from Boutique Ado and customised for Farm Fresh


class Category(models.Model):
    """This model contains each product category and
    it's related attributes and model methods"""

    class Meta:
        """This model meta class will display the correct spelling of
        the plural of category, django just adds a single s to the end
        of the word, which is incorrect in this case"""
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        """This string model method will take the categoy object itself
        and return its name"""

        return self.name

    def get_friendly_name(self):
        """This model method will take the category itself and
        return it's friendly name"""

        return self.friendly_name


class Product(models.Model):
    """This model will contain each products information and
    it's related attributes and model methods"""

    category = models.ForeignKey('Category', null=True, blank=True,
                                 on_delete=models.SET_NULL)
    producer = models.ForeignKey('Producer', null=True, blank=True,
                                 on_delete=models.SET_NULL)
    packaging = models.ForeignKey('Packaging', null=True, blank=True,
                                  on_delete=models.SET_NULL)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(null=True, blank=True)
    organic = models.BooleanField(default=False)
    in_season = models.BooleanField(default=False)

    def __str__(self):
        """This string model method will take the product itself and
        return its name"""

        return self.name


class Producer(models.Model):
    """This model will contain each producer and
    it's related attributes and model methods"""

    name = models.CharField(max_length=254)
    description = models.TextField()
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        """This string model method will take the producer itself and
        return its name"""

        return self.name


class Packaging(models.Model):
    """This model will contain packaging information and
    related attributes"""

    class Meta:
        """This model meta class will display the correct spelling of
        the plural of packaging, django just adds a single s to the end
        of the word, which is incorrect in this case"""
        verbose_name_plural = 'Packaging'

    name = models.CharField(max_length=254, null=True, blank=True)

    """how to implement choice field taken from stackoverflow, credited in
    readme"""
    PIECE = 'Piece'
    BAG = 'Bag'
    BOX = 'Box'
    BOTTLE = 'Bottle'
    JAR = 'Jar'
    PWRAP = 'Plastic Wrap'
    FWRAP = 'Foil Wrap'

    PACKAGING_CHOICES = [
        (PIECE, 'Piece'),
        (BAG, 'Bag'),
        (BOX, 'Box'),
        (BOTTLE, 'Bottle'),
        (JAR, 'Jar'),
        (PWRAP, 'Plastic Wrap'),
        (FWRAP, 'Foil Wrap'),
    ]

    packaging_type = models.CharField(
        max_length=50,
        choices=PACKAGING_CHOICES,
    )

    KG1 = '1 Kg'
    G500 = '500g'
    G250 = '250g'
    G200 = '200g'
    G120 = '120g'
    G100 = '100g'
    LT1 = '1 ltr'
    ML390 = '390ml'
    ML500 = '500ml'
    CA250350 = 'ca. 250-350g'
    CA911 = 'ca. 0.9-1.1kg'
    G5310pc = '10 pieces of 53g+'

    WEIGHT_CHOICES = [
        (KG1, '1 Kg'),
        (G500, '500g'),
        (G250, '250g'),
        (G200, '200g'),
        (G120, '120g'),
        (G100, '100g'),
        (LT1, '1 Ltr'),
        (ML390, '390ml'),
        (ML500, '500ml'),
        (CA250350, 'ca. 250-350g'),
        (CA911, 'ca. 0.9 - 1.1kg'),
        (G5310pc, '10 pieces of 53g+'),
    ]

    weight = models.CharField(
        max_length=50,
        choices=WEIGHT_CHOICES,
    )

    def __str__(self):
        """This string model method will take the packaging object itself and
        return its name"""

        return self.name
