import csv
from django.core.management.base import BaseCommand
from api.models import fooddata
import pandas as pd
class Command(BaseCommand):
    help = 'Load data from CSV file into fooddata model'

    def add_arguments(self, parser):
        parser.add_argument('csv_file_path', type=str, help='Path to the CSV file')

    def handle(self, *args, **kwargs):
        csv_file_path = kwargs['csv_file_path']
        self.load_data_from_csv(csv_file_path)

    def load_data_from_csv(self, csv_file_path):
        try:
            df = pd.read_csv(csv_file_path,encoding='latin1')
            for index, row in df.iterrows():
                fooddata.objects.create(
                    area_abbreviation_1=row['Area Abbreviation'],
                    area_abbreviation_2=row['Area Abbreviation'],
                    area_abbreviation_3=row['Area Abbreviation'],
                    item_code=int(row['Item Code']),
                    element_code=int(row['Element Code']),
                    element=row['Element'],
                    unit=row['Unit'],
                    latitude=float(row['latitude']),
                    longitude=float(row['longitude']),
                    Y1961=float(row['Y1961']),
                    Y1962=float(row['Y1962']),
                    Y1963=float(row['Y1963']),
                    Y1964=float(row['Y1964']),
                    Y1965=float(row['Y1965']),
                    Y1966=float(row['Y1966']),
                    Y1967=float(row['Y1967']),
                    Y1968=float(row['Y1968']),
                    Y1969=float(row['Y1969']),
                    Y1970=float(row['Y1970']),
                    Y1971=float(row['Y1971']),
                    Y1972=float(row['Y1972']),
                    Y1973=float(row['Y1973']),
                    Y1974=float(row['Y1974']),
                    Y1975=float(row['Y1975']),
                    Y1976=float(row['Y1976']),
                    Y1977=float(row['Y1977']),
                    Y1978=float(row['Y1978']),
                    Y1979=float(row['Y1979']),
                    Y1980=float(row['Y1980']),
                    Y1981=float(row['Y1981']),
                    Y1982=float(row['Y1982']),
                    Y1983=float(row['Y1983']),
                    Y1984=float(row['Y1984']),
                    Y1985=float(row['Y1985']),
                    Y1986=float(row['Y1986']),
                    Y1987=float(row['Y1987']),
                    Y1988=float(row['Y1988']),
                    Y1989=float(row['Y1989']),
                    Y1990=float(row['Y1990']),
                    Y1991=float(row['Y1991']),
                    Y1992=float(row['Y1992']),
                    Y1993=float(row['Y1993']),
                    Y1994=float(row['Y1994']),
                    Y1995=float(row['Y1995']),
                    Y1996=float(row['Y1996']),
                    Y1997=float(row['Y1997']),
                    Y1998=float(row['Y1998']),
                    Y1999=float(row['Y1999']),
                    Y2000=float(row['Y2000']),
                    Y2001=float(row['Y2001']),
                    Y2002=float(row['Y2002']),
                    Y2003=float(row['Y2003']),
                    Y2004=float(row['Y2004']),
                    Y2005=float(row['Y2005']),
                    Y2006=float(row['Y2006']),
                    Y2007=float(row['Y2007']),
                    Y2008=float(row['Y2008']),
                    Y2009=float(row['Y2009']),
                    Y2010=float(row['Y2010']),
                    Y2011=float(row['Y2011']),
                    Y2012=float(row['Y2012']),
                    Y2013=float(row['Y2013']),
                   
                )
                self.stdout.write(self.style.SUCCESS(f'Entery Added!{index}'))
            self.stdout.write(self.style.SUCCESS('Data loaded successfully- Completed'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error loading data: {str(e)}'))
