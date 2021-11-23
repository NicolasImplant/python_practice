from datetime import datetime as dt
import pytz

bogota_timezome = pytz.timezone('America/Bogota')
bogota_date = dt.now(bogota_timezome)
print('Bogota: ', bogota_date.strftime('%d/%m/%Y, %H:%M:%S'))

mexico_timezome = pytz.timezone('America/Mexico_City')
mexico_date = dt.now(mexico_timezome)
print('Ciudad de mexico: ', mexico_date.strftime('%d/%m/%Y, %H:%M:%S'))

caracas_timezome = pytz.timezone('America/caracas')
caracas_date = dt.now(caracas_timezome)
print('Ciudad de caracas: ', caracas_date.strftime('%d/%m/%Y, %H:%M:%S'))