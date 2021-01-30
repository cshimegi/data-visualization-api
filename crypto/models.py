from django.db import models
from unixtimestampfield.fields import UnixTimeStampField

# Create your models here.
class ICandle(models.Model):
    ''' Candle Model Interface

    '''
    # properties
    open   = models.FloatField()
    high   = models.FloatField()
    low    = models.FloatField()
    close  = models.FloatField()
    volume = models.FloatField()
    period = UnixTimeStampField(use_numeric = True, default = 0.0)

    class Meta:
        abstract = True # prevent this from migration

class VechainCandle(ICandle):
    ''' VeChain Candle Data Model

    '''
    # constants
    EXCHANGE = 'binance'
    INTERVAL = 'm1'
    BASE_ID  = 'vechain'
    QUOTE_ID = 'bitcoin'

    class Meta:
        verbose_name = 'CoinCap VeChain candle data table'
        verbose_name_plural = verbose_name
        indexes = [
            models.Index(fields = ['period'], name = "idx_vechain_candle_period"),
        ]
        ordering = ['-period']