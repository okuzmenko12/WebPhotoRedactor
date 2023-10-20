from django.db import models


class TitleTextAbstractModel(models.Model):
    title = models.CharField(max_length=250,
                             verbose_name='Title')
    text = models.TextField(max_length=10000,
                            verbose_name='Text')

    class Meta:
        abstract = True


class Preference(TitleTextAbstractModel):

    class Meta:
        db_table = 'preferences'
        verbose_name = 'preference'
        verbose_name_plural = 'Preferences'

    def __str__(self):
        return f'Preference: {self.title}'


class MainFaq(TitleTextAbstractModel):

    class Meta:
        db_table = 'main_faqs'
        verbose_name = 'faq'
        verbose_name_plural = 'Main FAQs'

    def __str__(self):
        return f'Faq: {self.title}'


class PricingFaq(MainFaq):

    class Meta:
        db_table = 'pricing_faqs'
        verbose_name = 'faq'
        verbose_name_plural = 'Pricing FAQs'
