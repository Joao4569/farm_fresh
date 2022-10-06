from django.db import models


class Category(models.Model):
    """This model will contain each product category and
    it's related attributes and model methods"""

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        """This string model method will take the category itself and
        return it's firendly name for a better UX on the admin site"""

        return self.friendly_name

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
        verbose_name_plural = 'Packaging'

    name = models.CharField(max_length=254, null=True, blank=True)

    # how to implement choice field taken from stackoverflow
    PIECE = 'Piece'
    BAG = 'Bag'
    BOTTLE = 'Bottle'
    JAR = 'Jar'

    PACKAGING_CHOICES = [
        (PIECE, 'Piece'),
        (BAG, 'Bag'),
        (BOTTLE, 'Bottle'),
        (JAR, 'Jar'),
    ]

    packaging_type = models.CharField(
        max_length=50,
        choices=PACKAGING_CHOICES,
    )

    KG1 = '1 Kg'
    G500 = '500g'
    G250 = '250g'
    G100 = '100g'
    LT1 = '1 ltr'
    LT2 = '2 ltrs'
    CA250350 = 'ca. 250-350g'

    WEIGHT_CHOICES = [
        (KG1, '1 Kg'),
        (G500, '500g'),
        (G250, '250g'),
        (G100, '100g'),
        (LT1, '1 Ltr'),
        (LT2, '2 Ltrs'),
        (CA250350, 'ca. 250-350g'),
    ]

    weight = models.CharField(
        max_length=50,
        choices=WEIGHT_CHOICES,
    )

    def __str__(self):
        """This string model method will take the packaging object itself and
        return its name"""

        return self.name
